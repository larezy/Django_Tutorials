# get use input
import random
from re import match


def get_guess():
    return list(input("What is the number! "))

# generate numbers
def generate_code():
    digit = [str(num) for num in range(10)]

    random.shuffle(digit)

    print(digit)
    return digit[:3]

#game report
def generate_clue(user_guess, code):
    # print("First")
    if user_guess == code:
        return "CODE CRACKED!!!"

    clues = []
    # print("second")

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("MATCH")
        elif num in code:
            clues.append("CLOSE")

    if clues == []:
        return ["NOPE"]
    else:
        return clues

# game logic
print("Welcome to the LEGENDARY guessing game!!!")
secret_code = generate_code()


# While loop
clues_report = []
while clues_report != "CODE CRACKED!!!":

    guess = get_guess()
    clues_report = generate_clue(guess, secret_code)
    print("Here is the result of your guess: ")

    for clue in clues_report:
        print(clue)



