import random

words = ["python", "pandas", "binary", "coding", "laptop"]
word = random.choice(words)

guessed = []
lives = 6

while lives > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\n" + display)

    if "_" not in display:
        print("You win! The word was", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single letter")
    elif guess in guessed:
        print("You already guessed that")
    else:
        guessed.append(guess)
        if guess not in word:
            lives -= 1
            print(f"Wrong! Lives left: {lives}")
else:
    print("Game over! The word was", word)