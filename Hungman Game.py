import random

def hangman():
    print("---------WELCOME TO HANGMAN MINI GAME----------")
    
    words_to_guess = ["java", "cpp", "javascript", "ruby", "swift", "python"]
    
    while True:
        pc_pick = random.choice(words_to_guess)
        attempts = 5
        guessed_letters = []
        correct_letters = set(pc_pick)    # make a set of pc_pick  e.g: {j,a,v,a}
        word_to_display = ['_' for _ in pc_pick]
        
        while attempts > 0 and '_' in word_to_display:
            print("\nCurrent word: " + ' '.join(word_to_display))
            print(f"Attempts remaining: {attempts}")
            print(f"Wrong guesses: {', '.join([char for char in guessed_letters if char not in correct_letters])}")
            
            user_guess = input("Guess a letter or the full word: ").lower()

            # Check if the input is valid
            if len(user_guess) != 1 and user_guess != pc_pick:
                print("Please enter a single letter or the full word.")
                continue
            
            # Check if the user has already guessed this letter
            if user_guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
                continue
            else:
                guessed_letters.append(user_guess)

            # Check if the guess is correct
            if user_guess in correct_letters:
                print(f"Good guess! '{user_guess}' is in the word.")
                for index, letter in enumerate(pc_pick):
                    if letter == user_guess:
                        word_to_display[index] = user_guess
            else:
                print(f"Sorry, '{user_guess}' is not in the word.")
                attempts -= 1

        if '_' not in word_to_display:
            print(f"Congrats! You've guessed the word: '{pc_pick}'")
        else:
            print(f"Game Over! The correct word was '{pc_pick}'.")

        # ask if the user wants to play again 
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

hangman()
