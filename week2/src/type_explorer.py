# type_explorer.py
# Demonstrē Python datu tipus, truthy/falsy un konversijas ar lietotāja ievadi

print("=== PAMATA DATU TIPI ===")

teksts = "Python"
skaitlis = 25
decimals = 4.75
loģiskais = False
nekas = None

print(teksts, "->", type(teksts))
print(skaitlis, "->", type(skaitlis))
print(decimals, "->", type(decimals))
print(loģiskais, "->", type(loģiskais))
print(nekas, "->", type(nekas))


print("\n=== TRUTHY / FALSY PIEMĒRI ===")

# Tukša virkne
if "":
    print("Tukša virkne ir True")
else:
    print("Tukša virkne '' ir Falsy")

# Skaitlis 0
if 0:
    print("0 ir True")
else:
    print("Skaitlis 0 ir Falsy")

# Ne-tukšs saraksts
if [1, 2, 3]:
    print("Saraksts [1,2,3] ir Truthy")

# None
if None:
    print("None ir True")
else:
    print("None ir Falsy")


print("\n=== LIETOTĀJA IEVADES KONVERSIJAS ===")

# Lietotāja ievade
user_input = input("Ievadi kādu skaitli: ")

# Konversija uz int
try:
    number_float = float(user_input)
    number_int = int(number_float)
    print("Konvertēts uz int:", number_int)
except ValueError:
    print("Nevar konvertēt uz int!")

# Konversija uz float
try:
    number_float = float(user_input)
    print("Konvertēts uz float:", number_float)
except ValueError:
    print("Nevar konvertēt uz float!")

# Konversija uz bool
print("Konvertēts uz bool:", bool(user_input))


print("\n=== PAPILDUS KONVERSIJAS PIEMĒRI ===")

print("int(3.9) =", int(3.9))        # no float uz int
print("float('10.5') =", float("10.5"))
print("bool('False') =", bool("False"))  # jebkura ne-tukša virkne = True
print("bool('') =", bool(""))            # tukša virkne = False

print("\nProgramma pabeigta.")