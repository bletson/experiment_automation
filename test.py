from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def connect_login(username, password, path_to_driver):

        # Login:
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        browser = webdriver.Firefox(firefox_profile=profile, executable_path=path_to_driver)
        browser.get('https://cmsdb.darkcosmos.org/experiments/run/new')
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[5]/main/div/div[1]/div/div[3]/button'))).click()
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#username"))).send_keys(username)
        browser.find_element_by_css_selector("input#password").send_keys(password)
        login_attempt = browser.find_element_by_css_selector("div.v-btn__content>i.v-icon.pr-1.mdi.mdi-lock-open-outline.theme--light").click()
        return browser

def log_page_1(browser, led_list):

        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#title"))).send_keys('Reference IVP Curve - 30 steps', Keys.TAB)
        browser.send_keys('30 step IVP curve for performance tests', Keys.TAB)


if __name__ == '__main__':
    browser = connect_login(<username, password>)
    time.sleep(2)
    log_page_1(browser, led_list=None)
