from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def main(request: HttpRequest) -> HttpResponse:
    """Главная страница."""
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'fourth_task/main.html', context)


def cart(request: HttpRequest) -> HttpResponse:
    """Корзина."""
    context = {
        'title': 'Корзина',
    }
    return render(request, 'fourth_task/cart.html', context)


def shop(request: HttpRequest) -> HttpResponse:
    """Магазин."""
    games: list = ['Atomic Heart', 'Cuberpunk 2077', 'PayDay 2']
    numbers_of_games: int = len(games)

    context = {
        'title': 'Игры',
        'games': games,
        'quantity': numbers_of_games,
    }
    return render(request, 'fourth_task/shop.html', context)
