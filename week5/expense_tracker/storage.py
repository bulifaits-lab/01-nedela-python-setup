import json
import os

FILE_PATH = "expenses.json"


def load_expenses():
    """Nolasa izdevumus no JSON faila."""
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    """Saglabā izdevumus JSON failā."""
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)