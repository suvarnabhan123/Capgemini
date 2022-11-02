import time
import re
from library.excel_lib import ReadExcel
from library.config import Configuration


class BookSport:
    read_xl = ReadExcel()
    book_locators = read_xl.read_locators(Configuration.LOCATORS_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def bengaluru(self, location):
        locator = self.book_locators["enter_bengaluru"]
        self.driver.find_element(*locator).send_keys(location)
        time.sleep(2)

    def click_bengaluru(self):
        locator = self.book_locators["click_bengaluru"]
        self.driver.find_element(*locator).click()

    def click_sports(self):
        locator = self.book_locators["click_sports"]
        self.driver.find_element(*locator).click()
        self.driver.refresh()

    def click_dreamhack(self):
        locator = self.book_locators["click_dreamhack"]
        self.driver.find_element(*locator).click()

    def click_book(self):
        locator = self.book_locators["click_book"]
        self.driver.find_element(*locator).click()

    def select_time(self):
        locator = self.book_locators["select_time"]
        self.driver.find_element(*locator).click()

    def click_continue(self):
        locator = self.book_locators["click_continue"]
        self.driver.find_element(*locator).click()

    def click_add(self):
        locator = self.book_locators["click_add"]
        self.driver.find_element(*locator).click()

    def click_proceed(self):
        locator = self.book_locators["click_proceed"]
        self.driver.find_element(*locator).click()

    def enter_name(self, name):
        locator = self.book_locators["enter_name"]
        self.driver.find_element(*locator).send_keys(name)

    def enter_mobileno(self, mobileno):
        if isinstance(mobileno, float):
            mobileno = str(int(mobileno))
        locator = self.book_locators["enter_no"]
        self.driver.find_element(*locator).send_keys(mobileno)

    def enter_email(self, email):
        locator = self.book_locators["enter_email"]
        self.driver.find_element(*locator).send_keys(email)

    def enter_age(self, age):
        if isinstance(age, float):
            age = str(int(age))
        locator = self.book_locators["enter_age"]
        self.driver.find_element(*locator).send_keys(age)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def click_checkbox(self):
        locator = self.book_locators["click_checkbox"]
        self.driver.find_element(*locator).click()

    def click_submit(self):
        locator = self.book_locators["click_submit"]
        self.driver.find_element(*locator).click()

    def click_proceedtopay(self):
        locator = self.book_locators["click_proceedtopay"]
        self.driver.find_element(*locator).click()

    def enter_number(self, number):
        if isinstance(number, float):
            number = str(int(number))
        locator = self.book_locators["enter_mobileno"]
        self.driver.find_element(*locator).send_keys(number)

    def click_continuebutton(self):
        locator = self.book_locators["click_continuebutton"]
        self.driver.find_element(*locator).click()
