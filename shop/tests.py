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
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"

        driver.get("http://127.0.0.1:8000/admin/orders/order/add/")
        time.sleep(5)
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
        elem = driver.find_element_by_xpath("//*[@id='order_form']/div/div[2]/input[1]").click()
        time.sleep(5)
        assert "Posted Blog Entry"
    def tearDown(self):
        self.driver.close()
