import random
word = ["impossible", "important", "cellphone", "wonderful",
            "Jack", "dog", "house", "bubblegum!", "Mark", "books"]
print(word)
letters_guess = 10
letters_guess_right = []
guesses_made = []
random_word = random.choice(word)
playing = True
hidden = list(random_word)
