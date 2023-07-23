from selenium import webdriver
import time
import selenium
from selenium.common.exceptions import StaleElementReferenceException


class Github:
    chrome_driver_path = r"C:\Users\YSK\Documents\Drivers\chromedriver.exe"

    def __init__(self, username, password):
        self.browser = webdriver.Chrome(Github.chrome_driver_path)
        self.baseUrl = "https://github.com/"
        self.username = username
        self.password = password
        self.followers = []

    def findRepositories(self, repository_name):
        self.browser.get(self.baseUrl + "search?q=" + repository_name + "&type=repositories")
        time.sleep(2)
        repositories = self.browser.find_elements_by_css_selector(".hKtuLA")
        for repository in repositories:
            text = repository.find_elements_by_tag_name("h3")[0].text
            link = repository.find_elements_by_tag_name("a")[0].get_attribute("href")
            repos = {
                "text": text,
                "link": link
            }
            print(repos)

    def signIn(self):
        self.browser.get(self.baseUrl + "login")
        self.browser.find_element_by_id("login_field").send_keys(self.username)
        self.browser.find_element_by_id("password").send_keys(self.password)
        self.browser.find_element_by_name("commit").click()

    def loadFollowers(self):
        while True:
            try:
                followers_elements = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
                for follower_element in followers_elements:
                    div_elements = follower_element.find_elements_by_tag_name("div")
                    if len(div_elements) > 1:
                        follower_username = div_elements[1].find_elements_by_tag_name("span")[1].text
                        link = follower_element.find_elements_by_tag_name("a")[0].get_attribute("href")
                        followers_data = {
                            "username": follower_username,
                            "link": link
                        }
                        self.followers.append(followers_data)
            except StaleElementReferenceException:
                self.browser.refresh()
                continue
            else:
                break

    def getFollowers(self, username):
        self.browser.get(self.baseUrl + username + "?tab=followers")
        self.loadFollowers()
        time.sleep(2)

        while True:
            try:
                pagination_element = self.browser.find_element_by_class_name("pagination")
                links = pagination_element.find_elements_by_tag_name("a")
                if len(links) == 1:
                    if links[0].text == "Next":
                        links[0].click()
                        self.loadFollowers()
                    else:
                        break
                else:
                    for link in links:
                        if link.text == "Next":
                            link.click()
                            self.loadFollowers()
                        else:
                            continue
            except selenium.common.exceptions.NoSuchElementException:
                break

    def __del__(self):
        time.sleep(5)
        self.browser.close()  # Close the browser when the object is destroyed


app = Github("yasin", "Password")
app.signIn()
app.findRepositories("python")
app.getFollowers("yasinsametkaraca")
print(app.followers)
print(len(app.followers))
