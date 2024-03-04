def greet(name):
    return f"Hey {name}!"

def concatenate(word_one, word_two):
    return word_one + word_two

def age_in_dog_years(age):
    result = age * 7
    return result
# Can only return one result if not 'none' will be defined unless: Lists or dictionaries!

print(greet('Beau'))
print(greet('Chris'))

print(concatenate('Beau', 'Griffel'))

print(age_in_dog_years(21))

print(concatenate(word_two='Beau', word_one='Griffel'))

name = "Beau"

def print_different_name():
    name = "Chris"
    print(name)
# scope function ^ Note second print(name) printed first defined name "Beau" thnx

print(name)
print_different_name()
print(name)

# Define the function

def reverse (text):
    return text[::-1]

def uppercase_and_reverse(text):
    return reverse(text.upper())

print(uppercase_and_reverse("Banana")) # ANANAB

# think datatype as a collection of functions








