from .base_page import BasePage
from .locators import ProductPageLocators


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

    def should_item_name_correct(self):
        alerts_content = self.browser.find_elements(*ProductPageLocators.ALERTS_CONTENT)[0]
        good_name = self.browser.find_elements(*ProductPageLocators.GOOD_NAME)[0]
        assert alerts_content.text == good_name.text, "В корзину добавлен не тот файл"


