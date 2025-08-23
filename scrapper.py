import requests
from bs4 import BeautifulSoup
import csv

# Example: scraping article titles from a website
url = "https://example.com"  # replace with real government open data site
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find example elements (update selectors as needed)
items = soup.find_all("h2")

with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title"])  # header
    for item in items:
        writer.writerow([item.get_text(strip=True)])

print("Data saved to data.csv")
