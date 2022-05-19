import pickle
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(
        "/home/alesya/PycharmProjects/pythonProject4/Lessons/mypytest/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def login_fixture(driver):
    driver.get(url)

    login = driver.find_element(by=By.ID, value="email")
    login.send_keys("alesia_94@bk.ru")

    password = driver.find_element(by=By.ID, value="passwd")
    password.send_keys("Qwe123456!")

    button = driver.find_element(by=By.ID, value="SubmitLogin")
    button.click()

    pickle.dump(driver.get_cookies(), open('session', 'wb'))
    yield driver


def test_cookie(login_fixture):
    driver = login_fixture

    for cookie in pickle.load(open('session', 'rb')):
        driver.add_cookie(cookie)

        driver.get(url)
        name_user = driver.find_element(by=By.XPATH, value='//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span').text
        assert name_user == "Alesia Kapashilova"


def test_del_cookie(login_fixture):
    driver = login_fixture

    for cookie in pickle.load(open('session', 'rb')):
        driver.add_cookie(cookie)

        driver.delete_all_cookies()
        driver.refresh()
        button = driver.find_element(by=By.ID, value="SubmitLogin")
        assert button.text == "Sign in"
