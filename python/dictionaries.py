# states = ['NY', 'PA', 'CA']
# states = ['New York', 'Pennsylvania', 'California']
# states = ['New York', 'NY', 'Pennsylvania', 'PA', 'California', 'CA']
# Key-Value pair ex. {'NY': 'New York'}

states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

print(states['NY'])

# print(states['FL'])  KeyError: 'FL'

people = ["Mattan", "Chris"]
# print(people[2])  IndexError: list index out of range

print(type(states))
print(type(people))

print(states.get('FL', 'Not found'))
print(states.get('NY', 'Not found'))

print(states.keys())
print(states.values())

states['FL'] = 'Florida'
print(states)

#user = ['Beau', 70.5, 11, 'Blue', 'Blue']
user = {'name': 'Beau', 'height': 70.5, 'shoe size': 11, 'clothes': 'Blue', 'eye color': 'Blue'}

blog_post = {'title': '11 Sexy Uses for Dictionaries', 'body': 'Blah blah blah...'}

print(user['name'])
print(blog_post['title'])

# Dictionaries and lists can be inside of each other

animal_sounds = {
    "cat": ["meow", "purr"],
    "dog": ["woof", "bark"],
    "fox": []
}
# list inside of a dictionary ^

Beau = {'name': 'Beau', 'height': 70.5, 'shoe size': 11, 'clothes': 'Blue', 'eye color': 'Blue'}
Chris = {'name': 'Beau', 'height': 68, 'shoe size': 10, 'clothes': 'Blue', 'eye color': 'Blue'}
Sarah = {'name': 'Beau', 'height': 72, 'shoe size': 8, 'clothes': 'Blue', 'eye color': 'Blue'}

people = [Beau, Chris, Sarah]

print(people)

for person in people:
    print(person.get('height', "Not Found"))
#person.get represents getting height but if not found returns "not found"









