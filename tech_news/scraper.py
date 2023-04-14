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
    selector = Selector(html_content)
    # element>element div > p
    # Selects all <p> elements where the parent is a <div> element

    # [attribute=value]	[target="_blank"]
    # Selects all elements with target="_blank"

    url = selector.css('head > link[rel=canonical]::attr(href)').get()
    title = selector.css('div > h1.entry-title::text').get().strip()
    # print("TITULOOOOO", title)
    timestamp = selector.css('ul > li.meta-date::text').get()
    writer = selector.css('span.author a::text').get()
    # print('DADAMARAVILHA', writer)
    reading_time = selector.css('li.meta-reading-time::text').get()
    string_split = reading_time.split()
    number = int(string_split[0])
    summary = "".join(
        selector.css('div.entry-content > p:first-of-type ::text').getall()
        ).strip()
    # print("SUMARIOOOOO ", summary)
    category = selector.css('a > span.label::text').get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": number,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
