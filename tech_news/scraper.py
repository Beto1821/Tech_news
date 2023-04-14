import requests
from parsel import Selector
from time import sleep


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    sleep(1)
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    # > header class"entry-header"> h2 class="entry-title" > a href
    news_links = selector.css('h2.entry-title a::attr(href)').getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    try:
        # main > div > nav > div class="nav-links" > a.next.page-numbers
        next_page = selector.css('a.next::attr(href)').get()
        return next_page
    except requests.exceptions.Timeout:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
