from selenium import webdriver
from src.browsers.browsers import select_browser

class textbox_validation:
    def textbox_test(self):
        driver = select_browser().browser_options('chrome');
        driver.get("https://demoqa.com/")
        driver.maximize_window()
        
        print("textbox test case")