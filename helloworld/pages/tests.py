from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AddFunctionalityTest(LiveServerTestCase):

    def testAdd(self):
        selenium = webdriver.Chrome()
        selenium.get("http://localhost:8000/")

        task_input = selenium.find_element_by_id('task_name')
        submit = selenium.find_element_by_id('first_submit')

        task_input.send_keys("Selenium Test")

        submit.send_keys(Keys.RETURN)

        assert "Selenium Test" in selenium.page_source