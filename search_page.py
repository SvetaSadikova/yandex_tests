from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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
        wait = WebDriverWait(self.my_driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'search-result')))

