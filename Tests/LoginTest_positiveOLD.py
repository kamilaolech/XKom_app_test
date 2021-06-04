import unittest
import os

from appium import webdriver
from time import sleep

from Pages.ProfilePage import ProfilePage
from Locators.Locators import Locators

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# Test - przypadek pozytywny logowania do konta XKom

email = 'testanitalis@gmail.com'
password = 'XKomincorrect'

class TestLogin_positive(unittest.TestCase):

    def setUp(self):        #  https://appium.io/docs/en/writing-running-appium/caps/
        desired_caps = {}
        desired_caps['app'] = PATH('pl.xkom_2021-04-07.apk')
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Genymotion Cloud'
        desired_caps['udid'] = 'localhost:10000'  # do uzupelnia gdyby nie byl staly (wynik adb devices)
        desired_caps['appPackage'] = 'pl.xkom'                  #  w konsoli po wlaszeniu aplikacji na komorce z wyniku: adb shell dumpsys window | grep -E 'mCurrentFocus'
        desired_caps['appActivity'] = 'pl.xkom.ui.MainActivity'
        #desired_caps['clearDeviceLogsOnStart'] = 'true'
        #desired_caps['noReset'] = 'false'

        # polaczenie z Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def testLogin(self):

        driver = self.driver

        # sprawdzenie czy aplikacja jest zainstalowana
        driver.is_app_installed('pl.xkom_2021-04-07.apk')

        # logowanie ze strony home
        profile = ProfilePage(driver)
        profile.click_profile()
        profile.enter_email(email)
        profile.enter_password(password)
        profile.click_login()
        # sprawdzenie czy uzytkownik jest zalogowany
        self.assertTrue(self.driver.find_element_by_id(Locators.logoutButton_id).is_displayed())
        sleep(2)

        # wylogowanie uzytkownika
        profile.logout()

if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin_positive)
    unittest.TextTestRunner(verbosity=2).run(suite)
