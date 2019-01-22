import random
a = random.randint(1, 10)
guess = 5
playing = True
print("choose a number between 1 and 10")


while guess > 0 and playing:
    number_guessed = int(input("guess a number"))
    if number_guessed > a:
        print("try a little lower")
        guess -= 1
    elif number_guessed < a:
         print ("try a little higher")
         guess -= 1
    else:
        print("you de winna")
        playing = False


if not playing:
    print ("winna")
else:
    print("you lose oh well")