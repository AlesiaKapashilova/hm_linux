<<<<<<< HEAD
import pytest
import allure

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


@pytest.fixture(scope='class')
def get_user():
    return User(name="Vasya", age=39)


class TestForPytest:
    def test_example(self):
        with allure.step('Бла блабла'):
            self.test_name()
            self.test_age()

            

    @allure.feature('я имя')
    def test_name(self, get_user):
        assert get_user.name == "Vasya"

    @allure.story('я типо возраст')
    def test_age(self, get_user):
        assert get_user.age == 39
=======
@pytest.mark.sanity
class TestExampleTest:

    def test_example(self):
        with allure.step('Do Login'):
            (LoginPage()
             .go_to_login_page()
             .insert_user_name()
             .insert_password())


class LoginPage:

    def go_to_login_page(self):
        Report.report_step('go to login page')
        return self

    def insert_user_name(self):
        Report.report_step('insert username')
        return self

    def insert_password(self):
        Report.report_step('insert password')
        return self
>>>>>>> 963ed7278bbbfa0f188c91030d64dec289a68ad9
