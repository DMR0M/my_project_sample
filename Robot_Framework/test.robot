*** Settings ***
Documentation   Test Website
Library         SeleniumLibrary
Library         OperatingSystem

*** Variables ***
${browser}      Chrome
${url}          https://www.google.com/


*** Keywords ***
Open Google
    Open Browser     ${url}     ${browser}
    Maximize Browser Window
    Close Browser


*** Test Cases ***
Test Open Google
    Open Google