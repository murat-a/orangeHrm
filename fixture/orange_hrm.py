from fixture.step import StepHelper


class OrangeHrm:

    username_field = 'input[id="txtUsername"]'
    password_field = 'input[id="txtPassword"]'
    login_button = 'button[type="submit"]'
    header = 'li[data-tooltip="Employee Management"] div'
    username_error_message = 'span[id="txtUsername-error"]'
    password_error_message = 'span[id="txtPassword-error"]'

    def __init__(self, app):
        self.app = app
        self.step: StepHelper = self.app.step
        self.wd = self.app.wd

    def openUrl(self, url):
        self.wd.get(url)

    def set_username(self, username):
        self.step.input_text(self.username_field, username)

    def set_password(self, password):
        self.step.input_text(self.password_field, password)

    def click_login_button(self):
        self.step.click_on_element(self.login_button)

    def login_to_the_application(self, username='Admin', password='qTJn5@5APu'):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

    def get_username_error(self):
        return self.step.get_element_text(self.username_error_message)

    def get_password_error(self):
        return self.step.get_element_text(self.password_error_message)

    def get_header_text(self):
        return self.step.get_element_text(self.header)