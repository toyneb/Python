# Write a program that prints the numbers from 1-100
# but for multiples of thee print "Fizz" instead of the number
# and for multiples of five print print "Buzz". for multiples of
# both three and five print "FizzBuzz"

#Hint: % (modulo) tells you what's left over when you divide one number by another
# ex. number % 3 == 0


for numbers in range(1, 101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)