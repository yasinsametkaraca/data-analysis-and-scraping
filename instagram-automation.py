from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys


def saveFollowers(followers):
    with open("followers.txt", "w", encoding="UTF-8") as file:
        for follower in followers:
            file.write(follower + "\n")


class Instagram:
    chrome_driver_path = r"C:\Users\YSK\Documents\Drivers\chromedriver.exe"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = []
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.driver = webdriver.Chrome(Instagram.chrome_driver_path, options=self.browserProfile)

    def signIn(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_element_by_name("password").send_keys(Keys.ENTER)
        time.sleep(4)

        if self.driver.find_element_by_class_name("_ac8f"):
            self.driver.find_element_by_class_name("_ac8f").click()
            time.sleep(4)

        button = self.driver.find_element_by_class_name("_a9-z")
        button.find_elements_by_tag_name('button')[1].click()

    def getFollowers(self, username, max_count=100):
        self.driver.get("https://www.instagram.com/" + username + "/followers/")
        time.sleep(6)

        followers = self.driver.find_elements_by_class_name("x1dm5mii")
        count = len(followers)

        action = webdriver.ActionChains(self.driver)

        while count < max_count:
            followers[0].click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            followers = self.driver.find_elements_by_class_name("x1dm5mii")
            new_count = len(followers)

            if count != new_count:
                count = new_count
                time.sleep(1)
            else:
                break

        for follower in followers:
            link = follower.find_element_by_tag_name('a').get_attribute('href')
            self.followers.append(link)

        saveFollowers(self.followers)

    def followUser(self, username):
        self.driver.get("https://www.instagram.com/" + username)
        time.sleep(3)
        button = self.driver.find_element_by_tag_name("button")

        if button.text == "Follow" or button.text == "Follow Back":
            button.click()
            time.sleep(2)
        else:
            print("You are already following this user.")

    def followUsers(self, users):
        for user in users:
            self.followUser(user)
            time.sleep(2)

    def unfollowUser(self, username):
        self.driver.get("https://www.instagram.com/" + username)
        time.sleep(3)
        button = self.driver.find_element_by_tag_name("button")

        if button.text == "Following":
            self.driver.find_element_by_tag_name("button").click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="mount_0_0_/v"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]').click()
            time.sleep(2)
        else:
            print("You are not following this user.")

    def unfollowUsers(self, users):
        for user in users:
            self.unfollowUser(user)
            time.sleep(2)

    def __del__(self):
        time.sleep(7)
        self.driver.close()


instagram = Instagram("Username", "Password")

instagram.signIn()
instagram.getFollowers("next.jsx", 10)
# instagram.followUser("next.jsx")
# instagram.followUsers(["next.js", "next.jsx"])
# instagram.unfollowUser("next.jsx")

