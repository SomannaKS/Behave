from behave import *
from selenium import webdriver

@given('launch chrome driver')
def launchBrowser(context):
    #context.driver = webdriver.Chrome(executable_path = "C:\Driver\chromedriver.exe")
    context.driver = webdriver.Chrome()

@when('open facebook home page')
def openPage(context):
    context.driver.get("https://www.facebook.com/")

@then('verify the logo presence')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[1]/div/img').is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()
