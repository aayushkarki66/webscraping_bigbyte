from bs4 import BeautifulSoup
import requests
import csv

price = []

url = "https://www.bigbyte.com.np/Laptops?limit=50"

source = requests.get(url).text

soup = BeautifulSoup(source, 'html.parser')

csv_file = open('scrapes.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Brand/Model', 'Description', 'prices'])

for i in soup.find_all('div', class_='caption'):
    Brand = i.h4.a.text
    print(Brand)

    Description = i.p.text
    print(Description)

    try:
        prices = i.find('p', class_='price').text
    except Exception as e:
        prices = None

    print(prices)

    print()

    csv_writer.writerow([Brand, Description, prices])

csv_file.close()