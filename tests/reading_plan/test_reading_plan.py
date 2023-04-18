from unittest.mock import MagicMock

import pytest
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501


mock = [
    {
        "url": "https://blog.betrybe.com/novidades/noticia-legal",
        "title": "Notícia 01",
        "timestamp": "10/10/2022",
        "writer": "João",
        "reading_time": 4,
        "summary": "Uma notícia legal para alegrar o dia!",
        "category": "Novidades",
    },
    {
        "url": "https://blog.betrybe.com/dicas/dica-incrivel",
        "title": "Dica 02",
        "timestamp": "01/01/2023",
        "writer": "Maria",
        "reading_time": 4,
        "summary": "Uma dica incrível que você não pode perder!",
        "category": "Dicas",
    },
    {
        "url": "https://blog.betrybe.com/tecnologia/nova-ferramenta",
        "title": "Nova 03",
        "timestamp": "05/05/2023",
        "writer": "Pedro",
        "reading_time": 22,
        "summary": "Uma nova ferramenta para você otimizar o seu trabalho!",
        "category": "Tecnologia",
    },
]


def test_reading_plan_group_news():
    # mock para teste
    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock)

    # Testa se os dados de teste são agrupados corretamente
    news = ReadingPlanService.group_news_for_available_time(12)
    assert len(news["readable"]) == 1
    assert len(news["unreadable"]) == 1
    assert news["readable"][0]["unfilled_time"] == 4

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-28)
