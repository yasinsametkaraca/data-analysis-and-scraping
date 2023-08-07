from general import *  # to import all functions from general.py file. We will use these functions in this file.
from urllib.request import urlopen  # to open a url
from link_finder import LinkFinder  # to import LinkFinder class from link_finder.py file. We will use this class in this file.


class Spider:  # to create a spider class that will crawl the website. We will create an object from this class. We will use this object to crawl the website. Spider means "Örümcek" in Turkish.
    # Class variables (static variables) are variables that are shared by all objects. We can access class variables with class name or object name. All spider objects will share these variables. Because we don't want another spider to crawl the crawled link again.
    project_name = ''  # project_name: the name of the project. It will be the name of the folder that will contain the queue and crawled files.
    base_url = ''  # base_url: the url of the website we are crawling. For example: https://www.kidega.com or https://www.kidega.com/cok-satanlar
    domain_name = ''  # domain_name: the domain name of the website we are crawling. For example: kidega.com or kidega.com/cok-satanlar
    queue_file = ''  # queue_file: the file that contains the links that are waiting to be crawled.
    crawled_file = ''  # crawled_file: the file that contains the links that are crawled. Crawled links.
    queue = set()  # queue: the set that contains the links that are waiting to be crawled.
    crawled = set()  # crawled: the set that contains the links that are crawled.

    def __init__(self, project_name, base_url,
                 domain_name):  # to initialize the spider object. We will create an object from this class. We will use this object to crawl the website.
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + "/queue.txt"
        Spider.crawled_file = Spider.project_name + "/crawled.txt"
        self.boot()
        self.crawl_page("First spider", Spider.base_url)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod  # to make the function static. We don't need to create an object from this class to run this function.
    def boot():  # to run the boot function when we create an object from this class. We will use this function to create the project folder and files and to update the queue and crawled sets.
        make_directory(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):  # to crawl a page. We will use this function to crawl a page. This function will be called by the threads. Thread_name is the name of the spider that is crawling the page. Page_url is the url of the page that will be crawled.
        if page_url not in Spider.crawled:  # If the page is not crawled yet.
            print(thread_name + " now crawling " + page_url)
            print("Queue " + str(len(Spider.queue)) + " | Crawled  " + str(len(Spider.crawled)))  # to print the number of links in the queue and crawled sets.
            Spider.add_links_to_queue(Spider.gather_links(
                page_url))  # to add the links that are found on the page to the queue set. We call the gather_links() function to find the links on the page. We call the add_links_to_queue() function to add the links in the current page to the queue set.
            Spider.queue.remove(page_url)  # to remove the page_url from the queue set. Because we crawled it.
            Spider.crawled.add(
                page_url)  # to add the page_url to the crawled set. Because we crawled it. We add it to the crawled set after we remove it from the queue set. Because if the program crashes after we remove it from the queue set and before we add it to the crawled set, we will lose the page_url. We will not crawl it again. We will not add it to the crawled set again. Because we check if the page_url is in the crawled set before we crawl it.
            Spider.update_files()  # to update the queue and crawled files.

    @staticmethod
    def gather_links(page_url):  # to gather the links on the page.
        html_string = ''
        try:
            response = urlopen(page_url)  # to open the page_url. But urlopen function read bytes. We need to decode it.
            if 'text/html' in response.getheader('Content-Type'):  # to check if the response is html.
                html_bytes = response.read()  # to read the response.
                html_string = html_bytes.decode("utf-8")  # to decode the response. Convert the response to string. Bytes to string. String: HTML string.
            finder = LinkFinder(Spider.base_url, page_url)  # to create a LinkFinder object. We will use this object to find the links on the page.
            finder.feed(html_string)  # to feed the html_string to the LinkFinder object. Feed function is a function of the LinkFinder class. Actually run the LinkFinder class. The LinkFinder class will call the handle_starttag function. The handle_starttag function will call the add_link function. The add_link function will add the link to the page_links set.
        except Exception as e:
            print(str(e))
            return set()  # to return an empty set. Because we don't want to add the links that are found on the page to the queue set
        return finder.page_links()  # to return the links that are found on the page.

    @staticmethod
    def add_links_to_queue(links):  # Gets the links that are found on the page and add them to the queue set. Saves queue data to project files.
        for link in links:  # to iterate through the links that are found on the page.
            if (link in Spider.queue) or (link in Spider.crawled):  # to check if the link is in the queue set or crawled set.
                continue  # to continue the loop. Don't add the link to the queue set.
            if Spider.domain_name not in link:  # to check if the domain name is in the url. We don't want to crawl the links that are not in the domain name. For example facebook.com, twitter.com, etc. We want to crawl the links that are in the domain name. For example kidega.com, kidega.com/cok-satanlar, etc.
                continue  # to continue the loop. Don't add the link to the queue set.
            Spider.queue.add(link)  # to add the link to the queue set.

    @staticmethod
    def update_files():  # to update the queue and crawled files. After all link crawled, all link in the queue set will be in the queue file and all link in the crawled set will be in the crawled file.
        set_to_file(Spider.queue, Spider.queue_file)  # to convert the queue set to a file.
        set_to_file(Spider.crawled, Spider.crawled_file)  # to convert the crawled set to a file.

