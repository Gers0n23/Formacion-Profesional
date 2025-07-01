import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://example.com"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find and extract the desired data from the HTML
# Example: Extract all the links on the page
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

# You can also perform more complex operations like extracting specific data from tables, forms, etc.
