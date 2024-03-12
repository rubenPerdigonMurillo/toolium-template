from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

from pageobjects.detailProduct import DetailProductPageObject


class SearchPageObject(PageObject):
    def init_page_elements(self):
        self.searchBox = InputText(By.CSS_SELECTOR, 'input[aria-label="Caja de búsqueda"]')
        self.orderPriceAsc = Link(By.CSS_SELECTOR, 'section > ul > li.ebx-sort-list__item.ebx-sort-list__item--priceAsc')
        self.searchButton = Button(By.CSS_SELECTOR, '#empathy-x > header > div.ebx-search-box > button.ebx-event-button.ebx-search-button.ebx-search-box__search-button')
        self.nameProduct = Link(By.CSS_SELECTOR, '#ebx-grid > article:nth-child(1) > div > div:nth-child(4) > a > h1')
        self.priceProduct = Text(By.CSS_SELECTOR, '#ebx-grid > article:nth-child(1) > div > p > strong')
        self.addProduct = Button(By.CSS_SELECTOR, '#ebx-grid > article:nth-child(1) > div > div:nth-child(6) > section > button')


    def searchProduct(self, text):
        self.logger.debug("search product")
        self.searchBox.wait_until_visible(6).text = text
        self.searchButton.wait_until_clickable(6).click()
        return self

    def clickPrice(self):
        self.logger.debug("click price")
        initial_price = self.priceProduct.wait_until_visible(6).text
        self.orderPriceAsc.wait_until_clickable(6).click()
        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '#ebx-grid > article:nth-child(1) > div > p > strong'), initial_price)
        )
        # WebDriverWait(self.driver, 6).until(
        #     lambda driver: self.priceProduct.text != initial_price
        # )
        return self

    def savePrice(self):
        self.logger.debug(self.priceProduct.wait_until_clickable(6).text)
        self.original_price = self.priceProduct.wait_until_clickable(6).text
        return self.original_price


    def clickAdd(self):
        self.logger.debug("Save price and name")
        self.addProduct.wait_until_visible(6).click()
        return self

    def clickDetail(self):
        self.logger.debug("Save price and name")
        self.nameProduct.wait_until_visible(6).click()
        return DetailProductPageObject(self.driver_wrapper)