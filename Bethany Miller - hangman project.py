import random
import string
word = ["impossible", "important", "cellphone", "wonderful",
            "Jack", "dog", "house", "bubblegum!", "Mark", "books"]
print(word)
guesses = 10
guesses_right = []
guesses_made = []
random_word = random.choice(word)
playing = True
hidden = list(random_word)

for i in range(len(hidden)):
    if hidden[i] in string.ascii_letters:
        hidden.pop(i)
        hidden.insert(i, "_ ")

while guesses_made != 0 and playing:
    letter = input("wUt LeTtEr?").lower()
    if letter in guesses_made:
        print("you already guesses this letter")
    elif letter not in random_word.lower():
        print("wrong letter be smart and try another letter")
        guesses -= 1
        guesses_made.append(letter)
        print("".join(hidden))
    else:
        print("oh you are actually smart that shocking you guess the letter right!")
        guesses_right.append(letter)
        guesses_made.append(letter)
        for i in range(len(random_word)):
            if random_word[i].lower() in guesses_right:
                hidden.pop(i)
                hidden.insert(i, random_word[i])
