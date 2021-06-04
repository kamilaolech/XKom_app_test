from Locators.Locators import Locators

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProfilePage():

    def __init__(self, driver):
        self.driver = driver
        self.icons_class_name = Locators.icons_class_name
        self.textInputWindows_class_name = Locators.textInputWindows_class_name
        self.loginButton_id = Locators.loginButton_id
        self.logoutButton_id = Locators.logoutButton_id
        self.logoutConfirm1_id = Locators.logoutConfirm1_id
        self.logoutConfirm2_id = Locators.logoutConfirm2_id

    def click_profile(self):
        (self.driver.find_elements_by_class_name(self.icons_class_name))[-1].click()

    def enter_email(self, email):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, self.loginButton_id)))
        (self.driver.find_elements_by_class_name(self.textInputWindows_class_name))[0].clear()
        (self.driver.find_elements_by_class_name(self.textInputWindows_class_name))[0].send_keys(email)

    def enter_password(self, password):
        (self.driver.find_elements_by_class_name(self.textInputWindows_class_name))[1].clear()
        (self.driver.find_elements_by_class_name(self.textInputWindows_class_name))[1].send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.loginButton_id).click()

    def logout(self):
        self.driver.find_element_by_id(self.logoutButton_id).click()
        self.driver.find_element_by_id(self.logoutConfirm1_id).click()
        self.driver.find_element_by_id(self.logoutConfirm2_id).click()


