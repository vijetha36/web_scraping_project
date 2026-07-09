import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = []

for item in soup.find_all("article", class_="product_pod"):
    title = item.h3.a["title"]
    price = item.find("p", class_="price_color").text

    books.append([title, price])

df = pd.DataFrame(books, columns=["Book Name", "Price"])

df.to_csv("books.csv", index=False)

print("Data saved successfully!")
