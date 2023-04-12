from selenium import webdriver
from userinfo import username, password
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from django.db import models
# from ..account.models import User
from django.contrib.auth import get_user_model
import DJANGO_SETTINGS_MODULE=mysite.setti

User = get_user_model()


sjsj = ''
class Instagram:
    driver_path = "/Users/qehreman/Desktop/driver/chromedriver"
    
    # driver_path = "C:\Driver\chromedriver"
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(Instagram.driver_path)
        self.browser.maximize_window() # For maximizing window
        self.browser.implicitly_wait(20) # gives an implicit wait for 20 seconds
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(10)
        usernameInput = self.browser.find_element("name",'username')
        passwordInput = self.browser.find_element("name",'password')
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)
        if self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'):
            self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
            # el.find_element(By.TAG_NAME,'button').click()
            print('asasfsdffasfadfsads')
        print('sdsadafsadsfsadf--------')
        time.sleep(10)

        if self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'):
            self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(10)
        print('23123213122321321')
        # usernameChan = self.browser.find_element(By.CSS_SELECTOR,"h2._aacl._aacs._aact._aacx._aada").text
        # details = self.browser.find_elements(By.CSS_SELECTOR, "span._ac2a._ac2b")
        # numb_of_post = details[0].text
        # followers = details[1].text
        # followings = details[2].text
        # print(usernameChan,numb_of_post,followers,followings)
        if self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/span/span'):
            usernames = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/a/h2').text
            posts = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/span/span').text
            followers = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a').text
            following = self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a').text
            print(username,posts,followers,following)
            user = User.objects.filter(username=usernames)
            if user:
                user.username=usernames,
                user.post=posts,
                user.follower=followers,
                user.following=following,
                user.update()
            else:
                User.objects.create(username=usernames,post=posts, follower=followers, following=following)


    def followUser(self, username):
        pass
    def unFollowUser(self, username):
        pass
    def __del__(self):
        time.sleep(10)
        # self.browser.close()
app = Instagram(username, password)
app.signIn()
app.getFollowers()
print(sjsj)