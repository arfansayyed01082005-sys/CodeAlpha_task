import random

def play_hangman():
    
    words = ["python", "keyboard", "monitor", "laptop", "coding"]
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_lives = 6
    display_word = "" 

    print("Welcome to Hangman!")
    
    
    while incorrect_guesses < max_lives:
        
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Lives remaining: {max_lives - incorrect_guesses}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")

        
        if "_" not in display_word:
            break

       
        guess = input("Guess a letter: ").lower()

       
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not there.")

    
    if "_" not in display_word:
        print("\nYou won! The word was:", secret_word)
    else:
        print("\nGame Over! The word was:", secret_word)

if __name__ == "__main__":
    play_hangman()
