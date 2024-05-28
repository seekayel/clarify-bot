
# This script scrapes COUNT random wikipedia pages and saves the contents to files named for the page title.
# Call https://en.wikipedia.org/wiki/Special:Random to get the redirect page
# and then scrape https://en.wikipedia.org/w/index.php?title=${title}&action=edit
# Extract data in textarea with id:wpTextbox1
# save the data in a file ./data/${title}.txt

import requests
from bs4 import BeautifulSoup
import re
import json
import os
import time
import random
import sys

def get_random_page_path():
    url = "https://en.wikipedia.org/wiki/Special:Random"
    response = requests.get(url, allow_redirects=False)

    path = response.url
    # Check if the response is a redirect
    if response.status_code in [301, 302, 303, 307]:
        # Get the redirect URL from the 'Location' header
        location = response.headers['Location']
        path = location.split('/')[-1]
        print(f"Location: {location}")
        print(f"Path: {path}")

    return path

def get_page_content(title):
    url = f"https://en.wikipedia.org/w/index.php?title={title}&action=edit"
    response = requests.get(url)

    for key, value in response.headers.items():
        print(f"{key}: {value}")

    soup = BeautifulSoup(response.text, 'html.parser')
    textarea = soup.find('textarea', {'id': 'wpTextbox1'})
    return textarea.text

def save_page_content(title, content):
    with open(f"./data/{title}.txt", 'w') as f:
        f.write(content)

def main():
    if not os.path.exists('./data'):
        os.makedirs('./data')
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    for i in range(count):
        print(f"Scraping [{i+1} of {count}] {i/count*100:.2f}%")
        path = get_random_page_path()
        content = get_page_content(path)
        save_page_content(path, content)
        print(f"Saved {path}")
        time.sleep(random.randint(1, 10))

if __name__ == "__main__":
    main()
