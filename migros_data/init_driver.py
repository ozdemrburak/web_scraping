from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def init_driver(url):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    return driver