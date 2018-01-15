# coding udt-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tools import preparetest


class TestCase(unittest.TestCase):
    prepare = preparetest.TestTools()
    # driver = webdriver.chrome()

    def setUp(self):
        url = "https://pinpineat.com/"
        self.prepare.driverchoice('chrome', url)
        self.driver = self.prepare.driver

    def test_login(self):
        print("test_login")


    def tearDown(self):
        self.driver.quit()




