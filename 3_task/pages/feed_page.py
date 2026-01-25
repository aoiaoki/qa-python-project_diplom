from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FeedPage(BasePage):
    ORDERS_TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    ORDERS_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList')]")

    def get_total_orders(self) -> int:
        return int(self.find(self.ORDERS_TOTAL).text)

    def get_today_orders(self) -> int:
        return int(self.find(self.ORDERS_TODAY).text)

    def refresh(self):
        self.driver.refresh()

    def has_orders_in_progress(self) -> bool:
        return self.find(self.ORDERS_IN_PROGRESS).is_displayed()
