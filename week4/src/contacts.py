import json
import sys
import os

# Faila nosaukums
CONTACTS_FILE = "contacts.json"


def load_contacts():
    """Ielādē kontaktus no JSON faila"""
    if not os.path.exists(CONTACTS_FILE):
        return []  # Ja nav faila → tukšs saraksts

    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_contacts(contacts):
    """Saglabā kontaktus JSON failā"""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)


def add_contact(name, phone):
    contacts = load_contacts()

    contacts.append({
        "name": name,
        "phone": phone
    })

    save_contacts(contacts)
    print(f"✓ Pievienots: {name} ({phone})")


def list_contacts():
    contacts = load_contacts()

    print("Kontakti:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} — {c['phone']}")


def search_contacts(query):
    contacts = load_contacts()

    results = [c for c in contacts if query.lower() in c["name"].lower()]

    print(f"Atrasti {len(results)} kontakti:")
    for i, c in enumerate(results, 1):
        print(f"{i}. {c['name']} — {c['phone']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Lieto: add/list/search")
        sys.exit()

    command = sys.argv[1]

    if command == "add":
        name = sys.argv[2]
        phone = sys.argv[3]
        add_contact(name, phone)

    elif command == "list":
        list_contacts()

    elif command == "search":
        query = sys.argv[2]
        search_contacts(query)