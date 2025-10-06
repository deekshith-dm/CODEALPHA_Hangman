import random

def hangman():
    # Predefined word list
    words = ["python", "hangman", "program","deekshith", "random", "simple"]
    
    # Randomly select a word
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    attempts_left = 6

    print("🎮 Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.")
    print("You have 6 incorrect guesses allowed.")
    print("Word to guess: ", " ".join(guessed_word))

    while attempts_left > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter only a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print(f"❌ You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in word:
            print(f"✅ Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts_left -= 1
            print(f"❌ Wrong guess! '{guess}' is not in the word. Attempts left: {attempts_left}")

        print("Word: ", " ".join(guessed_word))
        print("Guessed letters: ", ", ".join(guessed_letters))

    # End of game
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)


# Run the game
if __name__ == "__main__":
    hangman()




















