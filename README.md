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

## Fighting PIP

When you go to install the pip dependencies using:

```
pip3 install -r requirements.txt
```

You may see errors like:

```
  In file included from Modules/LDAPObject.c:3:
  Modules/common.h:15:10: fatal error: lber.h: No such file or directory
     15 | #include <lber.h>
        |          ^~~~~~~~
  compilation terminated.
  error: command '/usr/bin/x86_64-linux-gnu-gcc' failed with exit code 1
  ----------------------------------------
  ERROR: Failed building wheel for python-ldap
Failed to build python-ldap
ERROR: Could not build wheels for python-ldap which use PEP 517 and cannot be installed directly
```

If you see this error, please see [this stackoverflow post](https://stackoverflow.com/questions/4768446/i-cant-install-python-ldap)

## Why?

Inside the malicious classes are strings that can be used for further detection (IP addresses, commands, etc).
