from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class Attendance:
    table_headers = ".report-header-truncate"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def get_table_headers(self):
        print(self.table_headers)


