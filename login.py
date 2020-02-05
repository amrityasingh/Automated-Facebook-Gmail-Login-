from selenium import webdriver 
from time import sleep
import subprocess as sp

x = sp.getoutput("whoami")
user = "bananaboi"
stat = 0

if(x==user):
        print("Welcome {}".format(x))
        stat = 1

print("Enter platform name to login into it ")
c=str(input())

if(c=='facebook'):
        usr='amritya.lordstark@gmail.com'
        pwd='xoxoxo69'

        driver = webdriver.Chrome() 
        driver.get('https://www.facebook.com/') 
        print ("Opened facebook") 
        sleep(1) 

        username_box = driver.find_element_by_id('email') 
        username_box.send_keys(usr) 
        print ("Email Id entered") 
        sleep(1) 

        password_box = driver.find_element_by_id('pass') 
        password_box.send_keys(pwd) 
        print ("Password entered") 
        login_box = driver.find_element_by_id('loginbutton') 
        login_box.click() 


elif(c=='gmail'):
   
        usr='amritya.stark'
        pwd='Yuphoria6999'
        driver= webdriver.Chrome()
        driver.get(('https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession'))
        sleep(2)

        username = driver.find_element_by_id('identifierId')
        username.send_keys(usr)
        nextButton = driver.find_element_by_id('identifierNext')
        nextButton.click()

        sleep(3)

        password_box = driver.find_element_by_name('password') 
        password_box.send_keys(pwd) 
	 
        signInButton = driver.find_element_by_id('passwordNext')
        signInButton.click()

else:
        print("Oh Snap! We don't currently support this platform")

print ("Done") 
input('Press anything to quit') 
driver.quit() 
print("Finished") 
