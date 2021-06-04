from Locators.Locators import Locators


class ProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.productPrice_id = Locators.price_id
        self.productPage_id = Locators.product_id
        self.addProduct_accessibilityid = Locators.addToCart_accessibilityid
        self.icons_class_name = Locators.icons_class_name

    def check_product_price(self):   #zczytanie ceny produktu
        self.value = self.driver.find_element_by_id(self.productPrice_id).get_attribute('text')
        return (self.value)

    def open_product_page(self):  #otworzenie strony wyszukanego produktu
        self.driver.find_element_by_id(self.productPage_id).click()

    def add_product_to_cart(self):  # dodanie produkdo koszyka
        self.driver.find_element_by_accessibility_id(self.addProduct_accessibilityid).click()
        self.driver.implicitly_wait(10)

    def back_home(self):   # kliknac wroc i wroc do home
        self.driver.back()
        self.driver.implicitly_wait(10)
        i = self.driver.find_elements_by_class_name(self.icons_class_name)
        i[-5].click()



