import random

# CSE 4256 Homework 1
# Sooyoung Jeon

# Question 1
# User based guessing game
def guess_number_user():
  # Initialize the random number in between 1 to 100
  random_number = random.randrange(1, 101)
  # Initialize the counting number as 0
  count = 0
  # Prompt the user to type the guess
  number = int(input("Enter a guess: "))
  
  # If the guessing number is not correct,
  # display the direction of the random number
  # and prompt the user until the guessing number matches
  # with the random number
  while (number != random_number):
    # Count up with one
    count += 1
    # Based on the direction of the random number,
    # disaply the appropriate message
    if (number < random_number):
      print("To low.")
    elif (number > random_number):
      print("Too high.")
    number = int(input("Enter another guess: "))
  # Print the amount of times use guessed
  print(count)

# Question 2
# Computer based guessing game
def guess_number_computer(): 
  # Initizlize the maximum and minimum number to generate
  # the random number
  max = 101
  min = 1
  # Generate the guessing number by computer
  number = random.randrange(min, max)
  # Print computer's guessing number
  print("I am guessing " + str(number))
  # Prompt the user to type the result of the guessing number
  answer = input("Enter L (for low), H (high) or C (correcrt): ")
  # Let computer keep generate the guessing number based on the 
  # result from the user
  while (answer != "C"):
    # Based on the user's answer, set appropriate range for the
    # new maximum or minimum number
    if (answer == "L"):
      min = number
    elif (answer == "H"):
      max = number
    # Generate new computer's guessing number
    number = random.randrange(min, max)
    # Print computer's guessing number
    print("I am guessing " + str(number))
    # Prompt the user again to type the result of the guessing number
    answer = input("Enter L (for low), H (high) or C (correcrt): ")
  # Print the correct message
  print("This is correct.")

  # The first function should pick a ran
guess_number_user()