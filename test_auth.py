import pytest
from selenium import webdriver

def test_auth_by_phone_number():
    # Настройки браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless") # Отключение режима headless для визуального тестирования

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Шаг 1: Открытие страницы авторизации
    driver.get("https://lk.rt.ru/")
    assert "Личный кабинет Ростелеком" in driver.title

    # Шаг 2: Выбор авторизации по номеру телефона
    phone_tab = driver.find_element_by_xpath("//div[@class='login__tabs']/a[1]")
    phone_tab.click()

    # Шаг 3: Ввод номера телефона и пароля
    phone_input = driver.find_element_by_name("phone")
    password_input = driver.find_element_by_name("password")
    login_button = driver.find_element_by_xpath("//button[text()='Войти']")

    phone_input.send_keys("1234567890")
    password_input.send_keys("password")
    login_button.click()

    # Шаг 4: Проверка успешной авторизации и переход на страницу профиля
    assert "https://lk.rt.ru/profile/" in driver.current_url

    driver.quit()

def test_auth_by_email():
    # Настройки браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless") # Отключение режима headless для визуального тестирования

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Шаг 1: Открытие страницы авторизации
    driver.get("https://lk.rt.ru/")
    assert "Личный кабинет Ростелеком" in driver.title

    # Шаг 2: Выбор авторизации по почте
    email_tab = driver.find_element_by_xpath("//div[@class='login__tabs']/a[2]")
    email_tab.click()

    # Шаг 3: Ввод почты и пароля
    email_input = driver.find_element_by_name("email")
    password_input = driver.find_element_by_name("password")
    login_button = driver.find_element_by_xpath("//button[text()='Войти']")

    email_input.send_keys("test@example.com")
    password_input.send_keys("password")
    login_button.click()

    # Шаг 4: Проверка успешной авторизации и переход на страницу профиля
    assert "https://lk.rt.ru/profile/" in driver.current_url

    driver.quit()

def test_auth_by_login():
    # Настройки браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless") # Отключение режима headless для визуального тестирования

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Шаг 1: Открытие страницы авторизации
    driver.get("https://lk.rt.ru/")
    assert "Личный кабинет Ростелеком" in driver.title

    # Шаг 2: Выбор авторизации по логину
    login_tab = driver.find_element_by_xpath("//div[@class='login__tabs']/a[3]")
    login_tab.click()

    # Шаг 3: Ввод логина и пароля
    login_input = driver.find_element_by_name("login")
    password_input = driver.find_element_by_name("password")
    login_button = driver.find_element_by_xpath("//button[text()='Войти']")

    login_input.send_keys("testuser")
    password_input.send_keys("password")
    login_button.click()

    # Шаг 4: Проверка успешной авторизации и переход на страницу профиля
    assert "https://lk.rt.ru/profile/" in driver.current_url

    driver.quit()

def test_auth_by_account():
    # Настройки браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless") # Отключение режима headless для визуального тестирования

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Шаг 1: Открытие страницы авторизации
    driver.get("https://lk.rt.ru/")
    assert "Личный кабинет Ростелеком" in driver.title

    # Шаг 2: Выбор авторизации по лицевому счету
    account_tab = driver.find_element_by_xpath("//div[@class='login__tabs']/a[4]")
    account_tab.click()

    # Шаг 3: Ввод лицевого счета и пароля
    account_input = driver.find_element_by_name("account")
    password_input = driver.find_element_by_name("password")
    login_button = driver.find_element_by_xpath("//button[text()='Войти']")

    account_input.send_keys("12345")
    password_input.send_keys("password")
    login_button.click()

    # Шаг 4: Проверка успешной авторизации и переход на страницу профиля
    assert "https://lk.rt.ru/profile/" in driver.current_url

    driver.quit()

@pytest.mark.parametrize("product, auth_type", [("ЕЛК Web", "phone"), ("ЕЛК Web", "email"), ("Онлайм Web", "phone"), ("Старт Web", "phone"), ("Старт Web", "email"), ("Умный дом Web", "phone"), ("Умный дом Web", "ls"), ("Ключ Web", "phone"), ("Ключ Web", "email")])
def test_auth_by_product_and_type(product, auth_type):
    # Настройки браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless") # Отключение режима headless для визуального тестирования

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Выбор нужного продукта и типа авторизации
    if product == "ЕЛК Web":
        url = "https://lk.rt.ru/"
        if auth_type == "phone":
            tab_number = 1
            phone_value = "1234567890"
            password_value = "password"
        elif auth_type == "email":
            tab_number = 2
            email_value = "test@example.com"
            password_value = "password"
        elif auth_type == "ls":
            tab_number = 4
            ls_value = "12345"
            password_value = "password"
    elif product == "Онлайм Web":
        url = "https://my.rt.ru/"
        if auth_type == "phone":
            tab_number = 1
            phone_value = "1234567890"
            password_value = "password"
        elif auth_type == "email":
            tab_number = 2
            email_value = "test@example.com"
            password_value = "password"
    elif product == "Старт Web":
        url = "https://start.rt.ru/"
        if auth_type == "phone":
            tab_number = 1
            phone_value = "1234567890"
            password_value = "password"
        elif auth_type == "email":
            tab_number = 2
            email_value = "test@example.com"
            password_value = "password"
    elif product == "Умный дом Web":
        url = "https://lk.smarthome.rt.ru/"
        if auth_type == "phone":
            tab_number = 1
            phone_value = "1234567890"
            password_value = "password"
        elif auth_type == "ls":
            tab_number = 4
            ls_value = "12345"
            password_value = "password"
    elif product == "Ключ Web":
        url = "https://key.rt.ru/"
        if auth_type == "phone":
            tab_number = 1
            phone_value = "1234567890"
            password_value = "password"
        elif auth_type == "email":
            tab_number = 2
            email_value = "test@example.com"
            password_value = "password"
    
    # Шаг 1: Открытие страницы авторизации выбранного продукта
    driver.get(url)
    assert "Ростелеком" in driver.title

    # Шаг 2: Выбор нужного типа авторизации
    auth_tab = driver.find_element_by_xpath(f"//div[@class='login__tabs']/a[{tab_number}]")
    auth_tab.click()

    # Шаг 3: Ввод логина и пароля в соответствии с выбранным типом авторизации
    if auth_type == "phone":
        phone_input = driver.find_element_by_name("phone")
        password_input = driver.find_element_by_name("password")
        login_button = driver.find_element_by_xpath("//button[text()='Войти']")

        phone_input.send_keys(phone_value)
        password_input.send_keys(password_value)
        login_button.click()

    elif auth_type == "email":
        email_input = driver.find_element_by_name("email")
        password_input = driver.find_element_by_name("password")
        login_button = driver.find_element_by_xpath("//button[text()='Войти']")

        email_input.send_keys(email_value)
        password_input.send_keys(password_value)
        login_button.click()

    elif auth_type == "ls":
        ls_input = driver.find_element_by_name("account")
        password_input = driver.find_element_by_name("password")
        login_button = driver.find_element_by_xpath("//button[text()='Войти']")

        ls_input.send_keys(ls_value)
        password_input.send_keys(password_value)
        login_button.click()

    # Шаг 4: Проверка успешной авторизации и переход на страницу профиля
    assert "https://lk.rt.ru/profile/" in driver.current_url

    driver.quit()
