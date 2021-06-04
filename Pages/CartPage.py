from Locators.Locators import Locators


class CartPage():

    def __init__(self, driver):
        self.driver = driver
        self.totalProductsCost_id = Locators.totalProductsCost_id

    def check_sum(self):    #sprawdzenie sumy cen produktow w koszyku
        self.value = self.driver.find_element_by_id(self.totalProductsCost_id).get_attribute('text')
        return (self.value)





