import threading  # multithreading: multiple spiders crawling at the same time. Theareds are used to increase the speed of crawling.
from queue import Queue  # queue: store the urls to be crawled
from spider import Spider  # spider: crawl the urls
from domain import *   # domain.py: get the domain name from a url
from general import *  # general.py: create project directory and files, write and read files etc.

PROJECT_NAME = 'house_link'  # The name of the project
HOMEPAGE = 'https://www.emlakjet.com/'  # The url of the website we want to crawl
DOMAIN_NAME = get_domain_name(HOMEPAGE)  # The domain name of the website we want to crawl. For example: kidega.com
QUEUE_FILE = PROJECT_NAME + '/queue.txt'  # The file that will store the urls to be crawled
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'  # The file that will store the crawled urls
NUMBER_OF_THREADS = 4  # The number of threads (spiders) we want to use. Actually threads simply mean spiders.
queue = Queue()  # We create a queue object. Spider class will use this queue object to store the urls to be crawled.

Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)  # We create a Spider object. We pass the project name, homepage and domain name to the Spider class.


# Create worker threads (spiders)
def create_workers():  # We create threads (spiders) for each link in the queue. Every time we crawl a link, we add all the links on that page to the queue.
    for _ in range(NUMBER_OF_THREADS):  # Loop 4 times. _ means we don't care about the variable. We just want to loop 4 times.
        t = threading.Thread(target=work)  # We create a thread object. We pass the work function to the thread object. Target is the function that we want to run.
        t.daemon = True  # We set the daemon property of the thread object to True. This means that the thread will die whenever the main program dies.
        t.start()  # We start the thread.


# Do the next job in the queue
def work():
    while True:  # We want the thread to keep running as long as the program is running.
        url = queue.get()  # We get the url from the queue object. Get method removes an item from the queue.
        Spider.crawl_page(threading.current_thread().name, url)  # We call the crawl_page method of the Spider class. We pass the name of the current thread and the url to the crawl_page method.
        queue.task_done()  # We call the task_done method of the queue object. This method tells the queue that the job is done.


def create_jobs():  # Each queued link is a new job. We create jobs (spiders) for each link in the queue. Every time we crawl a link, we add all the links on that page to the queue.
    for link in file_to_set(QUEUE_FILE):  # We convert the contents of the queue file to a set. Each line will be a new item in the set.
        queue.put(link)  # We put each link in the queue object. Each queued link is a new job. For threading, we need to create a queue object. Put method adds an item to the queue.
    queue.join()  # Join the queue when all the links in the queue are crawled. We will use this method to make sure that the queue is empty.
    crawl()  # We call the crawl function because we want to crawl the links in the queue.

# queue.join() metodu, tüm işlerin kuyruktan çıkarılmasını (tamamlanmasını) beklemek ve kuyruğun tamamen boş olduğunu doğrulamak için kullanılıyor. Bu, tüm iş parçacıklarının çalışmalarının tamamlandığından emin olmak amacıyla kullanılır.


def crawl():  # Check if there are items in the queue, if so crawl them
    queued_links = file_to_set(QUEUE_FILE)  # We convert the contents of the queue file to a set. Each line will be a new item in the set.
    if len(queued_links) > 0:  # If there are items in the queue
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()  # We create jobs (spiders) for each link in the queue


create_workers()  # We create threads (spiders) for each link in the queue. Every time we crawl a link, we add all the links on that page to the queue.
crawl()  # Check if there are items in the queue, if so crawl them
