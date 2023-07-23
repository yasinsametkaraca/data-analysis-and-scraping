from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\YSK\Documents\Drivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = "https://www.python.org"
driver.get(url)

# driver.maximize_window()
# driver.save_screenshot("python_org.png")
print(driver.title)  # Welcome to Python.org
driver.get(url + "/about")
driver.back()  # Go back to the previous page

introduction = driver.find_element_by_xpath('//*[@id="touchnav-wrapper"]/header/div/div[3]/p')
blog_times = driver.find_elements_by_css_selector(".blog-widget time")  # Returns a list of elements. Time is a tag name
blog_names = driver.find_elements_by_css_selector(".blog-widget li a")

blogs = {}  # a dictionary
for i in range(len(blog_times)):
    blogs[i] = {"time": blog_times[i].text, "name": blog_names[i].text}

print(blogs)
print(blogs[0]["time"])
print(introduction.text)

click_upcoming_events = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')
click_upcoming_events.click()


search_bar = driver.find_element_by_xpath('//*[@id="id-search-field"]')
search_bar.send_keys("decorator")
search_bar.send_keys(Keys.ENTER)
time.sleep(3)

driver.close()


