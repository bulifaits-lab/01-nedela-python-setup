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
        json.dump(items, f, indent=2, ensure_ascii=False)