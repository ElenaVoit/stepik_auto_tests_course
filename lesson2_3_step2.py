from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Функция для вычисления ln(abs(12 * sin(x)))
def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Клик по элементу, вызывающему alert
    button = browser.find_element(By.XPATH, '//button[text()="I want to go on a magical journey!"]')
    button.click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    # Находим элемент, в котором хранится значение x
    x_element = browser.find_element(By.ID, "input_value")
    x_value = int(x_element.text)  # Получаем значение x как целое число

    # Вычисляем результат математической функции
    y = calc(x_value)

    # Находим поле для ввода ответа и вводим туда результат
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(str(y))  # Преобразуем результат в строку

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # Закрываем браузер после всех манипуляций
    browser.quit()
