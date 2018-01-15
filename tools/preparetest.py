# coding:utf-8
import os
from selenium import webdriver

pathRoot = os.path.dirname(os.path.abspath(__file__))


class TestTools(object):
    driver = webdriver.Chrome()

    @staticmethod
    def driverchoice(browsername, url):
        if browsername == "chrome":
            edriver = webdriver.Chrome(executable_path=pathRoot + r'\resources\drivers\chromedriver.exe')
            gotdriver = True
        elif browsername == "firefox":
            edriver = webdriver.Chrome(executable_path=pathRoot + r'\resources\drivers\gechodriver.exe')
            gotdriver = True
        else:
            print('you need input a validate browser name form chrome firefox')
            gotdriver = False

        if gotdriver:
            driver = edriver
            driver.get(url)

    @staticmethod
    def teardown(driver):
        driver.close()
        driver.quit
