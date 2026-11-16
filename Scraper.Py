
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

# Starting website
current_url = "https://books.toscrape.com/"

# Store all collected books
all_books = []

# Keep visiting pages while a next page exists
while current_url:

    print("Visiting:", current_url)

    response = requests.get(current_url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books on the current page
    books = soup.find_all("article", class_="product_pod")

    # Collect information from each book
    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p", class_="price_color"
        ).get_text(strip=True)

        rating = book.find(
            "p", class_="star-rating"
        )["class"][1]

        availability = book.find(
            "p", class_="availability"
        ).get_text(strip=True)

        all_books.append([title, price, rating, availability])

    # Find the next page
    next_button = soup.find("li", class_="next")

    if next_button:
        next_page = next_button.a["href"]
        current_url = urljoin(current_url, next_page)
    else:
        current_url = None

# Save all collected books
with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:

    writer = csv.writer(file)

    writer.writerow(["Title", "Price", "Rating", "Availability"])

    writer.writerows(all_books)

print("Total books collected:", len(all_books))
print("Data saved successfully!")

