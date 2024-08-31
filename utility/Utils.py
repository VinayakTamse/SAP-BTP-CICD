from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def wait_for(driver, element):
    wait_ele = WebDriverWait(driver=driver, timeout=45)
    wait_ele.until(ec.element_to_be_clickable(element))