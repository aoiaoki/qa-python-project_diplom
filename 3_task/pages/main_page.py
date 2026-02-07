import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MainPage(BasePage):

    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
    FEED_TAB = (By.XPATH, "//a[contains(@href,'/feed')]")

    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")

    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    INGREDIENT_NAME = "Соус Spicy-X"
    INGREDIENT = (By.XPATH, f"//p[text()='{INGREDIENT_NAME}']")

    CONSTRUCTOR_SECTION = (
        By.XPATH,
        "//section[contains(@class,'BurgerConstructor')]"
    )

    CONSTRUCTOR_ITEMS = (
        By.XPATH,
        "//section[contains(@class,'BurgerConstructor')]//li"
    )

    MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Modal_modal__close')]"
    )

    @allure.step("Открыть конструктор")
    def open_constructor(self):
        self.click(self.CONSTRUCTOR_TAB)

    @allure.step("Открыть ленту заказов")
    def open_feed(self):
        self.click(self.FEED_TAB)

    @allure.step("Проверить, что конструктор открыт")
    def is_constructor_opened(self) -> bool:
        return len(self.driver.find_elements(*self.CONSTRUCTOR_HEADER)) > 0

    @allure.step("Проверить, что лента заказов открыта")
    def is_feed_opened(self) -> bool:
        return len(self.driver.find_elements(*self.FEED_HEADER)) > 0

    @allure.step("Открыть модальное окно ингредиента")
    def open_ingredient_modal(self):
        self.wait.until(
            EC.element_to_be_clickable(self.INGREDIENT)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.MODAL)
        )

    @allure.step("Проверить, что модальное окно ингредиента открыто")
    def is_ingredient_modal_opened(self) -> bool:
        elements = self.driver.find_elements(*self.MODAL)
        return len(elements) > 0 and elements[0].is_displayed()

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click(self.MODAL_CLOSE_BUTTON)

    @allure.step("Дождаться закрытия модального окна")
    def wait_modal_closed(self):
        self.wait.until(
            EC.invisibility_of_element_located(self.MODAL)
        )

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        ingredient = self.wait.until(
            EC.presence_of_element_located(self.INGREDIENT)
        )
        target = self.wait.until(
            EC.presence_of_element_located(self.CONSTRUCTOR_SECTION)
        )

        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', { dataTransfer }));
            target.dispatchEvent(new DragEvent('dragover', { dataTransfer }));
            target.dispatchEvent(new DragEvent('drop', { dataTransfer }));
            source.dispatchEvent(new DragEvent('dragend', { dataTransfer }));
            """,
            ingredient,
            target
        )

    @allure.step("Проверить, что в конструкторе есть ингредиенты")
    def constructor_has_items(self) -> bool:
        return len(self.driver.find_elements(*self.CONSTRUCTOR_ITEMS)) > 0
