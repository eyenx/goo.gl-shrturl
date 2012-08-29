#!/usr/bin/python

### goo.gl url shortener

# mods

import sys
import os
import subprocess
import json

# vars



longurl = sys.argv[1]
key = 'AIzaSyDt3n_utWwGWprFFdMysqPIiMOvX9W5X88'
domain = 'https://www.googleapis.com/urlshortener/v1/url?key='
cmd = 'curl -s '+domain+key+' -H \'Content-Type: application/json\' -d \'{"longUrl":"'+longurl+'"}\''


# main

response = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
response = response.communicate()[0].decode()
#print(type(response))
#print(response)
index=json.loads(response)
shorturl=index["id"]
print('Here you go, it was xclipped...')
print('\nURL:\t'+shorturl+'\n')
echo=subprocess.Popen(['echo',shorturl],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
#xclip=subprocess.Popen(['xclip','-i','-se','c'],stdin=echo.stdout,stdout=subprocess.PIPE)
xclip=subprocess.Popen(['xclip','-i'],stdin=echo.stdout,stdout=subprocess.PIPE)
