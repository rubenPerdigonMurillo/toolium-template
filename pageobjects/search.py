import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

class SearchPageObject(PageObject):
    def init_page_elements(self):
        self.searchProductSel = InputText(By.CSS_SELECTOR, 'input[aria-label="Caja de búsqueda"]')
        self.priceSel = Link(By.CSS_SELECTOR, 'section > ul > li.ebx-sort-list__item.ebx-sort-list__item--priceAsc')
        self.searchButtonSel = Button(By.CSS_SELECTOR, '#empathy-x > header > div.ebx-search-box > button.ebx-event-button.ebx-search-button.ebx-search-box__search-button')


    def searchProduct(self, text):
        self.logger.debug("search product")
        self.searchProductSel.wait_until_visible(6).text = text
        self.searchButtonSel.wait_until_clickable(6).click()
        return self

    def clickPrice(self):
        self.logger.debug("click price")
        self.priceSel.wait_until_clickable(6).click()
        return self