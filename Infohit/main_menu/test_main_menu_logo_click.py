from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
options.add_argument('--headless')

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://info-hit.ru")

favorites = driver.find_element("xpath", "//a[@href='/catalog/favorites/']")
favorites.click()

logo = driver.find_element("xpath", "//a[contains(@class, 'header__nav__logo-name')]")
wait.until(EC.element_to_be_clickable(logo))
logo.click()
assert driver.title == "Агрегатор онлайн-курсов ИнфоХит — маркетплейс обучающих дистанционных программ", 'Заголовок неверен'

print('1 тест выпонен')
