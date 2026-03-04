# type_explorer.py
# Mērķis: Demonstrēt Python datu tipus, truthy/falsy uzvedību un konversijas

print("=== PAMATA DATU TIPI ===")

# 1. Piešķiram vismaz 2 pamata tipu vērtības mainīgajiem
teksts = "Sveika, pasaule!"     # str
skaitlis = 42                   # int
decimālskaitlis = 3.14          # float
loģiskā_vertība = True          # bool
nekas = None                    # NoneType

# 2. Konsoles izvade ar katras vērtības tipu
print(teksts, "->", type(teksts))
print(skaitlis, "->", type(skaitlis))
print(decimālskaitlis, "->", type(decimālskaitlis))
print(loģiskā_vertība, "->", type(loģiskā_vertība))
print(nekas, "->", type(nekas))


print("\n=== TRUTHY / FALSY PIEMĒRI ===")

# 3. Truthy / Falsy piemēri

# Tukša virkne ir Falsy
if "":
    print("Tukša virkne ir True")
else:
    print("Tukša virkne '' ir Falsy")

# Skaitlis 0 ir Falsy
if 0:
    print("0 ir True")
else:
    print("Skaitlis 0 ir Falsy")

# Ne-tukšs saraksts ir Truthy
if [1, 2, 3]:
    print("Saraksts [1,2,3] ir Truthy")

# None ir Falsy
if None:
    print("None ir True")
else:
    print("None ir Falsy")


print("\n=== TIEŠĀS DATU TIPU KONVERSIJAS ===")

# 4. Explicit conversion ar robežgadījumiem

# String uz int (derīgs gadījums)
teksts_skaitlis = "100"
print("int('100') =", int(teksts_skaitlis))

# String uz int (nederīgs gadījums)
try:
    print("int('abc') =", int("abc"))
except ValueError as e:
    print("Kļūda konvertējot 'abc' uz int:", e)

# Float uz int (zaudē decimāldaļu)
print("int(3.99) =", int(3.99))

# String uz float
print("float('5.75') =", float("5.75"))

# String uz bool (robežgadījums)
print("bool('False') =", bool("False"))  # jebkura ne-tukša virkne ir True

# Tukša virkne uz bool
print("bool('') =", bool(""))  # tukša virkne ir False

print("\n=== PROGRAMMA PABEIGTA ===")