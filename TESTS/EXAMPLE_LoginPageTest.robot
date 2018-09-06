*** Settings ***
Documentation     LoginPage (Login with correct data)
Library           ../Libraries/Base_methods.py
Library           ../Libraries/Driver.py
Library           ../Pages/LoginPage.py
Suite Setup     Create web driver
Suite Teardown  Close browser

*** Variables ***
${URL}            some_url
${profile_url}    some_url



*** Test Cases ***
Test Login Page
    [Tags]    LoginPage (Login with correct data)
    go to url           ${URL}
    login to site
    get url
    verify page
    go to url           ${profile_url}
    verify user


*** Keywords ***
Close browser
    close driver

Create web driver
    open browser        ph

