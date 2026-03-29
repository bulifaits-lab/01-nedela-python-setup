import sys
from storage import load_list, save_list, get_price, set_price
from utils import calc_line_total, calc_grand_total, count_units


def ask_price(name):
    existing = get_price(name)

    if existing is not None:
        print(f"Atrasta cena: {existing}")
        choice = input("[A/M]? ").strip().lower()

        if choice == "a":
            return existing
        if choice == "m":
            price = float(input("Jaunā cena: "))
            set_price(name, price)
            return price

    price = float(input("Cena: "))
    set_price(name, price)
    return price


def add_item(name, qty, price=None):
    if price is None:
        price = ask_price(name)

    items = load_list()
    items.append({
        "name": name,
        "qty": qty,
        "price": price,
    })
    save_list(items)

    print(f"✓ Pievienots: {name} × {qty} = {round(qty * price, 2)} EUR")


def list_items():
    items = load_list()

    print("Iepirkumu saraksts:")
    for i, item in enumerate(items, 1):
        line_total = calc_line_total(item)
        print(f"{i}. {item['name']} × {item['qty']} — {line_total} EUR")


def total():
    items = load_list()
    total_sum = calc_grand_total(items)
    units = count_units(items)

    print(f"Kopā: {round(total_sum, 2)} EUR ({units} vienības)")


def clear():
    save_list([])
    print("Saraksts notīrīts!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Lietošana: add <name> <qty> [price] | list | total | clear")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 4:
            print("add requires name and qty")
            sys.exit(1)

        name = sys.argv[2]
        qty = int(sys.argv[3])
        price = float(sys.argv[4]) if len(sys.argv) > 4 else None
        add_item(name, qty, price)

    elif command == "list":
        list_items()

    elif command == "total":
        total()

    elif command == "clear":
        clear()

    else:
        print(f"Neatpazīts komanda: {command}")
        sys.exit(1)
