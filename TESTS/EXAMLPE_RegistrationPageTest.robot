*** Settings ***
Documentation     RegistrationPage (Registration with correct data)
Library           ../Libraries/Base_methods.py
Library           ../Libraries/Driver.py
Library           ../Pages/RegistrationPage.py
Suite Setup     Create web driver
Suite Teardown  Close browser

*** Variables ***
${URL}            some_url
${profile_url}    some_url

*** Test Cases ***
Test Registration Page
    [Tags]    RegistrationPage (Registration with correct data)
    go to url           ${URL}
    registration to site
    verify message
    get url
    verify page
    go to url           ${profile_url}
    verify user
*** Keywords ***
Close browser
    close driver
Create web driver
    open browser        gc

