# converter.py
# Vienību konvertors

# --- Konstantes ---
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020


print("=== Vienību konvertors ===")

print("""
Izvēlies konversiju:
1 - Kilometri -> Jūdzes
2 - Jūdzes -> Kilometri
3 - Kilogrami -> Mārciņas
4 - Mārciņas -> Kilogrami
5 - Litri -> Galoni
6 - Galoni -> Litri
7 - Dolāri -> Eiro
8 - Eiro -> Dolāri
""")

choice = input("Ievadi konversijas numuru: ")

try:
    value = float(input("Ievadi vērtību: "))
except ValueError:
    print("Kļūda: jāievada skaitlis!")
    exit()

# --- Konversijas ---
if choice == "1":
    result = value * KM_TO_MI
    print(f"{value:.2f} km = {result:.2f} mi")

elif choice == "2":
    result = value / KM_TO_MI
    print(f"{value:.2f} mi = {result:.2f} km")

elif choice == "3":
    result = value * KG_TO_LB
    print(f"{value:.2f} kg = {result:.2f} lb")

elif choice == "4":
    result = value / KG_TO_LB
    print(f"{value:.2f} lb = {result:.2f} kg")

elif choice == "5":
    result = value * L_TO_GAL
    print(f"{value:.2f} L = {result:.2f} gal")

elif choice == "6":
    result = value / L_TO_GAL
    print(f"{value:.2f} gal = {result:.2f} L")

elif choice == "7":
    result = value * USD_TO_EUR
    print(f"${value:.2f} = {result:.2f} €")

elif choice == "8":
    result = value / USD_TO_EUR
    print(f"{value:.2f} € = ${result:.2f}")

else:
    print("Nepareiza izvēle! Izvēlies skaitli no 1 līdz 8.")