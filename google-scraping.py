import requests
from bs4 import BeautifulSoup

search_input = input("Enter the search term: ").replace(" ", "+")
link = f"https://www.google.com/search?q={search_input}"
header_params = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.get(link, headers=header_params)
soup = BeautifulSoup(response.content, 'html.parser')

results = soup.find_all('div', class_='yuRUbf')


for result in results:
    title = result.find('h3').text
    link = result.find('a')['href']

    next_sibling_span = result.parent.next_sibling
    if next_sibling_span and next_sibling_span.find('span'):
        description = next_sibling_span.find('span').text
    else:
        description = "No description available"

    print(f"Title: {title}\nLink: {link}\nDescription: {description}\n")

