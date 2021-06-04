from Locators.Locators import Locators


class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.icons_class_name = Locators.icons_class_name
        self.searchWindow_xpath = Locators.searchWindow_xpath
        self.searchedProduct_id = Locators.searchedProduct_id

    def click_profile(self):
        (self.driver.find_elements_by_class_name(self.icons_class_name))[-1].click()

    def search_product(self, productsItem):
        search = self.driver.find_element_by_xpath(self.searchWindow_xpath)
        search.click()
        search.send_keys(productsItem)
        self.driver.find_element_by_id(self.searchedProduct_id).click()
        self.driver.implicitly_wait(10)

    def go_to_cart(self):
        image = self.driver.find_elements_by_class_name(self.icons_class_name)
        image[-2].click()
        self.driver.implicitly_wait(10)



