from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
#загружаем страницу
browser.get('https://ok.ru/')

def auth():
    # заполняем поле логин, привязываемся к элементу через его имя
    username=browser.find_element(by=By.ID, value='field_email')
    username.send_keys('89011408799')

    # заполняем поле пароля, привязываемся к элементу через его id
    password=browser.find_element(by=By.ID, value='field_password')
    password.send_keys('omamorer13')
    password.send_keys(Keys.ENTER)
    auth_check()

def auth_check():
    try:
        # Проверка что на странице присутствует полное имя пользователя
        assert "Марина Омельченко" in browser.page_source
        print('The test was completed successfully')
    except Exception as err:\
        print('The test was failled')
    # Закрываем браузер
    browser.close()


def music():
    auth()
    input_music = browser.find_element(by=By.CSS_SELECTOR, value='input[placeholder="Искать на сайте"]')
    input_music.send_keys('Николай Басков')
    input_music.send_keys(Keys.ENTER)
    music_check()

def music_check():
    try:
        # Проверка что на странице присутствует полное имя пользователя
        assert "Фантазёр" in browser.page_source
        print('The test was completed successfully')
    except Exception as err:
        print('The test was failled')
        # Закрываем браузер
        browser.close()

def language():
    auth()
    profile = browser.find_element(by=By.XPATH, value="//div[@class='ucard-mini_cnt']")
    profile.click()
    browser.implicitly_wait(10)
    language_button = browser.find_element(by=By.XPATH, value="//ul[@class='u-menu']/li[@class='u-menu_li'][2]/a[@class='u-menu_a']/div[@class='tico']/span[@class='u-menu_tx ellip-i lp']")
    language_button.click()
    browser.implicitly_wait(10)
    link_language1 = browser.find_element(by=By.XPATH, value="//form/div[@class='sel-lang_list']/a[@class='sel-lang_i o'][1]")
    link_language1.click()
    browser.implicitly_wait(10)
    language_chek()

def language_chek():
    try:
        # Проверка что язык изменен
        assert "OK" in browser.title
        print('The test was completed successfully')
    except Exception as err:
        print('The test was failled')
        # Закрываем браузер
        browser.close()
language()