# darkweb-crawler

> Lightweight dark web OSINT tool that crawls .onion sites through Tor, performs NLP-based keyword extraction, and visualizes content patterns for threat intelligence.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Tor](https://img.shields.io/badge/Tor-7D4698?style=flat-square&logo=torproject&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-154F5B?style=flat-square&logoColor=white)

## Overview

A reconnaissance tool designed for **threat intelligence** and **OSINT research**. It connects to `.onion` services through a local Tor SOCKS5 proxy, scrapes page content, strips HTML using BeautifulSoup, tokenizes text with NLTK, filters stopwords, and outputs the most frequent keywords as a visualization.

Built for security researchers and CTF players who need quick insight into dark web page content.

## Features

- Tor SOCKS5 proxy routing for anonymous `.onion` access
- HTML parsing and clean text extraction via BeautifulSoup
- NLP tokenization and stopword filtering (NLTK)
- Top-N keyword frequency visualization (matplotlib)
- Configurable proxy, timeout, and keyword count

## Prerequisites

- [Tor Browser](https://www.torproject.org/) running locally on port `9150`
- Python 3.7+

## Installation

```bash
git clone https://github.com/AARUSHGAUR/Dark-Web-crawler.git
cd Dark-Web-crawler
pip install requests beautifulsoup4 nltk matplotlib pysocks
```

## Usage

```bash
# 1. Start Tor Browser (must be running on port 9150)
# 2. Edit the target .onion URL in the script
# 3. Run
python darkwebcrawlwer.py
```

## How It Works

```.onion URL → Tor Proxy → HTTP GET → BeautifulSoup (HTML → Text) → NLTK Tokenizer → Stopword Filter → Keyword Counter → matplotlib Chart```

## Project Structure

```
Dark-Web-crawler/
├── darkwebcrawlwer.py    # Main crawler script
└── README.md             # Documentation
```

## Disclaimer

This tool is intended for **legal security research and educational purposes only**. The author is not responsible for any misuse. Always comply with applicable laws and regulations when accessing dark web resources.

## License

MIT