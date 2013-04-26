#!/usr/bin/python

### goo.gl url shortener

# mods

import sys
import subprocess as sub
import json as js
import urllib.request as ureq
#helper
def helper():
    if len(sys.argv)<2:
        print("\nno arguments found. you must provide a url!\n")
        sys.exit(1)

def main():
    helper()
    # vars
    longurl = sys.argv[1]
    key = 'AIzaSyDt3n_utWwGWprFFdMysqPIiMOvX9W5X88'
    domain = 'https://www.googleapis.com/urlshortener/v1/url?key='
    # main
    data='{"longUrl":"'+longurl+'"}'
    req=ureq.Request(domain+key,data.encode('utf-8'),{"Content-Type" : "application/json"})
    #get response and load json
    resp=js.loads(ureq.urlopen(req).read().decode('utf-8'))
    shrtrl=resp["id"]
    print('Here you go, it was xclipped...')
    print('\nURL:\t'+shrtrl+'\n')
    echo=sub.Popen(['echo',shrtrl],stdin=sub.PIPE,stdout=sub.PIPE)
    #xclip=sub.Popen(['xclip','-i','-se','c'],stdin=echo.stdout,stdout=sub.PIPE)
    xclip=sub.Popen(['xclip','-i'],stdin=echo.stdout)

if __name__=='__main__':
    main()
