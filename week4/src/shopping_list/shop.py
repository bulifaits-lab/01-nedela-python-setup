import sys
from storage import load_list, save_list


def add_item(name, price):
    items = load_list()

    items.append({
        "name": name,
        "price": price
    })

    save_list(items)
    print(f"✓ Pievienots: {name} ({price} EUR)")


def list_items():
    items = load_list()

    print("Iepirkumu saraksts:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item['name']} — {item['price']} EUR")


def total():
    items = load_list()
    total_sum = sum(item["price"] for item in items)

    print(f"Kopā: {round(total_sum, 2)} EUR ({len(items)} produkti)")


def clear():
    save_list([])
    print("Saraksts notīrīts!")


if __name__ == "__main__":
    command = sys.argv[1]

    if command == "add":
        name = sys.argv[2]
        price = float(sys.argv[3])
        add_item(name, price)

    elif command == "list":
        list_items()

    elif command == "total":
        total()

    elif command == "clear":
        clear()