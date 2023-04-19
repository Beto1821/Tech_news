from tech_news.database import search_news
from datetime import datetime

# from winreg import QueryValue


# Requisito 7
def search_by_title(title):
    news_list = search_news(
        # options -i é para busca case-insensitive
        {"title": {"$regex": f".*{title}.*", "$options": "-i"}}
    )
    # print(news_list)
    # retorna uma lista de tuplas
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 8
def search_by_date(date):
    try:
        # Converte a data para o formato dd/mm/AAAA
        # from ISO format = fromsioformat()
        dt = datetime.fromisoformat(date).strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    # Busca as notícias no banco de dados
    news_list = search_news(
        {
            "timestamp": dt
        }
    )
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
