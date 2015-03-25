#!/usr/bin/env python
__author__ = 'Xplore'
import os
import sys
import time
import urllib
import urllib2
import xml.dom.minidom as XML

username = raw_input("enter user id :")
def sendLogoutRequest(username):
    url = 'https://192.168.100.1:8090/httpclient.html'
    post_data = 'mode=193' + '&username=' + username
    req = urllib2.Request(url, post_data)
    response = urllib2.urlopen(req)
    print response
    print 'logout.'

sendLogoutRequest(username)
