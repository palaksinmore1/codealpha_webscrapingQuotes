import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Website URL
url = "https://quotes.toscrape.com/"

# Step 2: Send GET request
response = requests.get(url)

# Step 3: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Extract all quote blocks
quotes = soup.find_all('div', class_='quote')

# Step 5: Prepare CSV file
with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])

    # Step 6: Loop through and extract quote + author
    for quote in quotes:
        text = quote.find('span', class_='text').text.strip()
        author = quote.find('small', class_='author').text.strip()
        writer.writerow([text, author])
        print(f"Quote: {text}\nAuthor: {author}\n")