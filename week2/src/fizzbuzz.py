# fizzbuzz.py
import sys

# pārbaude vai ir ievadīts arguments
if len(sys.argv) < 2:
    print("Lūdzu norādi skaitli N.")
    sys.exit()

# mēģina pārvērst par skaitli
try:
    N = int(sys.argv[1])
except ValueError:
    print("N jābūt skaitlim.")
    sys.exit()

for i in range(1, N + 1):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=", ")
    elif i % 3 == 0:
        print("Fizz", end=", ")
    elif i % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")