from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERTS_CONTENT), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERTS_CONTENT), \
            "Success message is presented, but should not be"

