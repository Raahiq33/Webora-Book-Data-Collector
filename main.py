
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
from urllib.parse import urljoin
import time
import re

# Project settings
BASE_DIR = Path(__file__).resolve().parent
BASE_URL = "https://books.toscrape.com/"

SEARCH_KEYWORD = ""  # Example: "travel"
MAX_PAGES = 3

books = []
seen_urls = set()

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# Website connection
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Educational Python Project)"
})

print("===== AUTOMATED BOOK DATA COLLECTOR =====")

# Collect data from website
for page in range(1, MAX_PAGES + 1):

    if page == 1:
        url = BASE_URL
    else:
        url = urljoin(
            BASE_URL,
            f"catalogue/page-{page}.html"
        )

    print(f"\nCollecting page {page}...")

    try:
        response = session.get(url, timeout=15)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Request error: {error}")
        continue

    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.select("article.product_pod")

    if not items:
        print("No books found on this page.")
        break

    for item in items:

        link = item.select_one("h3 a")
        price_element = item.select_one(".price_color")
        stock = item.select_one(".availability")
        rating = item.select_one("p.star-rating")

        if not all([link, price_element, stock, rating]):
            continue

        # Book title
        title = link.get("title", "").strip()

        # Book URL
        book_url = urljoin(
            url,
            link.get("href", "")
        )

        if not title or book_url in seen_urls:
            continue

        # Optional title search
        if SEARCH_KEYWORD.lower() not in title.lower():
            continue

        # Extract numeric price safely
        price_text = price_element.get_text(strip=True)
        price_match = re.search(
            r"(\d+(?:\.\d+)?)",
            price_text
        )

        if not price_match:
            continue

        price_value = float(price_match.group(1))

        # Book rating
        rating_classes = rating.get("class", [])
        rating_value = next(
            (
                rating_map[name]
                for name in rating_classes
                if name in rating_map
            ),
            0
        )

        # Book availability
        availability = stock.get_text(
            " ",
            strip=True
        )

        books.append({
            "Title": title,
            "Price_GBP": price_value,
            "Rating": rating_value,
            "Availability": availability,
            "URL": book_url
        })

        seen_urls.add(book_url)

    print(f"Books collected so far: {len(books)}")
    time.sleep(1)

# Create DataFrame
if books:

    df = pd.DataFrame(books)

    # Data cleaning
    df["Price_GBP"] = pd.to_numeric(
        df["Price_GBP"],
        errors="coerce"
    )

    df = df.dropna(subset=["Price_GBP"])
    df = df.drop_duplicates(subset=["URL"])
    df = df[df["Price_GBP"] > 0].copy()

    if df.empty:
        print("\nNo valid book prices found.")
    else:
        # Save CSV and JSON
        csv_path = BASE_DIR / "books_data.csv"
        json_path = BASE_DIR / "books_data.json"

        df.to_csv(
            csv_path,
            index=False,
            encoding="utf-8-sig"
        )

        df.to_json(
            json_path,
            orient="records",
            indent=4,
            force_ascii=False
        )

        # Statistics
        print("\n===== COLLECTION SUMMARY =====")
        print(f"Total Books: {len(df)}")
        print(
            f"Average Price: GBP "
            f"{df['Price_GBP'].mean():.2f}"
        )
        print(
            f"Highest Price: GBP "
            f"{df['Price_GBP'].max():.2f}"
        )
        print(
            f"Average Rating: "
            f"{df['Rating'].mean():.2f}/5"
        )

        # Display first five books
        print("\n===== SAMPLE BOOK DATA =====")
        print(
            df[
                [
                    "Title",
                    "Price_GBP",
                    "Rating",
                    "Availability"
                ]
            ].head(5).to_string(index=False)
        )

        print("\nSUCCESS! Data collection completed.")
        print("CSV File: books_data.csv")
        print("JSON File: books_data.json")

else:
    print("\nNo matching books collected.")
    print("Check your internet connection or search keyword.")
