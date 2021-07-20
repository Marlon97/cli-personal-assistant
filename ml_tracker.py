from selenium import webdriver
import operator


bool_operators = {
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
    "==": operator.eq
}


def get_item_price(url, webDriverPath):
    with webdriver.Chrome(webDriverPath) as driver:
        driver.get(url)
        price = float(driver.find_element_by_css_selector('meta[itemprop="price"]').get_attribute('content'))
        driver.close()
        return price


def price_tracker(url, condition, amount, webDriverPath):
    current_price = get_item_price(url, webDriverPath)
    if bool_operators[condition](current_price, amount):
        return True, "Tu producto acaba de cumplir tu condición de precio!", f"Hola, tu producto {url} acaba de cumplir de cumplir tu condición de búsqueda {current_price} {condition} {amount}"
    return False
