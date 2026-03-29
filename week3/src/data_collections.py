# --- Saraksti ---

# Izveido sarakstu
numbers = [1, 2, 3, 4, 5]

# Pievieno elementu
numbers.append(10)

# Dzēš pēdējo elementu
numbers.pop()

# Aprēķina summu un vidējo (bez sum() un len())
total = 0
count = 0

for num in numbers:
    total += num
    count += 1

average = total / count

print("# --- Saraksti ---")
print(f"Summa: {total}, Vidējais: {average}")

# Filtrē pāra skaitļus
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Pāra skaitļi: {even_numbers}")

# Slice piemēri
first_three = numbers[:3]
last_two = numbers[-2:]
every_second = numbers[::2]

print(f"Pirmie 3: {first_three}, Pēdējie 2: {last_two}")
print(f"Katrs otrais: {every_second}")


# --- Vārdnīcas ---

students = {
    "Anna": 85,
    "Jānis": 72,
    "Līga": 95
}

# Pievieno jaunu studentu
students["Pēteris"] = 88

# Maina esošu atzīmi
students["Jānis"] = 75

print("\n# --- Vārdnīcas ---")

# Iterē pa vārdnīcu
for name, grade in students.items():
    print(f"{name}: {grade}")

# Atrod labāko studentu
best_name = ""
best_grade = 0

for name, grade in students.items():
    if grade > best_grade:
        best_grade = grade
        best_name = name

print(f"Labākais students: {best_name} ({best_grade})")


# --- Kombinācija ---

students_list = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 75},
    {"name": "Līga", "grade": 95},
    {"name": "Pēteris", "grade": 88}
]

# Filtrē studenti ar >= 80
good_students = []

for student in students_list:
    if student["grade"] >= 80:
        good_students.append(student)

print("\n# --- Studenti ar atzīmi >= 80 ---")

# Izvade ar enumerate un f-string
for i, student in enumerate(good_students, start=1):
    print(f"{i}. {student['name']} — {student['grade']}")