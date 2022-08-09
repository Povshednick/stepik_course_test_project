from .base_page import BasePage
from .locators import CartPageLocators

class BasketPage(BasePage):
    def should_not_be_product_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT_IN_CART), "There is product in cart"

    def should_be_emrty_cart_text(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART), "Cart is not empty"
