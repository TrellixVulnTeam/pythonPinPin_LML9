# coding:utf-8
import os
from selenium import webdriver


class TestTools():

    def driverchoice(self, browsername, url, path):
        if browsername == "chrome":
            edriver = webdriver.Chrome(executable_path=path + r'\resources\drivers\chromedriver.exe')
            gotdriver = True
        elif browsername == "firefox":
            edriver = webdriver.Chrome(executable_path=path + r'\resources\drivers\gechodriver.exe')
            gotdriver = True
        else:
            print('you need input a validate browser name form chrome firefox')
            gotdriver = False

        if gotdriver:
            self.driver = edriver
            self.driver.get(url)

    def getDriver(self):
        return self.driver

    def teardown(self, driver):
        driver.close()
        driver.quit




