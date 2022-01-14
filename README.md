# Jay the Log4Janitor

This tool will take a malicious LDAP query and pull back the malicious Java class hosted by an attacker.

## Usage

The usage of the script is simple...

```
usage: jay.py [-h] [-q QUERY] [-l LOG_FILE] [-o OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Full LDAP query to get payload back from. Example: "ldap://3.144.191.136:1389/#log4j"
  -l LOG_FILE, --log-file LOG_FILE
                        File to write logging out to
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        File to write malicious class out to
```

## Why?

Inside the malicious classes are strings that can be used for further detection (IP addresses, commands, etc).
