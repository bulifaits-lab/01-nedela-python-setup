# guess.py
import random

while True:  # spēle atkārtojas, ja lietotājs grib spēlēt vēlreiz

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Es esmu izvēlējies skaitli no 1 līdz 100.")

    while True:
        guess = input("Tavs minējums: ")

        # pārbauda vai ievade ir skaitlis
        try:
            guess = int(guess)
        except ValueError:
            print("Lūdzu ievadi skaitli!")
            continue

        attempts += 1

        if guess > number:
            print("Par lielu")
        elif guess < number:
            print("Par mazu")
        else:
            print(f"Pareizi! Tu uzminēji {attempts} mēģinājumos.")
            break

        if attempts >= max_attempts:
            print("Beidzās mēģinājumi!")
            print(f"Pareizais skaitlis bija: {number}")
            break

    # piedāvā spēlēt vēlreiz
    again = input("Spēlēt vēlreiz? (j/n): ")

    if again.lower() != "j":
        print("Paldies par spēli!")
        break