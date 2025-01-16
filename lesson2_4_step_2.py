import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Локатор элемента с ценой
    price_locator = (By.ID, "price")  # ID элемента с ценой

    # Ожидаем, пока текст элемента с ценой не станет равным "$100"
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element(price_locator, "$100")
    )

    # Находим и кликаем кнопку "Book", проверяем доступность кнопки
    button_book = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button_book.click()

    # Находим элемент, в котором хранится значение x
    x_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "input_value"))
    )

    # Получаем текст из элемента и пытаемся преобразовать его в целое число
    x_value = int(x_element.text)

    # Вычисляем результат математической функции
    y = calc(x_value)

    # Находим поле для ввода ответа и вводим туда результат
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(str(y))  # Преобразуем результат в строку

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()

    # Ждем немного, чтобы результат появился
    time.sleep(5)

finally:
    # Закрываем браузер после всех манипуляций
    browser.quit()
