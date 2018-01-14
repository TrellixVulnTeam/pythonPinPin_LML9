# coding:utf-8
import os

from selenium import webdriver

pathRoot = os.path.dirname(os.path.abspath(__file__))


def driverchoice(self, browsername):
    if browsername == "chrome":
        driver = webdriver.Chrome(executable_path=pathRoot + r'\resources\drivers\chromedriver.exe')
        gotdriver = True
    elif browsername == "firefox":
        driver = webdriver.Chrome(executable_path=pathRoot + r'\resources\drivers\gechodriver.exe')
        gotdriver = True
    else:
        print('you need input a validate browser name form chrome firefox')
        gotdriver = False

    if gotdriver:
        driver.get("https://pinpineat.com/")


def teardown(self, driver):
    driver.close()
    driver.quit
