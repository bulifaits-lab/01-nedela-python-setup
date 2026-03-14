# eligibility.py

age = int(input("Ievadi vecumu: "))
license = input("Vai ir autovadītāja apliecība? (j/n): ")
student = input("Vai ir students? (j/n): ")
veteran = input("Vai ir veterāns? (j/n): ")

print("\n---")

# Balsošana
if age >= 18:
    print("Balsošana:        Jā ✓")
else:
    print("Balsošana:        Nē ✗")

# Auto īre
if age >= 21 and license == "j":
    print("Auto īre:         Jā ✓")
elif age < 21:
    print("Auto īre:         Nē ✗ (par jaunu)")
else:
    print("Auto īre:         Nē ✗ (nav apliecības)")

# Senioru atlaide
if age >= 65 or veteran == "j":
    print("Senioru atlaide:   Jā ✓")
else:
    print("Senioru atlaide:   Nē ✗")

# Studentu atlaide
if age >= 16 and age <= 26 and student == "j":
    print("Studentu atlaide:  Jā ✓")
else:
    print("Studentu atlaide:  Nē ✗")