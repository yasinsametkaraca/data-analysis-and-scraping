from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = fp.read()

obj = BeautifulSoup(soup, 'html.parser')

# print(obj.prettify())  # print the html in a readable format
print(obj.title)  # print the title tag
print(obj.title.name)  # print the name of the title tag
print(obj.h1)  # print the h1 tag
print(obj.h1.string)  # print the string inside the h1 tag

print(obj.a)  # print the first a tag
print(obj.find_all('p'))  # print all the p tags. Give a list of all the p tags
print(obj.find(id="diva"))  # print the tag with id first.
print(obj.find_all(class_="left"))  # print all the tags with class special

divs = obj.find_all('div')
for div in divs:
    print(div.find_all('a'))  # print all the p tags inside the div tags
    print(div.find_all('a')[0].string)  # print the first p tag inside the div tags
    print(div.find_all('a')[1].string)  # print the second p tag inside the div tags

print(obj.select('#diva'))  # print the tag with id first.
print(obj.select('.left'))  # print all the tags with class special
print(obj.select_one('.left'))  # print the tag with id first.

print(obj.div.attrs)  # print the attributes of the div tag. Return object of type dictionary
print(obj.div.attrs['id'])  # print the id of the div tag
print(obj.get_text(strip=True,
                   separator=','))  # print the text inside the html file. strip=True removes the extra spaces. separator=',' separates the text with comma
print(obj.div.a.get('href'))  # print the href of the a tag inside the div tag
print(obj.div.a['href'])  # print the href of the a tag inside the div tag

print("-------------------")

print(obj.head)  # print the head tag
print(obj.head.contents)  # print the contents of the head tag
print(obj.head.contents[0])  # print the first element of the contents of the head tag
print(obj.body.div.contents)  # print the contents of the div tag inside the body tag
print(obj.body.div.contents[0])  # print the first element of the contents of the div tag inside the body tag

print(obj.body.div.children) # print the children of the div tag inside the body tag. Return object of type list_iterator. We can iterate over it
for child in obj.body.div.children:
    if child != "\n":
        print(child) # print the children of the div tag inside the body tag

for child in obj.body.div.descendants:
    if child != "\n":
        print(child) # print the descendants of the div tag inside the body tag. Descendants = Also return elements inside the children

print(obj.body.div.parent)  # print the parent of the div tag inside the body tag. Return body tag

print(obj.body.h2.text)  # print the text inside the h2 tag inside the body tag

h2 = obj.body.h2  # print the string inside the h2 tag inside the body tag
print(h2.next_sibling)  # print the next sibling of the h2 tag inside the main tag. Return the next tag
print(h2.next_sibling.next_sibling)
print(h2.previous_sibling)  # print the previous sibling of the h2 tag inside the main tag. Return the previous tag
print(h2.find_next_siblings('p')) # print the next siblings of the h2 tag inside the main tag. Return the next tags
print(h2.find_parent('main')) # print the parent of the h2 tag inside the main tag. Return the parent tag
