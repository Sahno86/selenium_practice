import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
options.add_argument('--headless')


driver = webdriver.Chrome(service=service, options=options)


driver.get("https://info-hit.ru")

favorites = driver.find_element("xpath", "//a[@href='/catalog/favorites/']")
favorites.click()
# time.sleep(2)

logo = driver.find_element("xpath", "//a[contains(@class, 'header__nav__logo-name')]")
logo.click()
assert driver.title == "Агрегатор онлайн-курсов ИнфоХит — маркетплейс обучающих дистанционных программ", 'Заголовок неверен'
# time.sleep(3)