import os
import sys
import selenium
from selenium import webdriver
#create variable file name using Cmd terminal
folderName = str(sys.argv[1])
#set webdriver to chrome browser
driver = webdriver.Chrome()
#function to create project folder
def makedirectory():
        #creates folder in new location
        os.mkdir(("C:/Users/Ignas/Documents/DjangoProjects/") + folderName)
if __name__ == '__main__':
    makedirectory()
# call chrome web browser
driver = webdriver.Chrome()

login = driver.find_element_by_id('login_field')
login.send_keys("your github login")
login = driver.find_element_by_id('password')
login.send_keys("your github password")


submit_button = driver.find_elements_by_xpath('//*[@id="login"]/form/div[3]/input[7]')[0]
submit_button.click()