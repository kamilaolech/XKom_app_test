import unittest
from ddt import ddt, data, unpack

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Pages.ProfilePage import ProfilePage
from Locators.Locators import Locators
from Tests.BaseTest import BaseTest
from TestUtils.XLUtils import get_data

file_path = "Data/data_login_positive.csv"

# Test - przypadek pozytywny logowania do konta XKom

@ddt
class TestLogin_positive(BaseTest):

    @data(*get_data(file_path))
    @unpack
    def testLogin(self, email, password):

        driver = self.driver

        # sprawdzenie czy aplikacja jest zainstalowana
        driver.is_app_installed('pl.xkom_2021-04-07.apk')
        # logowanie ze strony home
        profile = ProfilePage(driver)
        profile.click_profile()
        profile.enter_email(email)
        profile.enter_password(password)
        profile.click_login()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, Locators.logoutButton_id)))
        # sprawdzenie czy uzytkownik jest zalogowany
        self.assertTrue(self.driver.find_element_by_id(Locators.logoutButton_id).is_displayed())
        # wylogowanie uzytkownika
        profile.logout()

if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin_positive)
    unittest.TextTestRunner(verbosity=2).run(suite)
