from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\under\Desktop\geckodriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/emailsignup/')
        time.sleep(1)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.likePhotos('hashtag')
    
    def likePhotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
        time.sleep(5)
        #for i in range(1,3):
         #   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          #  time.sleep(3)
        hrefs = driver.find_elements_by_tag_name('a')
        picHrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in picHrefs if hashtag in href]
        print(hashtag + ' fotos: ' + str(len(picHrefs)))

        for picHref in picHrefs:
            driver.get(picHref)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                curtir = driver.find_elements_by_xpath("//button[@class='wpO6b  ']")
                curtir[1].click()
                time.sleep(19)
            except Exception as e:
                time.sleep(5)

loginBot = InstagramBot('user','password')
loginBot.login()