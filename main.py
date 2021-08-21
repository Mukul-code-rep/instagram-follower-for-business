from selenium import webdriver
import os
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException

USERNAME = os.environ.get('username')
PASSWORD = os.environ.get('password')
SEARCH = 'dogsphere'


class InstagramFollowerBot:
    def __init__(self):
        chrome_driver = '/Users/mukulperiwal/Downloads/chromedriver'
        self.driver = webdriver.Chrome(executable_path=chrome_driver)

    def login(self):
        self.driver.get('https://www.instagram.com')
        sleep(2)

        enter_username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        enter_username.send_keys(USERNAME)

        enter_password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        enter_password.send_keys(PASSWORD)

        login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        sleep(5)

    def search_for_account(self):
        self.driver.get(f'https://www.instagram.com/{SEARCH}/')
        sleep(2)

    def get_followers_of_an_account(self):
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(2)

    def follow(self):
        follow = self.driver.find_elements_by_css_selector('.jSC57 button.sqdOP')
        for i in range(10):
            try:
                follow[i].click()
            except ElementClickInterceptedException:
                cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel.click()
            finally:
                sleep(2)


bot = InstagramFollowerBot()

bot.login()
bot.search_for_account()
bot.get_followers_of_an_account()
bot.follow()
