import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class StageCoach:

    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    url = 'https://www.stagecoachbus.com/'
    xpaths = {'from': "//*[@id = 'from']", 'to': "//*[@id = 'to']", 'plan_journey': "//*[@id = 'plan-journey']"}

    def plan_journey(self):
        self.driver.get(self.url)
        origin = self.driver.find_element(By.XPATH, self.xpaths['from'])
        click_on_element(origin)
        origin.send_keys('Bedworth, Warwickshire')
        destination = self.driver.find_element(By.XPATH, self.xpaths['to'])
        click_on_element(destination)
        destination.send_keys('Nuneaton, Warwickshire')
        destination.send_keys(Keys.ENTER)
        plan_journey_button = self.driver.find_element(By.XPATH, self.xpaths['plan_journey'])
        click_on_element(plan_journey_button)
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
    StageCoach().plan_journey()
