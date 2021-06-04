import unittest
from time import sleep
from ddt import ddt, data, unpack

from TestUtils.XLUtils import get_data
from Pages.HomePage import HomePage
from Tests.BaseTest import BaseTest
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage

file_path = "Data/data_price_sum.csv"

# Test - poprawnosc sumowania cen w koszyku przy dwoch produktach

@ddt
class TestPriceSum_positive(BaseTest):

    @data(*get_data(file_path))
    @unpack
    def testPrice_1(self, product1, product2):

        products = [product1, product2]

        driver = self.driver
        home = HomePage(driver)
        product = ProductPage(driver)
        cart = CartPage(driver)

        # sprawdzenie czy aplikacja jest zainstalowana
        driver.is_app_installed('pl.xkom_2021-04-07.apk')

        totalPrice = 0
        for item in range(len(products)):

            # wyszukanie produktu
            home.search_product(products[item])

            # zczytanie ceny i otworzenie strony produktu
            price = product.check_product_price()
            priceFloat = float(price[0:-10]+price[-9:-6]+'.'+price[-4:-3])
            totalPrice += priceFloat
            product.open_product_page()
            sleep(2)
            # dodanie produktu do koszyka
            product.add_product_to_cart()
            # powrot do home
            product.back_home()
            sleep(2)

        # przejscie do koszyka ze strony glownej
        home.go_to_cart()

        # zaczytanie sumy zamowienia i porownanie ceny w koszyku z suma cen zczytanych z kart produktow
        finalPrice = cart.check_sum()
        final = float(finalPrice[0:-10] + finalPrice[-9:-6] + '.' + finalPrice[-4:-3])
        self.assertEqual(totalPrice, final)
        sleep(2)


if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPriceSum_positive)
    unittest.TextTestRunner(verbosity=2).run(suite)
