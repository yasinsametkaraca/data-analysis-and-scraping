import os


# Each website you crawl is a separate project (folder)
def make_directory(directory):  # to create directory
    if not os.path.exists(directory):
        os.makedirs(directory)


# make_directory("project_data")


def create_data_files(project_name, base_url):  # to create project folder and files
    queue = os.path.join(project_name, "queue.txt")
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")


def write_file(path, data):  # to write project_data to the file
    with open(path, "w", encoding='utf-8') as f:
        f.write(data)


# create_data_files("project_data", "https://www.kidega.com/cok-satanlar")


def append_to_file(path, data):  # to append project_data to the file
    with open(path, 'a', encoding='utf-8') as f:
        f.write(data + '\n')


def delete_file_contents(path):  # to delete the contents of a file
    open(path, 'w').close()  # open the file in write mode and close it. Actually, it will delete the contents of the file. Because we opened the file in write mode.


def file_to_set(file_name):  # to convert file contents to set. Each line will be a new item in the set. We will use this function to convert the contents of the queue and crawled files to sets.
    results = set()  # If we don't use set, there will be duplicate links in the queue and crawled files.
    with open(file_name, 'rt', encoding='utf-8') as f:  # rt: read text
        for line in f:
            results.add(line.replace('\n', ''))  # We don't want to add the new line character to the set.
    return results


def set_to_file(links, file_name):  # to convert set to file. We will use this function to convert the queue and crawled sets to files.
    with open(file_name, "w", encoding='utf-8') as f:
        for link in sorted(links):
            f.write(link + "\n")
