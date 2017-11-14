from django.test import TestCase

# Create your tests here.
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://savvymavvies.pythonanywhere.com")
        time.sleep(5)
        elem = driver.find_element_by_link_text("Intro to MIT App Inventor").click()
        time.sleep(10)
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys(2)
        time.sleep(10)
        elem = driver.find_element_by_xpath("//*[@id='content']/div/form/input[3]").click()
        time.sleep(10)
        elem = driver.find_element_by_xpath("//*[@id='content']/p/a[1]").click()
        time.sleep(10)
        elem = driver.find_element_by_xpath("//*[@id='main']/div[2]/a[2]").click()
        time.sleep(10)
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys(3)
        time.sleep(10)
        elem = driver.find_element_by_xpath("//*[@id='content']/div/form/input[3]").click()
        time.sleep(10)
        elem = driver.find_element_by_link_text("Checkout").click()
        time.sleep(10)
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("vaishnavi")
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys("valipe")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("vvalipe@unomaha.edu")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("omaha")
        elem = driver.find_element_by_id("id_postal_code")
        elem.send_keys("68132")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("omaha")
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='content']/form/p[7]/input").click()
        time.sleep(10)
    def tearDown(self):
        self.driver.close()
