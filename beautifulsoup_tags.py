from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = fp.read()

obj = BeautifulSoup(soup, 'html.parser')

print(obj.prettify())  # print the html in a readable format
print(obj.title)  # print the title tag
print(obj.title.name)  # print the name of the title tag
print(obj.h1)  # print the h1 tag
print(obj.h1.string)  # print the string inside the h1 tag

