from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class DetailProductPageObject(PageObject):
    def init_page_elements(self):
        self.priceProductSel = Text(By.CSS_SELECTOR, 'div.buybox__prices')


    def get_Price(self):
        self.logger.debug(self.priceProductSel.text)
        self.actual_price = self.priceProductSel.wait_until_clickable(6).text
        return self.actual_price