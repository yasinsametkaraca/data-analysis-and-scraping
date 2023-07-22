import requests
from bs4 import BeautifulSoup
import re

header_params = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


def get_category_url(category):
    url = f"https://www.n11.com/{category}"
    html = requests.get(url, headers=header_params).content
    soup = BeautifulSoup(html, 'html.parser')  # html.parser is the default parser. We can use lxml parser also

    product_list = soup.find_all('li', {'class': 'column'}, limit=7)

    for product in product_list:
        name = product.div.a.h3.text.strip()
        link = product.div.a.get('href')
        price_container = product.find('div', {'class': 'priceContainer'})
        if price_container is not None:
            old_price_element = price_container.find('span')
            if old_price_element is not None:
                old_price = old_price_element.text.strip().strip('TL')
                old_price = re.sub(r'[^\d.]', '', old_price)
                old_price_num = float(old_price) if old_price else 0.0
            else:
                old_price = "N/A"
                old_price_num = 0.0

            new_price_element = price_container.find_all('span')[1]
            if new_price_element is not None:
                new_price = new_price_element.text.strip().strip('TL')
                new_price = re.sub(r'[^\d.]', '', new_price)
                new_price_num = float(new_price) if new_price else 0.0
            else:
                new_price = "N/A"
                new_price_num = 0.0

            discount_amount = old_price_num - new_price_num
            discount_rate = (discount_amount / old_price_num) * 100

            print(f"Product Name: {name}")
            print(f"Link: {link}")
            print(f"Old Price: {old_price} TL")
            print(f"New Price: {new_price} TL")
            print(f"Discount Amount: {discount_amount:.2f} TL")
            print(f"Discount Rate: {discount_rate:.2f}%\n")


while True:
    print("Available Categories:")
    print("1. fotograf-ve-kamera")
    print("2. telefon-ve-aksesuarlari")
    print("3. elektronik")
    print("4. bilgisayar")
    print("5. televizyon-ve-ses-sistemleri")
    print("6. elektrikli-ev-aletleri")
    print("7. eskisi-bizde-yenisi-sende")
    print("8. video-oyun-konsol")
    print("9. beyaz-esya")
    print("0. Exit")

    choice = input("Choose a category (0-9): ")

    if choice == "0":
        break
    elif choice == "1":
        get_category_url("fotograf-ve-kamera")
    elif choice == "2":
        get_category_url("telefon-ve-aksesuarlari")
    elif choice == "3":
        get_category_url("elektronik")
    elif choice == "4":
        get_category_url("bilgisayar")
    elif choice == "5":
        get_category_url("televizyon-ve-ses-sistemleri")
    elif choice == "6":
        get_category_url("elektrikli-ev-aletleri")
    elif choice == "7":
        get_category_url("eskisi-bizde-yenisi-sende")
    elif choice == "8":
        get_category_url("video-oyun-konsol")
    elif choice == "9":
        get_category_url("beyaz-esya")
    else:
        print("Invalid choice. Please try again.")


