name = "Beau Toyne"

total = 42.75

print(f"{name} The total before a tip will be ${total:.2f}")

tip_one = 6.40
tip_two = 7.70
tip_three = 8.60

print(f"${tip_one:.2f}(15%), ${tip_two:.2f}(18%), ${tip_three:.2f}(20%)")

amount = float(input("Which tip amount would you like to leave today? (Note to leave amount without $ symobol, i.e: 6.40, 7.70, or 8.60): "))

real_amount = amount + total

print(f"{name} Your total today was ${real_amount:.2f}")
