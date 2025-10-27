from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user):
        wd = self.app.wd
        self.app.open_home_page()
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
        wd.find_element(By.XPATH, "//form[@id='loginFrm']/fieldset/div").click()
        wd.find_element(By.XPATH, "//form[@id='loginFrm']/fieldset/button/i").click()

    def logout(self):
        wd = self.app.wd
        self.app.open_user_page()
        wd.find_element(By.LINK_TEXT, "Logoff").click()
        wd.get("https://automationteststore.com/index.php?rt=account/logout")