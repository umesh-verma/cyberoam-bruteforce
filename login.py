import urllib
import time
import datetime
import urllib2
import sys
import xml.dom.minidom as XML

#CountDown And Credits
def countdown(num):
    for i in xrange(num,0,-1):
        time.sleep(1)
        sys.stdout.write(str(i%10)+'\r')
        sys.stdout.flush()
        
print 'MADE BY - "XPLORE" '
countdown(5)        

userid = raw_input("enter user id:")
passd = raw_input("enter pass:")

def sendLoginRequest(username, password):
    url = 'http://192.168.100.1:8090/httpclient.html'
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
        elif 'limit' in response:
            return True
        elif 'data' in response:
            return True
            
    except:
        return False    
if sendLoginRequest(userid, passd) == True:
    print 'success!!! and '+passd+' - password, userid -'+userid
