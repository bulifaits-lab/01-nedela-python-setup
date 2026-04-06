import json
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent / "expenses.json"


def load_expenses():
    """Nolasa izdevumus no JSON faila."""
    if not FILE_PATH.exists():
        return []

    with FILE_PATH.open("r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    """Saglabā izdevumus JSON failā."""
    with FILE_PATH.open("w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)