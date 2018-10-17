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

        # Title and details:
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#title"))).send_keys('Reference IVP Curve - 30 steps')
        browser.find_element_by_css_selector("input#desc").send_keys('30 step IVP curve for performance tests')

        # Number of Groups:
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[12]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/form/div[4]/div/div/div[2]/div[1]/div[1]/input'))).click() # Open first drop down
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div/div/div[1]/a/div/div'))).click()

        # Experiment Type:
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[21]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/form/div[5]/div/div/div[2]/div[1]/div[1]/input'))).click()
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[9]/div/div/div[2]/a/div/div'))).click()

        # LEDs
        for led in led_list:
            browser.find_element_by_css_selector("div.v-select__selections:nth-child(2) > input:nth-child(1)").send_keys(led)
            time.sleep(1)
            browser.find_element_by_css_selector("div.v-select__selections:nth-child(2) > input:nth-child(1)").send_keys(Keys.RETURN)
            browser.find_element_by_xpath('/html').click() # Click off screen to reset dropdown

        # Submit
        browser.find_element_by_css_selector('div.v-stepper__content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()
        print('Page 1: Experiment Complete')
        return browser




if __name__ == '__main__':
    browser = connect_login('bletson', 'baseball2046', '/Users/cameron.carverdata/geckodriver.exe')
    time.sleep(2)
    log_page_1(browser, led_list=['AA123', 'CJ03'])
