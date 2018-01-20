# coding udt-8
import unittest

import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from tools import preparetest
from tools import fileoprate

class TestCase():
    pathRoot = os.path.dirname(os.path.abspath(__file__))
    prepare = preparetest.TestTools()

    def __init__(self):
        url = "https://pinpineat.com/#!/login"
        self.prepare.driverchoice('chrome', url, self.pathRoot)
        self.driver = self.prepare.getDriver()
        self.wait = WebDriverWait(self.driver, 30)

    def test_login_xls(self):
        path= self.pathRoot+r'\resources\parameter.xlsx'
        file=fileoprate.fileoperate
        parameter=file.read_xls(path,0)
        i=0
        for i in range(len(parameter)):
            print()

    def test_login_positive(self):
        driver = self.driver
        wait = self.wait
        user_email = driver.find_element_by_xpath("//*[@id='username']")
        user_pass = driver.find_element_by_xpath("//*[@id='password']")
        login_btn = driver.find_element_by_xpath("//*[@id='loginDiv']/div[2]/div/form/div[3]/button")
        # operation on webpage
        user_email.send_keys("12@12.com")
        user_pass.send_keys("123456")
        login_btn.click()
        # assert change to user page
        user_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='myNavBar']/ul/li[2]/a/span/span[2]")))
        # user_btn = driver.find_element_by_xpath("//*[@id='myNavBar']/ul/li[2]/a/span/span[2]")
        assert "User" in user_btn.text
        print(user_btn.text)
        user_btn.click()
        user_ver = wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='view']/div/div[2]/div/h3")))
        print(user_ver.text)
        assert "12@12.com" in user_ver.text

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    t = TestCase()
    t.test_login_positive()
    t.tearDown()
