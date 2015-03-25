__author__ = 'Xplore'
import urllib
import time
import datetime
import urllib2
import xml.dom.minidom as XML
userid = raw_input("enter user id:")
password = raw_input("enter pass:")
def sendLoginRequest(username, password):
    url = 'https://192.168.100.1:8090/httpclient.html'
    post_data = 'mode=191' + '&username=' + username + '&password=' + password
    try:
        req = urllib2.Request(url, post_data)
        response = urllib2.urlopen(req)
        xml_dom = XML.parseString(response.read())
        document = xml_dom.documentElement
        response = document.getElementsByTagName('message')[0].childNodes[0].nodeValue
        print response
        if 'successfully' in response:
            return True
            
    except:
        return False

sendLoginRequest(userid, password)
    
