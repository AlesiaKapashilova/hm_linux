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
