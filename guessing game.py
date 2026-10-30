import random

# GET GUESS
def get_guess():
    return list(input("What is your guess! "))


# GENERATE COMPUTER CODE 123 {using list comprehension}
def generate_code():
    digits = [str(num) for num in range(10)]

    # Shuffle the digits
    random.shuffle(digits)
    print(digits)

    #Then grab the first three
    return digits[:3]


# GENERATE THE CLUES
def generate_clues(code , user_guess):
    if user_guess == code:
        return "CODE CRACKED!"

    # clues
    clues = []
    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")

        elif num in code:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues








# RUN GAME LOGIC
print("Welcome code breaker! Let's see if you can guess my 3 digit number!")

secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED!":
    guess = get_guess()

    clue_report = generate_clues(secret_code, guess)
    print("here is the result of your guess: ")
    for clue in clue_report:
        print(clue)

























# user  input
# def get_input():
#     return input("Enter guess")
#
# digit = []
# # generate number
# def num_generate():
#     for num in range(10):
#         digit.append(num)
#
#
#
#     return digit
# print(num_generate())





