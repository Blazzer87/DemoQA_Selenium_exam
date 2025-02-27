from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Настройки Chrome
chrome_options = Options()
chrome_options.page_load_strategy = 'eager'

with webdriver.Chrome(options=chrome_options) as driver:
    driver.get("https://demoqa.com/progress-bar")

    # Локаторы
    p_bar = (By.XPATH, "//div[@role='progressbar']")
    btn = (By.XPATH, "//button[@id='startStopButton']")

    wait = WebDriverWait(driver, 10)

    # Кликаем кнопку Start
    wait.until(EC.element_to_be_clickable(btn)).click()
    print("Прогресс-бар запущен")

    # Ожидание, пока прогресс достигнет 1% или 2%
    def progress_reached_target(driver, target_value):
        progress_element = driver.find_element(*p_bar)
        value = progress_element.get_attribute("aria-valuenow")  # Получаем значение
        if value is None:
            print("Атрибут aria-valuenow еще не обновился, ждем...")
            return False  # Ждем, пока атрибут появится
        value = int(value)  # Преобразуем в число
        print(f"Текущий прогресс: {value}%")  # Для отладки
        if value >= target_value:  # Когда прогресс достигает или превышает целевое значение
            # Нажимаем кнопку Stop
            stop_button = driver.find_element(*btn)
            stop_button.click()
            print(f"Прогресс-бар остановлен на {value}%")
            return True  # Завершаем ожидание
        return False  # Продолжаем ждать

    # Уменьшаем время ожидания между проверками
    while not progress_reached_target(driver, 1):  # Проверка на target_value
        time.sleep(0.01)  # Уменьшаем задержку до 100 миллисекунд



    time.sleep(3)  # Ожидание для наглядности
 😁