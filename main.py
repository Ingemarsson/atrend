import requests
import lxml
from bs4 import BeautifulSoup
import json
import csv
from rich import print

headers = {
    'Accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

with open('data/data.json', 'r', encoding='utf-8') as file:
    data = json.loads(file.read())

with open('data/data.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            "SKU",
            "Link",
            "Product Name",
            "Features",
            "Description"
        )
    )
    
for i in data:
    for link in i:
        req = requests.get(i[link], headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')
        productName = soup.find('h1', class_='product-title').text
        productFeatures = soup.find('div', class_='toggle-content').findAll('ul')
        productDescription = soup.find('div', class_='toggle-content').findAll('p')
        with open('data/data.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    link,
                    i[link],
                    productName,
                    productFeatures,
                    productDescription
                )
            )
