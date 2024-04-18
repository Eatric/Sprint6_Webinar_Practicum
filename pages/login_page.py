import allure
from selenium.webdriver.common.by import By

from Sprint6_Webinar_Practicum.pages.base_page import BasePage
from Sprint6_Webinar_Practicum.pages.main_page import MainPage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @id='password']")
    SUBMIT = (By.XPATH, "//button[text() = 'Войти']")

    @allure.step('Заполняем поле Email')
    def set_email_input(self, email):
        login_input = self.wait_and_find_element(self.EMAIL_INPUT)
        login_input.send_keys(email)

    @allure.step('Заполняем поле Password')
    def set_password_input(self, password):
        login_input = self.wait_and_find_element(self.PASSWORD_INPUT)
        login_input.send_keys(password)

    @allure.step('Кликаем на кнопку Войти')
    def click_auth_button(self):
        button = self.wait_and_find_element(self.SUBMIT)
        button.click()

        return MainPage(self.driver)
