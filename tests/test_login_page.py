import allure

from Sprint6_Webinar_Practicum.data import MestoAuthData
from Sprint6_Webinar_Practicum.data import Urls
from Sprint6_Webinar_Practicum.pages.login_page import LoginPage


class TestLoginPage:

    @allure.title("Проверка авторизации")
    @allure.description("Авторизуемся под тестовым пользователем и проверяем что авторизовались под ним")
    def test_success_authorization(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.MESTO)

        login_page.set_email_input(MestoAuthData.LOGIN)
        login_page.set_password_input(MestoAuthData.PASSWORD)
        main_page = login_page.click_auth_button()

        assert main_page.get_current_user() == MestoAuthData.LOGIN
