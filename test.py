import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTest:

    def test_dzen_redirect(self, driver):
        driver.get("https://dzen.ru/")

        time.sleep(5)

        element = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[9]/div/main/section[2]/div/div[1]/div[1]/div/article/div[2]/ul/li[2]/a")

        element.click()

        time.sleep(5)

        WebDriverWait(driver, 10).until(expected_conditions.url_changes())


