Feature: sports


  Background:User should able to book a sports
    Given user should able to launch chrome browser
    Then user should select the location
    When user should click on the location
    Then user should able to click on  sports page
    And user should click on dreamhack
    Then user should click on book
    Then user should select the time
    And user should click on continue
    Then user should click on add
    Then user should click on proceed


  Scenario Outline:
    When user enter name"<name>" into name textfield
    Then user enter mobileno "<mobileno>" into mobile number textfield
    Then user enter the email "<email>" into email textfiled
    And user enter the age "<age>" into age textfield
    Then user should able to click on checkbox
    Then user should able to click on submit button
    And user should able to click on proceed to pay
    Then user should able to enter "<mobileno>"
    And user should able to click on continue button

    Examples:

                | name    |  | mobileno   |  | email                     |  | age |
                | suvarna |  |9353781139 |  | suvarnabhandari@gmail.com |  | 22  |
                |123456   |  |9900346785  |  |ambika123                  |   |25   |
                |anu      |  |9113676419  |   |anuj@gmail.com            |   |20  |
                |shree    |  |9986451950  |   |appu@gmail.com            |    |15 |
                |sri      |  |98765432    |   |sri8765@gmail.com         |    |22 |
                |shivu    |  |9353781139  |   |suvarnabhandari@gmail.com |    |abc|






