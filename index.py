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
# name = "john smith"
# age = 20
# nemPatient = True

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
# course = """
#     Hi,

#     There is our first email to you

#     thank you ,

#     The support tram
# """
# print(course)

# getting the index for the first character in a
# string = "Python For Beginners"
# print(string[0])
# print(string[:])

# formated strings
# first = "john"
# last = "smith"
# message = f"{first} [{last}] is a coder"
# print(message)

# string lenght
# strlen = "Python For Beginners"
# print(len(strlen))

# string to uppercase
# print(strlen.upper())

# sting to lowercase
# print(strlen.lower())

# find a character in py
# print(strlen.find("o"))

# replace words in py
# print(strlen.replace("Beginners", "Absolute Beginners"))

# checking if a word exists in a string
# print("Python" in strlen)

# arithmetic operations
# math functions
# x = -2.9
# y = 2.9


# approximating function
# print(round(y))

# function for returning positive number
# print(abs(x))

# using modules
# print(math.ceil(y))
# print(math.floor(y))

# if statement
# is_hot = False
# is_cold = True
# if is_hot:
#     print("It's a hot day")
#     print("Enjoy your day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day ")
#     print("Wear warm cloths")
# else:
#     print("Lovely day")

# python random numbers
# print(random.randrange(1,100))


# looping through a string
# for x in string:
#   print(x)

# while loop
# i = 1
# while i <= 5:
#   print('*' * i)
#   i = i + 1

# geussing game
# print("guessing game guess the correct number to win ")
# start_range = random.randrange(1,10)
# end_range = random.randrange(1,100)
# print(f"guess between {start_range} and {end_range}")
# secret_no = random.randrange(start_range,end_range)
# # print(secret_no)
# guess_count = 0
# guess_limit = 3
# while guess_count <= guess_limit:
#   guess = int(input("guess the secret number: "))
#   guess_count += 1
#   if guess_count <= guess_limit:
#     if guess == secret_no:
#       print("You guessed correct")
#       break
#     else:
#       print("You guessed wrong guess again")
#   else:
#     print("you have exceeded the trial run the game to try again")


# car game
# print("Welcome to my car game you can get hint of how it works by entering help")
# command = input("> ")
# while command.lower() != quit:
#     if command == "help":
#         print(
#             """
#           Commands
#           start- to start te car
#           stop- to stop the car
#           quit- to quit
#           help- opens list of commands
#     """
#         )
#         command = input("> ")
#     elif command == "start":
#         msg = print("Car started ready to go ...")
#         command = input("> ")
#     elif command == "stop":
#         msg = print("Car Stopped")
#         command = input("> ")
#     elif command == "quit":
#         confirm = input("Are you sure you want to quit:")
#         if confirm == "yes":
#             msg = print("Game Exited")
#             break
#         elif confirm == "no":
#             msg = print("Okay Your Car is still running")
#             command = input("> ")
#         else:
#             msg = print("invalid command try entering yes or no")
#             confirm = input("Are you sure you want to quit:")
#     else:
#         msg = print("I don't understand ...")
#         command = input("> ")


# for loops
