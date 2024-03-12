from telnetlib import EC

from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

from pageobjects.search import SearchPageObject


class DashboardPageObject(PageObject):
    def init_page_elements(self):
        self.acceptCookiesSel = Button(By.ID, 'onetrust-accept-btn-handler')
        self.searchProductSel = InputText(By.ID, 'search-input')
        self.unico = InputText(By.CSS_SELECTOR, 'input[aria-label="Caja de búsqueda"]')

    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get(self.config.get('Test', 'urlCarrefour'))
        return self

    def clickAccept(self):
        self.logger.debug("accept")
        self.acceptCookiesSel.wait_until_visible(6).click()
        return self

    def clickSearch(self):
        self.logger.debug("click search")
        self.searchProductSel.wait_until_visible(6).click()
        return SearchPageObject(self.driver_wrapper)