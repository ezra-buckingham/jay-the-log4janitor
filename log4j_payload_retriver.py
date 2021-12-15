import requests
import argparse
import logging
import ldap
import calendar
import time

def main():

  gmt = time.gmtime()
  timestamp = calendar.timegm(gmt)
  
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('-q', '--query', dest='query',help='Full LDAP query to get payload back from \n ex) "ldap://3.144.191.136:1389/#log4j"')
  parser.add_argument('-l', '--log-file',default=f"log4j_payload_{timestamp}.log",dest='log_file',help='File to write logging out to')
  parser.add_argument('-o', '--output-file',default=f'output_file_{timestamp}.class',dest='output_file',help='File to write malicious class out to')

  args = parser.parse_args()

  # Configure the logging
  logging.basicConfig(filename=args.output_file, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

  query = args.query

  logging.info(f'Getting payload for {query}')
  try:
    basedn = "dc=scan"
    scope = ldap.SCOPE_SUBTREE
    ldap_server = ldap.initialize(query)
    response = ldap_server.search_s(basedn, scope)

    # Parse the response 
    http_endpoint = f'{(response[0][1]["javaCodeBase"][0]).decode("utf-8") }{(response[0][1]["javaFactory"][0]).decode("utf-8") }.class'
    logging.info(f'Found redirection to {http_endpoint}')

    try:
      http_response = requests.get(http_endpoint)
      log_info(f'Received payload')
      with open(args.output_file, 'w') as malClass:
        log_info(f'Writing java class to {args.output_file}')
        malClass.write(http_response.text)
        log_info(f'Java class succesfully written to {args.output_file}')
    except Exception as e:
      log_error(f'Some Exception Occured: {e}')

    logging.info(f'Received response from {query}')
  except Exception as e:
    log_error('Some Exception Occured: {e}')

def log_info(message):
  print(f'[*] {message}')
  logging.info(message)

def log_warn(message):
  print(f'[!] {message}')
  logging.warn(message)

def log_error(message):
  print(f'[X] {message}')
  logging.error(message)


if __name__ == '__main__':
  main()