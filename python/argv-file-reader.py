# From the module environment import argument variable
from sys import argv
# variables linked to the argument variable, this is where argv gets "unpackes"
# and gives a value to st of parameters v
script, filename = argv
# sets function to variable 'txt' function open's variable 'filename' of said parameter
txt = open(filename)
# prints out txt within ("txt") and has formatted variable assigned
print("Here's your file %r:" % filename)
# prints out the value of varibale 'txt' aka: reads parameter filename
print(txt.read())
# Always close files after opening them.
txt.close()
# prints out the string ("txt")
print("Type the filename again:")
# sets up variable function and gives a prompt
file_again = input("> ")
# sets variable a function which opens file of previous parameter 'filename'
txt_again = open(file_again)
# prints out the 'txt_again' variable by reading or disputing its file value
print(txt_again.read())
# Always close files after opening them.
txt_again.close()