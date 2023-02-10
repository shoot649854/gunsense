import numpy as np
from numpy import random
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import time

class AutoScraping():
    def __init__(self):
        return 0

    def checkup():
        options = Options()
        Chrome_Options = Options()
        options.add_argument('--headless')
        executable_path = '/Users/shotomorisaki/Desktop/RSA_Comany_Scrape/chromedriver'
        browser = webdriver.Chrome(executable_path, options = options)
    
    def quitWebdriver(browser):
        browser.quit()

    def scriptByClass(browser, url, class_element, array):
        browser.get(url)
        element = browser.find_element_by_class_name(class_element)
        element.click()
        array.append(element)
    
    def scriptByXPath(browser, url, xPath_element, array):
        browser.get(url)
        elem = browser.find_element_by_xpath(xPath_element)
        print(elem.text)
        array.append(elem)
    
    

