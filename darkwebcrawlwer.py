import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

import nltk
nltk.download('punkt')
nltk.download('stopwords')

TOR_PROXY = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150',
}

def crawl_dark_web(onion_url):
    
    try:
        response = requests.get(onion_url, proxies=TOR_PROXY, timeout=15)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to access {onion_url}: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error accessing {onion_url}: {e}")
        return None


def analyze_text(content):
    
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(content)
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    return Counter(filtered_words)


def visualize_keywords(keyword_counter, top_n=10):
    
    most_common = keyword_counter.most_common(top_n)
    if not most_common:
        print("No significant keywords found to visualize.")
        return
    keywords, counts = zip(*most_common)
    plt.barh(keywords, counts, color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Keywords')
    plt.title('Top Keywords in Dark Web Content')
    plt.gca().invert_yaxis()
    plt.show()

def main():
    # .onion url to crawl
    onion_url = "http://gunsiqvaicyzyq7xqm2c3xshl6pjegtxjf3m3ldms2fo52lqvrmvbyyd.onion/"  # Replace with a valid URL

    print(f"Crawling: {onion_url}")
    html_content = crawl_dark_web(onion_url)

    if html_content:
        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')
        text_content = soup.get_text()

        print("Analyzing text content...")
        keyword_counter = analyze_text(text_content)

        print("Visualizing top keywords...")
        visualize_keywords(keyword_counter)
    
if __name__ == "__main__":
    main()