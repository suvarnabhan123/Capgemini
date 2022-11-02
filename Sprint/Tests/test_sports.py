import re
import pytest
from POM.sports import BookSport
from library.excel_lib import ReadExcel
from library.config import Configuration


class TestBookSport:
    read_excel = ReadExcel()
    data = read_excel.read_testdata(Configuration.DATA_SHEET)

    @pytest.mark.parametrize("location, name, mobileno, email,age, number", data)
    def test_book(self, init_driver, location, name, mobileno, email, age, number):
        driver = init_driver
        bs = BookSport(driver)
        bs.bengaluru(location)
        bs.click_bengaluru()
        bs.click_sports()
        bs.click_dreamhack()
        bs.click_book()
        bs.select_time()
        bs.click_continue()
        bs.click_add()
        bs.click_proceed()
        bs.enter_name(name)
        bs.enter_mobileno(mobileno)
        bs.enter_email(email)
        bs.enter_age(age)
        bs.click_checkbox()
        bs.click_submit()
        bs.click_proceedtopay()
        bs.enter_number(number)
        bs.click_continuebutton()


