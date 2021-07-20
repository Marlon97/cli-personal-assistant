from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def send_hours(driver):
    try:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Click Here to submit those hours."))
        )
        print(driver.find_element(By.LINK_TEXT, "Click Here to submit those hours.").text)
        #Descomentar línea de código para ejecutar el bot correctamente
        #driver.find_element(By.LINK_TEXT, "Click Here to submit those hours.").click()
        return True
    except:
        return False


def register_hours(driver):
    try:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, ".ng-scope > .tasksid > .ng-binding"))
        )
        driver.find_element(By.CSS_SELECTOR, ".ng-scope > .hours:nth-child(4) > .ng-binding").click()
        driver.find_element(By.CSS_SELECTOR, ".ng-scope > .hours:nth-child(4) > .hours-inner > input").send_keys("8")
        for i in range(5, 9):
            el = driver.find_element(By.CSS_SELECTOR, f".ng-scope > .hours:nth-child({i}) > .hours-inner > input")
            el.click()
            el.send_keys("8")
        driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(4)").click()
        return True
    except:
        return False


def bigtime_login(user, password, driver):
    try:
        driver.get("https://intuit.bigtime.net/Bigtime/myaccount/session/login")
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.ID, "SUserName"))
        )
        userLabel = driver.find_element(By.ID, "SUserName")
        userLabel.click()
        userLabel.send_keys(user)
        passLabel = driver.find_element(By.ID, "SPassword")
        passLabel.click()
        passLabel.send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".btn").click()
        return True
    except:
        return False


def weekly_check_hours(user, password, webDriverPath):
    with webdriver.Chrome(webDriverPath) as driver:
        if bigtime_login(user, password, driver):
            if register_hours(driver):
                return send_hours(driver)
    return False
