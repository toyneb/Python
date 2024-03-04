# strings are text surrounded by quotes
# Both single ('') or double ("") or triple (""") quotes are used
# examples: "dinosaurs", '2112', "I'm lovin' it!"
# /n means new line breaks in python
# triple """blank""" makes multiple line string okay.
# I can use single ('') quotes for strings if there is "" inside string characters.
# kid\'s lets python know with the \ that kid's doesn't end the string to call it
# print(f"{name} the total will be {total}") f(floats) to call variables

kanye_quote = """My greatest pain in life 
is that I will never be able
to see myself perform live."""

print(kanye_quote)

hamilton_quote = 'Well, the world got around, they said, "This kid\'s is insane, man"'

print(hamilton_quote)

name = "Beau Toyne"
orphan_fee = 200
teddy_bear_fee = 121.80

total = orphan_fee + teddy_bear_fee

#print(name,"the total will be", total)
print(f"{name} the total will be ${total:.2f}") #${total:.2f}") :.2f floats two decimals for $currency