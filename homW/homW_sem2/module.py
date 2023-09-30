"""
Задание
Условие: Добавить в задание с REST API ещё один тест,
в котором создаётся новый пост, а потом проверяется его наличие на сервере по полю «описание».
Подсказка: создание поста выполняется запросом к
https://test-stand.gb.ru/api/posts с передачей параметров title, description, content.

Что ещё можно почитать:
• Описание Wikipedia API
• Пример использования zeep
"""
import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


class Site:
    def __init__(self, address):
        if browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            # service = Service(testdata["driver_path"])
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata["sleep_time"])

    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def find_element_wait_located(self, mode, path):
        wait = WebDriverWait(self.driver, 10)
        if mode == "css":
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, path)))
        elif mode == "xpath":
            element = wait.until(EC.presence_of_element_located((By.XPATH, path)))
        else:
            element = None
        return element

    def find_element_wait_clickable(self, mode, path):
        wait = WebDriverWait(self.driver, 10)
        if mode == "css":
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, path)))
        elif mode == "xpath":
            element = wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close_dr(self):
        self.driver.quit()