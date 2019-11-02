from selenium import webdriver
from getpass import getpass

# usr = input("Enter your facebook username or email: ")
# pwd = getpass("Enter your facebook password: ")

usr = "***REMOVED***"
pwd = "***REMOVED***"

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")

username_box = driver.find_element_by_id("email")
username_box.send_keys(usr)

password_box = driver.find_element_by_id("pass")
password_box.send_keys(pwd)

login_btn = driver.find_element_by_xpath('//*[@id="u_0_a"]')
login_btn.submit()
