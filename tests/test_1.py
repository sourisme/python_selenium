"""Basic test"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://testqastudio.me/'

def test_1(browser):
    """SMK-1. Smoke test"""
    
    browser.get(url=URL)
    
    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="post-11328"]')
    element.click()
    sku = browser.find_element(by=By.CSS_SELECTOR, value='[class="sku"]')
    
    assert sku.text == '4XAVRC34', 'Unexpected sku for "Градвис Керамическая ваза"'

def test_2(browser):
    """SMK-2. Smoke test"""
    
    browser.get(url=URL)
    
    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="tab-best_sellers"]')
    element.click()
    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="post-11341"]')
    element.click()
    sku = browser.find_element(by=By.CSS_SELECTOR, value='[class="sku"]')
    
    assert sku.text == 'C0MSSDSUM7', 'Unexpected sku for "ДИВВИНА Журнальный столик"'
