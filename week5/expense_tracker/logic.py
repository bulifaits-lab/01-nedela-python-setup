from datetime import datetime


def sum_total(expenses):
    """Aprēķina kopējo summu."""
    return round(sum(exp["amount"] for exp in expenses), 2)


def filter_by_month(expenses, year, month):
    """Filtrē pēc mēneša."""
    result = []

    for exp in expenses:
        d = datetime.strptime(exp["date"], "%Y-%m-%d")
        if d.year == year and d.month == month:
            result.append(exp)

    return result


def sum_by_category(expenses):
    """Summē pa kategorijām."""
    totals = {}

    for exp in expenses:
        cat = exp["category"]
        totals[cat] = totals.get(cat, 0) + exp["amount"]

    return {k: round(v, 2) for k, v in totals.items()}


def get_available_months(expenses):
    """Atgriež pieejamos mēnešus."""
    months = set()

    for exp in expenses:
        months.add(exp["date"][:7])  # YYYY-MM

    return sorted(months)