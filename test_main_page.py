from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_open_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(3)
    page = LoginPage(browser, link)
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()
