# Bing Web Scraper

A Bing web scraper with an API.

## Installation

```bash
git clone https://github.com/arturnawrot/web-scraper.git && cd web-scraper
pip install -r requirements.txt
python3 server.py
```
## Docker

```bash
docker build .
docker run -p 5000:5000 scraper
```

## Example usage

```bash
curl -X GET "http://localhost:5000/?query=Apple"
```
