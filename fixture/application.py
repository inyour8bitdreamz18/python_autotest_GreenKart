from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def continue_to_use_site(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Continue").click()

    def confirm_registration_info(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Continue").click()
        wd.get("https://automationteststore.com/index.php?rt=account/account")

    def open_success_registration_page(self):
        wd = self.wd
        wd.get("https://automationteststore.com/index.php?rt=account/success")

    def click_on_register_button(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Login or register").click()

    def fill_user_info(self, user):
        wd = self.wd
        self.open_home_page()
        self.open_login_page()
        self.click_on_register_button()
        self.open_registration_page()
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

    def open_registration_page(self):
        wd = self.wd
        wd.get("https://automationteststore.com/index.php?rt=account/create")

    def open_login_page(self):
        wd = self.wd
        wd.get("https://automationteststore.com/index.php?rt=account/login")

    def open_user_page(self):
        wd = self.wd
        wd.get("https://automationteststore.com/index.php?rt=account/account")

    def open_home_page(self):
        wd = self.wd
        wd.get("https://automationteststore.com/")

    def open_logout_page(self):
        wd = self.wd
        wd.get("https://automationteststore.com/index.php?rt=account/logout")

    def add_product(self):
        # Temporary add first product on main page
        wd = self.wd
        wd.find_element(By.XPATH, "//div[@id='block_frame_featured_1769']/div/div/div[2]/div[3]/a/i").click()

    def open_cart(self):
        wd = self.wd
        wd.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Check Your Order'])[1]/following::span[2]").click()

    def destroy(self):
        self.wd.quit()