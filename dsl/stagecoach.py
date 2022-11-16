import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
url = 'https://www.stagecoachbus.com/'
from_ = "//*[@id = 'from']"
to_ = "//*[@id = 'to']"
plan_journey = "//*[@id = 'plan-journey']"


def florida():
    driver.get(url)
    uu = driver.find_element(By.XPATH, from_)
    click_on_element(uu)
    uu.send_keys('Bedworth, Warwickshire')
    us = driver.find_element(By.XPATH, to_)
    click_on_element(us)
    us.send_keys('Nuneaton, Warwickshire')
    us.send_keys(Keys.ENTER)
    dd = driver.find_element(By.XPATH, plan_journey)
    click_on_element(dd)
    time.sleep(10)


def click_on_element(element):
    element_is_clickable = False
    while element_is_clickable:
        try:
            element.click()
            element_is_clickable = True
        except ElementClickInterceptedException:
            continue


if __name__ == '__main__':
    florida()
