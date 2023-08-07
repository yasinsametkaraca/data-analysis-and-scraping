from html.parser import HTMLParser  # HTMLParser is a built-in class
from urllib import parse  # parse is a built-in module


# It scrapes the html codes sent to it. returns links in the html code.
# LinkFinder Class: It will find the links in the HTML file. It will parse the HTML file and find the links. It will return the links it finds.
class LinkFinder(HTMLParser):  # LinkFinder class inherits from HTMLParser class. We use HTMLParser class to parse HTML files.

    def __init__(self, base_url, page_url):  # base_url: the url of the website we are crawling, page_url: the url of the page we are crawling. We will use these variables to create absolute links.
        super().__init__()  # We call the constructor of the parent class. HTMLParser class has a constructor. We call it. We don't need to write it again.
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()  # We will store the links we find in this set. We don't want duplicate links. So we use set.

    def handle_starttag(self, tag: str, attrs):  # This method is called when an opening tag is encountered. We override it.
        if tag == 'a':
            for (attribute, value) in attrs:  # attrs is a list of tuples. Each tuple contains an attribute and its value. For example: [('href', 'https://www.kidega.com/'), ('class', 'logo')]
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)  # We create an absolute link. We use parse.urljoin() method to create an absolute link. kidega.com and /tutunamayanlar are given as parameters. It returns https://www.kidega.com/tutunamayanlar
                    self.links.add(url)  # We add the link to the set.

    def page_links(self):  # This method returns the links we found.
        return self.links

    def error(self, message):  # This method is called when an error occurs. We override it.
        pass
