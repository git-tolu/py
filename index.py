import math 
import random
# print("hello, puthon")
# age = 11
# if age == 10:
#   print("ten")
# elif age == 11:
#   print("eleven")
# else:
#   print("invalid")

# quick work
name = "john smith"
age = 20
nemPatient = True

# input function
# name = input("what is your name? ")
# print("Hi " + name)

# quick work
# name = input("what is your name? ")
# fav_color = input("what is your favourite color? ")
# print(name + "'s favourite color is " + fav_color)

# program to get birth year
# birth_yr = input("what is your birth year: ")
# print(type(birth_yr))
# age = 2023 - int(birth_yr)
# print(type(age))
# print("Your Age is " + str(age))

# quick work
# user_weight = input("what is your weight in pounds: ")
# user_weight_kg = int(user_weight) * 0.45
# print("your weight in kg is " + str(user_weight_kg))

# python strings
course = '''
    Hi, 
    
    There is our first email to you
    
    thank you ,
    
    The support tram 
'''
print(course)

# getting the index for the first character in a
string = "Python For Beginners"
print(string[0])
print(string[:])

# formated strings
first = 'john'
last = 'smith'
message = f'{first} [{last}] is a coder'
print(message)

# string lenght
strlen = "Python For Beginners"
print(len(strlen))
# string to uppercase
print(strlen.upper())
# sting to lowercase
print(strlen.lower())
# find a character in py
print(strlen.find('o'))
# replace words in py
print(strlen.replace('Beginners', 'Absolute Beginners'))
# checking if a word exists in a string
print('Python' in strlen)

# arithmetic operations
# math functions
x = -2.9
y = 2.9
# approximating function
print(round(y))
# function for returning positive number
print(abs(x))

# using modules
print(math.ceil(y))
print(math.floor(y))

# if statement
is_hot = False
is_cold = True
if is_hot:
  print('It\'s a hot day')
  print('Enjoy your day')
  print('Drink plenty of water')
else:
  print('It\'s a cold day ')
  print('Wear warm cloths')


# python random numbers
print(random.randrange(1,100))


# looping through a string
for x in string:
  print(x)