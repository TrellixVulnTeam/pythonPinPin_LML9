# coding udt-8
import unittest

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tools import preparetest


class TestCase():
    pathRoot = os.path.dirname(os.path.abspath(__file__))
    prepare = preparetest.TestTools()

    def __init__(self):
        url = "https://pinpineat.com/#!/login"
        self.prepare.driverchoice('chrome', url, self.pathRoot)
        self.driver = self.prepare.getDriver()

    def test_login(self):
        print("gsdgs")

    def tearDown(self):
        self.driver.quit()


t=TestCase()

t.test_login()
t.tearDown()
