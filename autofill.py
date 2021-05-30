from selenium import webdriver
from getpass import getpass
import time

stuentid = input("Enter your id: ")
password = getpass("Enter your password: ")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://psns.cc.stonybrook.edu/psp/csprods/EMPLOYEE/CAMP/?cmd=login")

usernametextbox = driver.find_element_by_id("userid")
passwordtextbox = driver.find_element_by_id("pwd")


usernametextbox.send_keys(stuentid)
passwordtextbox.send_keys(password)

loginbutton = driver.find_element_by_xpath("//*[@id=\"login\"]/input[4]")
loginbutton.click()
