import json
import os

FILE = "shopping.json"


def load_list():
    """Ielādē iepirkumu sarakstu"""
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_list(items):
    """Saglabā sarakstu"""
    with open(FILE, "w", encoding="utf-8") as f:
<<<<<<< HEAD
        json.dump(items, f, indent=2, ensure_ascii=False) 

PRICES_FILE = "prices.json"


def load_prices():
    if not os.path.exists(PRICES_FILE):
        return {}

    with open(PRICES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_prices(prices):
    with open(PRICES_FILE, "w", encoding="utf-8") as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)


def get_price(name):
    return load_prices().get(name)


def set_price(name, price):
    prices = load_prices()
    prices[name] = price
    save_prices(prices)
=======
        json.dump(items, f, indent=2, ensure_ascii=False)
>>>>>>> 152a66bbd89c19ca3c25b70eb3df3f09e00a15d0
