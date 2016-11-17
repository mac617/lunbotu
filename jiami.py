#! /usr/bin/python

import cgi
import re
import urllib

form = cgi.FieldStorage() 

id = form.getvalue('id')
site_name = form.getvalue('name')

if id=="macheng":
    def getHtml(url):
        page = urllib.urlopen(url)
        html = page.read()
        return html
    url = "http://www.baidu.com"
    html = getHtml(url)
    print html
else:
    print "fuck you"