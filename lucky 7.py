import random
money = 10000000000000000000
playing = True
roles = 0

while playing and money > 0:
    dice_roll = random.randint(1, 6)
    dice_roll2 = random.randint(1, 6)
    print("%d %d" % (dice_roll, dice_roll2))
    role = dice_roll + dice_roll2
    if role == 7:
        money += 4
        roles += 1
        print("You rolled a 7")
    else:
        money -= 1
        roles += 1
print("It about time it took you %d roles to lose your money" % roles)