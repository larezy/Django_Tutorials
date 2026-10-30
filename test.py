import random
print("Welcome to Hangeman👌")

actors = ["knight", "author", "merlin"]

display_words=[]

secret_actor = random.choice(actors)
print(secret_actor)



for actor in secret_actor:
    display_words += "_"

print(display_words)




gameover= False
count = 4

while not gameover:
    guess = input("Guess the Actor: ").lower()
    for position in range(len(secret_actor)):
        letter = secret_actor[position]



        if guess in letter:
            display_words[position] = guess

    if guess not in secret_actor:
            count -= 1
            print(count)

    if count <= 0 :
        print("Game over!!, Wanna try again!")
        gameover= True


    print(display_words)

    if "_" not in display_words:
        print("You won, Try again!")
        gameover= True



