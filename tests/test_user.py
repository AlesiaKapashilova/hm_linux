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
