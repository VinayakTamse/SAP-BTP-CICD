from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utility.Utils import wait_for
import time

def test_execute_grid():

    hub_url = "http://localhost:4444"
    chrome_options = Options()
    chrome_options.set_capability('browserVersion', '128.0.6613.119')
    chrome_options.set_capability('platformName', 'LINUX')
    #options.add_argument('--headless')
    driver = webdriver.Remote(command_executor=hub_url, options=chrome_options)
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(60)
    user = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    wait_for(driver, user)
    user.send_keys('Admin')
    print('Entered User Name')
    password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    wait_for(driver, password)
    password.send_keys("admin123")
    print('Entered Password')
    submit = driver.find_element(By.CSS_SELECTOR, "button.orangehrm-login-button")
    wait_for(driver, submit)
    submit.click()
    print('Clicked on Submit Button')
    time.sleep(5)
    print('User is on Home Page of Orange HRM')
    print('Test Ended')

