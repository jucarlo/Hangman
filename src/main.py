import random

# Hangman ASCII stages
stages = [
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

# Word list
word_list = ["water", "dog", "camel"]

# Pick a random word
chosen_word = random.choice(word_list)

# Initialize lives and progress
lives = 6
display = "_" * len(chosen_word)
correct_letters = set()
game_over = False

print("Welcome to Hangman!")
print(display)

# Main game loop
while not game_over:
    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in correct_letters:
        print(f"You already tried the letter '{guess}'.")
        continue

    # Update progress
    new_display = ""
    letter_found = False
    for letter in chosen_word:
        if letter == guess:
            new_display += letter
            letter_found = True
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print(display)

    # Win condition
    if "_" not in display:
        print("You win! 🎉 The word was:", chosen_word)
        game_over = True
    # Wrong guess
    elif not letter_found:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life. Lives left: {lives}")
        print(stages[lives])
        if lives == 0:
            print("You lose! 😢 The word was:", chosen_word)
            game_over = True
    else:
        correct_letters.add(guess)