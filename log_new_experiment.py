from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def log_new_experiment(username, password):

        # Connect:
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        browser = webdriver.Firefox(firefox_profile=profile, executable_path='/home/clcarver/geckodriver')
        browser.get('https://cmsdb.darkcosmos.org/experiments/run/new')

        # Login
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[5]/main/div/div[1]/div/div[3]/button'))).click()
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#username"))).send_keys(username)
        browser.find_element_by_css_selector("input#password").send_keys(password)
        login_attempt = browser.find_element_by_css_selector("div.v-btn__content>i.v-icon.pr-1.mdi.mdi-lock-open-outline.theme--light").click()


        # Log new experiment:

        # Page 1
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#title"))).send_keys('Reference IVP Curve - 30 steps') # Title
        browser.find_element_by_css_selector("input#desc").send_keys('30 step IVP curve for performance tests') # Details
        time.sleep(2)

        # Number of Groups:
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[12]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/form/div[4]/div/div/div[2]/div[1]/div[1]/input'))).click() # Open first drop down
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div/div/div[1]/a/div/div'))).click() # Click group 1

        # Experiment Type:
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[21]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/form/div[5]/div/div/div[2]/div[1]/div[1]/input'))).click()
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[9]/div/div/div[2]/a/div/div'))).click()

        # LED:



        # Page 2

if __name__ == '__main__':
    log_new_experiment('bletson', 'baseball2046')
