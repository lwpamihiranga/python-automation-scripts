from selenium import webdriver
from getpass import getpass
from time import sleep

# usr = input("Enter your twitter username or email: ")
# pwd = getpass("Enter your twitter password: ")
msg = input("Enter your tweet: ")

usr = "your email here"
pwd = "your password here"

driver = webdriver.Firefox()
driver.get("https://twitter.com/")


username_box = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[1]/input")
username_box.send_keys(usr)
sleep(3)

password_box = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div[1]/div[1]/div[1]/form/div[2]/input")
password_box.send_keys(pwd)
sleep(3)

login_btn = driver.find_element_by_class_name("submit")
login_btn.submit()
# sleep(3)

# text_box = driver.find_element_by_xpath(
#     "/html/body/div[1]/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
# text_box.send_keys(msg)
# sleep(3)

# tweet_button = driver.find_element_by_xpath(
#     "/html/body/div[1]/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[3]")
# tweet_button.click()
