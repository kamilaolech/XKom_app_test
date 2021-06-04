import unittest
import os
from appium import webdriver


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseTest(unittest.TestCase):

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


