import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/fotograf-ve-kamera/fotograf-makinesi"

html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')   # html.parser is the default parser. We can use lxml parser also

product_list = soup.find_all('li', {'class': 'column'}, limit=7)


for product in product_list:
    name = product.div.a.h3.text.strip()
    link = product.div.a.get('href')
    old_price = product.find('div', {'class': 'priceContainer '}).find_all('span')[0].text.strip().strip('TL')
    new_price = product.find('div', {'class': 'priceContainer '}).find_all('span')[1].text.strip().strip('TL')

    old_price_num = float(old_price.replace(',', '.'))
    new_price_num = float(new_price.replace(',', '.'))
    discount_amount = old_price_num - new_price_num
    discount_rate = (discount_amount / old_price_num) * 100

    print(f"Product Name: {name}")
    print(f"Link: {link}")
    print(f"Old Price: {old_price} TL")
    print(f"New Price: {new_price} TL")
    print(f"Discount Amount: {discount_amount:.2f} TL")
    print(f"Discount Rate: {discount_rate:.2f}%\n")
