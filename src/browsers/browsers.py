from selenium import webdriver
import os


class select_browser:
    def browser_options(self, browser):
        driver = None
        if browser == "chrome":
            ChromeDriverPath = os.getcwd() + "\\drivers\\chromedriver.exe"
            driver = webdriver.Chrome(ChromeDriverPath)

        return driver
