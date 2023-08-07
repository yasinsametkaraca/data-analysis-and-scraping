from urllib.parse import urlparse


def get_domain_name(url):  # Get domain name (kidega.com) from a url
    try:
        results = get_sub_domain_name(url).split('.')  # We get the sub domain name. For example: book.kidega.com. Then we split it by dot. We get ['book', 'kidega', 'com']
        return results[-2] + '.' + results[-1]  # We return the last two items of the list. We get 'kidega' and 'com'. Then we join them with a dot. We get 'kidega.com'
    except:
        return ''


def get_sub_domain_name(url):  # Get sub domain name (book.kidega.com) from a url
    try:
        return urlparse(url).netloc  # urlparse() method returns a tuple. We get the netloc part of the tuple. netloc is the domain name. For example: book.kidega.com
    except:
        return ''


# print(get_domain_name('https://www.kidega.com/cok-satanlar'))  # kidega.com
# print(get_sub_domain_name('https://www.book.kidega.com/cok-satanlar'))  # www.book.kidega.com

