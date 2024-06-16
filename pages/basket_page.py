from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def goods_should_not_to_be_presented(self) -> bool:
        assert self.is_not_element_present(*BasketPageLocators.GOODS), "Goods are added"

    def should_be_empty_basket_alert(self) -> bool:
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_CONTENT), "Basket is not empty"
