import unittest
import os
from ddt import ddt, data, unpack

from Pages.ProfilePage import ProfilePage
from Locators.Locators import Locators
from Tests.BaseTest import BaseTest
from TestUtils.XLUtils import get_data

file_path = "Data/data_login_negative.csv"

# Test - przypadek negatywny logowania do konta XKom

@ddt
class TestLogin_negative(BaseTest):

    @data(*get_data(file_path))
    @unpack
    def testLogin(self, email, password, expectedResult):

        driver = self.driver

        # sprawdzenie czy aplikacja jest zainstalowana
        driver.is_app_installed('pl.xkom_2021-04-07.apk')
        # logowanie ze strony home
        profile = ProfilePage(driver)
        profile.click_profile()
        profile.enter_email(email)
        profile.enter_password(password)
        profile.click_login()
        # sprawdzenie bledu
        notices = self.driver.find_elements_by_class_name(Locators.errorNotices_class_name)
        all_notices = []
        for el in notices:
            all_notices.append(el.get_attribute('text'))
        self.assertIn(expectedResult, all_notices)
        print(all_notices)

if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin_negative)
    unittest.TextTestRunner(verbosity=2).run(suite)
