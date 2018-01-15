# coding udt-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tools import preparetest


class TestCase(unittest.TestCase):
    prepare = preparetest.TestTools()
    driver = webdriver.chrome()

    def setUp(self, browsername):
        url = "https://pinpineat.com/"
        self.prepare.driverchoice(browsername, url)
        self.driver = self.prepare.driver

    # def test_login(self):
