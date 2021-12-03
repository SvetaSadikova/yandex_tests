from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class YandexPage(object):
    def __init__(self, d):
        self.url = "https://ya.ru/"
        self.my_driver = d

    def open(self):
        self.my_driver.get(self.url)

    def quit(self):
        self.my_driver.quit()

    def input(self):
        return self.my_driver.find_element(By.ID, 'text')

    def page_content(self):
        return self.my_driver.page_source

    def search(self, text_value: str):
        self.input().clear()
        self.input().send_keys(text_value)
        self.input().send_keys(Keys.RETURN)

    def wait_result(self):
        self.my_driver.implicitly_wait(5)

