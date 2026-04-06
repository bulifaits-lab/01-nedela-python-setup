from storage import load_expenses, save_expenses
from logic import sum_total, filter_by_month, sum_by_category, get_available_months
from export import export_to_csv
from datetime import date, datetime


CATEGORIES = [
    "Ēdiens",
    "Transports",
    "Izklaide",
    "Komunālie maksājumi",
    "Veselība",
    "Iepirkšanās",
    "Cits",
]


def show_menu():
    print("\n1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("3) Filtrēt pēc mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Dzēst izdevumu")
    print("6) Eksportēt CSV")
    print("7) Iziet")
    return input("Izvēlies: ")


def add_expense(expenses):
    today = date.today().strftime("%Y-%m-%d")
    d = input(f"Datums [{today}]: ") or today

    try:
        datetime.strptime(d, "%Y-%m-%d")
    except ValueError:
        print("❌ Nepareizs datums!")
        return

    print("\nKategorijas:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")

    try:
        cat_index = int(input("Izvēlies: ")) - 1
        category = CATEGORIES[cat_index]
    except:
        print("❌ Nepareiza izvēle")
        return

    try:
        amount = float(input("Summa: "))
        if amount <= 0:
            raise ValueError
    except:
        print("❌ Nepareiza summa")
        return

    desc = input("Apraksts: ")

    expenses.append({
        "date": d,
        "amount": amount,
        "category": category,
        "description": desc
    })

    save_expenses(expenses)
    print("✅ Pievienots!")


def show_expenses(expenses):
    if not expenses:
        print("Nav izdevumu")
        return

    print(f"\n{'Datums':<12} {'Summa':>10} {'Kategorija':<15} Apraksts")
    print("-" * 50)

    for exp in expenses:
        print(f"{exp['date']:<12} {exp['amount']:>8.2f} EUR {exp['category']:<15} {exp['description']}")

    print("-" * 50)
    print(f"Kopā: {sum_total(expenses)} EUR")


def delete_expense(expenses):
    if not expenses:
        print("Nav ko dzēst")
        return

    for i, exp in enumerate(expenses, 1):
        print(f"{i}) {exp['date']} | {exp['amount']} EUR | {exp['category']}")

    try:
        choice = int(input("Dzēst kuru?: "))
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            save_expenses(expenses)
            print("Dzēsts:", removed)
    except:
        print("❌ Nepareizi")


def main():
    expenses = load_expenses()

    while True:
        choice = show_menu()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            months = get_available_months(expenses)
            for i, m in enumerate(months, 1):
                print(f"{i}) {m}")

            try:
                m = months[int(input("Izvēlies: ")) - 1]
                year, month = map(int, m.split("-"))
                filtered = filter_by_month(expenses, year, month)
                show_expenses(filtered)
            except:
                print("❌ Kļūda")
        elif choice == "4":
            summary = sum_by_category(expenses)
            for k, v in summary.items():
                print(f"{k}: {v} EUR")
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            name = input("Faila nosaukums [data.csv]: ") or "data.csv"
            export_to_csv(expenses, name)
            print("Eksportēts!")
        elif choice == "7":
            break


if __name__ == "__main__":
    main()