from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MainPage(BasePage):
    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
    FEED_TAB = (By.XPATH, "//a[contains(@href,'/feed')]")

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

    def open_constructor(self):
        self.click(self.CONSTRUCTOR_TAB)

    def open_feed(self):
        self.click(self.FEED_TAB)

    def scroll_to_sauces(self):
        tab = self.wait.until(EC.element_to_be_clickable(self.SAUCES_TAB))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", tab
        )
        tab.click()

    def open_ingredient_modal(self):
        ingredient = self.wait.until(
            EC.element_to_be_clickable(self.INGREDIENT)
        )
        ingredient.click()
        self.wait.until(EC.visibility_of_element_located(self.MODAL))

    def close_ingredient_modal(self):
        self.click(self.MODAL_CLOSE_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(self.MODAL))

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

    def constructor_has_items(self) -> bool:
        return len(self.driver.find_elements(*self.CONSTRUCTOR_ITEMS)) > 0

    def wait_modal_closed(self):
        self.wait.until(EC.invisibility_of_element_located(self.MODAL))
