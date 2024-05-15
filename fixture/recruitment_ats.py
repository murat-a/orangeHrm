import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

from fixture.table import Table

class RecruitmentATS:
    search_field = "input[data-test='autocompleteSelect']"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def search_candidate_name(self, text):
        self.step.input_text(self.search_field, text)