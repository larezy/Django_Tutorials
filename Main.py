import random
#1 Greeting
#2 Create a word list
#3 create a secret_word using random
#4 Create an empty list
#5 user input(guess)
#6 for loop to handle checking of letters
#7 for loop to handle position of letters
#8 while loop continue play
#9 add a counter for tracking wrong guesses
#############################################################
#1
print("Welcome to the Legendary Guessing game")

#2
players = ["rice", "messi", "eze"]

#3
secret_player = random.choice(players)
# print(secret_player)
#4
display_player =[]

#10 counter for wrong guess
count = 0

#6
for letter in secret_player:
    display_player += "_"

print(display_player)

#8 while loop
game_over = False

while not game_over:
    # 5 guess
    guess = input("Guess the player: ").lower()
    # print(f"{len(guess)} + length")

    #bonus
    if len(guess) > 1:
        guess = guess[0]


    #7
    for position in range(len(secret_player)):
        letter = secret_player[position]
        if letter == guess:
            display_player[position] = letter
    print(display_player)

    #11 counter check and reduction
    if guess not in secret_player:
        count += 1
        print(count)

        if count >= 4:
            print("You Lost, Try Again Champ")
            game_over = True


    #9 exit loop as winner
    if "_" not in display_player:
        print("You Won!")
        game_over = True