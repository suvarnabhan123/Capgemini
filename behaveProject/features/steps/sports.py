from behave import *
from selenium import webdriver


@given(u'user should able to launch chrome browser')
def launch_browser(context):
    path = r"C:\Users\SNEHA\PycharmProjects\behaveProject\drivers\chromedriver.exe"
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.get("https://in.bookmyshow.com/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)





@then(u'user should select the location')
def bengaluru(context):
    context.driver.find_element("xpath", "//input[@type='text']").send_keys("bengaluru")


# @then(u'user see the sports present in that perticular place')
# def
@when(u'user should click on the location')
def click_bengaluru(context):
    context.driver.find_element("xpath", "//strong[.='Bengaluru']").click()


@then(u'user should able to click on  sports page')
def click_sports(context):
    context.driver.find_element("link text", "Sports").click()
    context.driver.refresh()



@then(u'user should click on dreamhack')
def dreamhack(context):
    context.driver.find_element("xpath", "//div[.='DreamHack Hyderabad 2022']").click()


@then(u'user should click on book')
def click_book(context):
    context.driver.find_element("id", "synopsis-book-button").click()


@then(u'user should select the time')
def select_time(context):
    context.driver.find_element("xpath", '//li[@data-id="time-pill"]').click()


@then(u'user should click on continue')
def click_continue(context):
    context.driver.find_element("xpath", "//button[.='Continue']").click()


@then(u'user should click on add')
def click_add(context):
    context.driver.find_element("xpath", "//div[.='P1 - Gaming Enthusiast']/../..//div[.='Add']").click()


@then(u'user should click on proceed')
def click_proceed(context):
    context.driver.find_element("xpath", "//button[.='Proceed']").click()


@when(u'user enter name"{name}" into name textfield')
def enter_name(context, name):
    context.driver.find_element("xpath", '//input[@type="text"]').send_keys(name)


@then(u'user enter mobileno {number} into mobile number textfield')
def enter_mobileno(context, number):
    if isinstance(number, float):
        number = str(int(number))
    context.driver.find_element("xpath", '//input[@type="number"]').send_keys(number)


@then(u'user enter the email "{email}" into email textfiled')
def enter_emai(context, email):
    context.driver.find_element("xpath", '//input[@type="email"]').send_keys(email)


@then(u'user enter the age {age} into age textfield')
def enter_age(context, age):
    if isinstance(age, float):
        age = str(int(age))
    context.driver.find_element("name", "age").send_keys(age)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


@then(u'user should able to click on checkbox')
def click_checkbox(context):
    context.driver.find_element("xpath", '//input[@type="checkbox"]').click()


@then(u'user should able to click on submit button')
def click_submit(context):
    context.driver.find_element("id", "registration-submit-button").click()
    # context.driver.implicitly_wait(10)
    # context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


@then(u'user should able to click on proceed to pay')
def click_proceedtopay(context):
    context.driver.find_element("xpath", "//button[.='Login to Proceed']").click()


@then(u'user should able to enter {number}')
def enter_number(context, number):
    if isinstance(number, float):
        number = str(int(number))
    context.driver.find_element("id", "mobileNo").send_keys(number)


@then(u'user should able to click on continue button')
def click_continuebutton(context):
    context.driver.find_element("xpath", "//button[.='Continue']").click()
    context.driver.close()
