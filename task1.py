import random
words = ["apple", "banana", "grape", "mango", "peach"]
secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word)
guessed_letters = []
max_attempts = 6
remaining_attempts = max_attempts
print("Welcome to the Hangman Game!")
print("Try to guess the word letter by letter.")
while "_" in guessed_word and remaining_attempts > 0:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", ", ".join(guessed_letters))
    print("Remaining Attempts:", remaining_attempts)
    guess = input("Enter a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
        print("Correct guess!")
    else:
        remaining_attempts -= 1
        print("Wrong guess!")
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nGame Over. The word was:", secret_word)