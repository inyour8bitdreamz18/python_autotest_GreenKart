# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
from user import User

class test_register_new_user(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_register_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.open_login_page(wd)
        self.click_on_register_button(wd)
        self.open_registration_page(wd)
        self.fill_user_info(wd, User(firstname="Anna", lastname="Lazopulo", email="qa.anna.lazopulo@gmail.com",
                                telephone="+123545789", fax="+148234578", company="Learning Automation",
                                address1="str.Learn, 21", address2="str. Quality Assurance, 12",
                                city="London", zone_id="Cheshire", postcode="1234567", country_id="United Kingdom",
                                loginname="admin.anna", password="admin"))

        # open the page 'Successful Registration'
        wd.get("https://automationteststore.com/index.php?rt=account/success")

        # click to confirm registration info
        wd.find_element(By.LINK_TEXT,"Continue").click()
        wd.get("https://automationteststore.com/index.php?rt=account/account")

        # click to log out
        wd.find_element(By.XPATH,"//a[contains(@href, 'https://automationteststore.com/index.php?rt=account/logout')]").click()
        #wd.get("https://automationteststore.com/index.php?rt=account/logout")

        # click to continue using the site
        wd.find_element(By.LINK_TEXT,"Continue").click()

        self.open_home_page(wd)

    def click_on_register_button(self, wd):
        wd.find_element(By.LINK_TEXT, "Login or register").click()

    def fill_user_info(self, wd, user):
        # fill user's first name
        wd.find_element(By.ID, "AccountFrm_firstname").click()
        wd.find_element(By.ID, "AccountFrm_firstname").clear()
        wd.find_element(By.ID, "AccountFrm_firstname").send_keys(user.firstname)
        # fill user's last name
        wd.find_element(By.ID, "AccountFrm_lastname").click()
        wd.find_element(By.ID, "AccountFrm_lastname").clear()
        wd.find_element(By.ID, "AccountFrm_lastname").send_keys(user.lastname)
        # fill user's email
        wd.find_element(By.ID, "AccountFrm_email").click()
        wd.find_element(By.ID, "AccountFrm_email").clear()
        wd.find_element(By.ID, "AccountFrm_email").send_keys(user.email)
        # fill user's telephone
        wd.find_element(By.ID, "AccountFrm_telephone").click()
        wd.find_element(By.ID, "AccountFrm_telephone").clear()
        wd.find_element(By.ID, "AccountFrm_telephone").send_keys(user.telephone)
        # fill user's fax
        wd.find_element(By.ID, "AccountFrm_fax").click()
        wd.find_element(By.ID, "AccountFrm_fax").clear()
        wd.find_element(By.ID, "AccountFrm_fax").send_keys(user.fax)
        # fill user's company name
        wd.find_element(By.ID, "AccountFrm_company").click()
        wd.find_element(By.ID, "AccountFrm_company").clear()
        wd.find_element(By.ID, "AccountFrm_company").send_keys(user.company)
        # fill user's address 1
        wd.find_element(By.ID, "AccountFrm_address_1").click()
        wd.find_element(By.ID, "AccountFrm_address_1").clear()
        wd.find_element(By.ID, "AccountFrm_address_1").send_keys(user.address1)
        # fill user's address 2
        wd.find_element(By.ID, "AccountFrm_address_2").click()
        wd.find_element(By.ID, "AccountFrm_address_2").clear()
        wd.find_element(By.ID, "AccountFrm_address_2").send_keys(user.address2)
        # fill user's city
        wd.find_element(By.ID, "AccountFrm_city").clear()
        wd.find_element(By.ID, "AccountFrm_city").send_keys(user.city)
        # select user's zone id
        wd.find_element(By.ID, "AccountFrm_zone_id").click()
        Select(wd.find_element(By.ID, "AccountFrm_zone_id")).select_by_visible_text(user.zone_id)
        # fill user's postcode (ZIP code)
        wd.find_element(By.ID, "AccountFrm_postcode").click()
        wd.find_element(By.ID, "AccountFrm_postcode").clear()
        wd.find_element(By.ID, "AccountFrm_postcode").send_keys(user.postcode)
        # select user's country
        wd.find_element(By.ID, "AccountFrm_country_id").click()
        Select(wd.find_element(By.ID, "AccountFrm_country_id")).select_by_visible_text(user.country_id)
        # fill user's login name
        wd.find_element(By.ID, "AccountFrm_loginname").clear()
        wd.find_element(By.ID, "AccountFrm_loginname").send_keys(user.loginname)
        wd.find_element(By.XPATH, "//form[@id='AccountFrm']/div[3]/fieldset").click()
        # fill user's login password
        wd.find_element(By.ID, "AccountFrm_password").click()
        wd.find_element(By.ID, "AccountFrm_password").clear()
        wd.find_element(By.ID, "AccountFrm_password").send_keys(user.password)
        # confirm user's login password
        wd.find_element(By.ID, "AccountFrm_confirm").clear()
        wd.find_element(By.ID, "AccountFrm_confirm").send_keys(user.password)
        # subscribe for newsletter ("AccountFrm_newsletter1" is Yes; "AccountFrm_newsletter0" is No)
        wd.find_element(By.ID, "AccountFrm_newsletter1").click()
        # click to agree to the Privacy Policy
        wd.find_element(By.ID, "AccountFrm_agree").click()
        # submit the registration info
        wd.find_element(By.XPATH, "//button[@type='submit']").click()

    def open_registration_page(self, wd):
        wd.get("https://automationteststore.com/index.php?rt=account/create")

    def open_login_page(self, wd):
        wd.get("https://automationteststore.com/index.php?rt=account/login")

    def open_home_page(self, wd):
        wd.get("https://automationteststore.com/")
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
