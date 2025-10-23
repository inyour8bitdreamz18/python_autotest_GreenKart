# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from user import User

class test_login(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def login(self, wd, user):
        wd.get("https://automationteststore.com/")
        wd.find_element(By.XPATH, "//img[@alt='Automation Test Store']").click()
        wd.find_element(By.ID, "customernav").click()
        wd.find_element(By.LINK_TEXT, "Login or register").click()
        # Input login name
        wd.find_element(By.ID, "loginFrm_loginname").clear()
        wd.find_element(By.ID, "loginFrm_loginname").send_keys(user.loginname)
        # Input login password
        wd.find_element(By.ID, "loginFrm_password").clear()
        wd.find_element(By.ID, "loginFrm_password").send_keys(user.password)
        #
        wd.find_element(By.XPATH,"//form[@id='loginFrm']/fieldset/div").click()
        wd.find_element(By.XPATH,"//form[@id='loginFrm']/fieldset/button/i").click()

        #wd.find_element(By.LINK_TEXT,"Not Anna? Logoff").click()

    def test_login(self):
        wd = self.wd
        self.login(wd, User(loginname="admin.anna", password="admin"))

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
