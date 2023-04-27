import requests
from bs4 import BeautifulSoup
import json
from collections import Counter

def count_words(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    words = soup.get_text().split()
    word_count = Counter(words)
    return word_count

url = input("Enter the URL of the website: ")
word_count = count_words(url)
sorted_count = {word: freq for word, freq in word_count.items()}
result = json.dumps(sorted_count, indent=4)
print(result)

