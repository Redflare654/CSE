import random
word = ["impossible", "important", "cellphone", "wonderful",
            "Jack", "dog", "house", "bubblegum!", "Mark", "books"]
print(word)
guesses = 10
guess_right = []
letters_guess_wrong = []
guesses_made = []
random_word = random.choice(word)
playing = True
hidden = list(random_word)

while guesses_made < 0 and playing:
    letter = input("wUt LeTtEr?")
    if letter in random_word: guess_right