from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def adding_to_cart_check(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE).text
        assert product_name == added_product_name, "Product not match"

    def cart_total_check(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total_price = self.browser.find_element(*ProductPageLocators.CART_TOTAL).text
        assert product_price == total_price, "Total not match"
