import time

from selenium.webdriver.common.by import By


def test_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    assert browser.find_element(By.CSS_SELECTOR, '#ad_to_basket_form > button')