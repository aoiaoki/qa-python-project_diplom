import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Ожидание видимости элемента {locator}")
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента {locator}")
    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        element = self.find_clickable(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Проверка наличия элемента {locator}")
    def is_visible(self, locator) -> bool:
        try:
            self.find(locator)
            return True
        except Exception:
            return False

    @allure.step("Ожидание исчезновения элемента {locator}")
    def wait_until_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Получение списка элементов {locator}")
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Обновление страницы")
    def refresh(self):
        self.driver.refresh()
