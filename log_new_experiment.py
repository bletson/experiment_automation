from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def connect_login(username, password, path_to_driver):
        '''
        Connects and opens a Firefox browser window and logins into the new experiment page.

        username: str, username to log into the website
        password: str, password to log into the website
        path_to_driver: str, path to directory that holds the geckodriver.exe driver. Can be downloaded here:
        https://github.com/mozilla/geckodriver/releases

        Returns a browser object to use in future automation
        '''
        # Connect
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        browser = webdriver.Firefox(firefox_profile=profile, executable_path=path_to_driver)
        browser.get('https://cmsdb.darkcosmos.org/experiments/run/new')

        # Login
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[5]/main/div/div[1]/div/div[3]/button'))).click()
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#username"))).send_keys(username)
        browser.find_element_by_css_selector("input#password").send_keys(password)
        login_attempt = browser.find_element_by_css_selector("div.v-btn__content>i.v-icon.pr-1.mdi.mdi-lock-open-outline.theme--light").click()
        return browser

def log_page_1(browser, led_list):

        '''
        Function that logs information in the first page of the experiment.

        broswer: selenium driver object, browser object that controls the automation process
        led_list: array of strings, list of length 8 that specifies the LED in each slot. If the slot is empty enter a 'x'. Example: ['AA123', 'CJ03', 'X', 'CJ02', 'CJ01', 'X', 'X', 'X']

        Returns a browser object to use in future tasks
        '''

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
        for led in [x for x in led_list if x.lower() != 'x']: # Remove X's from led_list
            led_loc = browser.find_element_by_xpath("/html/body/div/div[21]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/form/div[6]/div/div/div[2]/div[1]/div[1]/div[1]/input")
            led_loc.send_keys(led)
            led_loc.send_keys(Keys.TAB)
            # browser.find_element_by_xpath('/html').click() # Click off screen to reset dropdown

        # Submit
        browser.find_element_by_css_selector('div.v-stepper__content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()
        print('Page 1: Experiment Complete')
        return browser

def log_page_2(browser, led_list):

        '''
        Function that logs information in the second page of the experiment.

        broswer: selenium driver object, browser object that controls the automation process
        led_list: array of strings, list of length 8 that specifies the LED in each slot. If the slot is empty enter a 'x'. Example: ['AA123', 'CJ03', 'X', 'CJ02', 'CJ01', 'X', 'X', 'X']

        Returns a browser object to use in future tasks
        '''
        # Rack
        # rack_loc = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[33]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div/form/div[1]/div/div/div[2]/div[1]/div[1]/input')))
        rack_loc = '/html/body/div/div[33]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div/form/div[1]/div/div/div[2]/div[1]/div[1]/input'
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, rack_loc))).send_keys('R01')
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[21]/div/div/div[1]/a/div/div'))).click()


        # TEC
        tec_loc = '/html/body/div/div[33]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div/form/div[2]/div/div/div[2]/div[1]/div[1]/input'
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, tec_loc))).send_keys('TEC01')
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[20]/div/div/div[1]/a/div/div'))).click()


        # Holder
        holder_loc = '/html/body/div/div[33]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div/form/div[3]/div/div/div[2]/div[1]/div[1]/input'
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, holder_loc))).send_keys('H01')
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[19]/div/div/div[1]/a/div/div'))).click()


        # Power Supply
        power_supply_loc = '/html/body/div/div[33]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div/form/div[4]/div/div/div[2]/div[1]/div[1]/input'
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, power_supply_loc))).click()
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[18]/div/div/div[2]/a/div/div'))).click()

        # LEDs

        # # Slot dictionary:
        slot_dict = {
        1: ['80', 'LRed'],
        2: ['81', 'LOrange'],
        4: ['82', 'LYellow'],
        5: ['85', 'LGreen'],
        6: ['81', 'LBlue'],
        7: ['81', 'LPink'],
        8: ['81', 'LPurple']
        }

        # led_list_alphabatized = sorted(led_list)
        # for led in led_list_alphabatized:
        #     if led.lower() != 'x':
        #         slot = led_list.index(led) + 1
        #         channel, usb = slot_dict[slot][0], slot_dict[slot][1]
        #         WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[33]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div/form/div[6]/div/div/div[2]/div[1]'))).clear().send_keys(slot)
        #         WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[33]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div/form/div[7]/div/div/div[2]/div[1]'))).clear().send_keys(channel)
        #         WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[33]/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div/form/div[8]/div/div/div[2]/div[1]/div[1]/input'))).send_keys(usb)
        #         browser.send_keys(KEYS.TAB)
        #     else:
        #         continue



if __name__ == '__main__':
    browser = connect_login(<username>, <passowrd>)
    time.sleep(3)
    browser = log_page_1(browser, led_list=['AA123', 'CJ03', 'X', 'CJ02', 'CJ01', 'X', 'X', 'X'])
    time.sleep(3)
    log_page_2(browser, led_list=['AA123', 'CJ03', 'X', 'CJ02', 'CJ01', 'X', 'X', 'X'])
