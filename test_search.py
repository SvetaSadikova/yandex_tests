from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from search_page import YandexPage

m_driver = webdriver.Chrome(ChromeDriverManager().install())
ya_page = YandexPage(m_driver)
ya_page.open()
ya_page.search("Python")
# ya_page.wait_result()
assert "Python" in ya_page.page_content()
ya_page.quit()
