import random

def menu():
    print("\n===================")
    print("   Hang Man Game")
    print("===================\n")
    print("Welcome! Are you ready to start playing?")
    while True:
        print("Choose your option")
        print("1. Start playing")
        print("2. Exit")
        try:
            user_input = int(input("Enter your option (1, 2): "))
            if user_input in [1, 2]:
                return user_input
            print('Invalid input. Please enter a valid option (1, 2): ')
        except ValueError:
            print('Invalid input. Please enter a valid option (1, 2): ')


def get_random_word():
    words = [
        "apple", "algorithm", "backpack", "computer", "cryptography", 
        "diamond", "elephant", "framework", "galaxy", "hierarchy", 
        "interface", "journal", "keyboard", "library", "mechanism", 
        "notebook", "ocean", "puzzling", "rhythm", "strategy", 
        "universe", "velocity", "weather", "zodiac"
    ]

    return random.choice(words)


def get_user_guess(guessed_letters):
    while True:
        user_guess = input("Enter your guess: ").lower()

        if not user_guess.isalpha() or len(user_guess) != 1:
            print("Invalid input: Please enter a single letter.")
        elif user_guess in guessed_letters:
            print("Invalid input: Your tried this num already.")
        else:
            return user_guess
        

def display_result(word, guessed_letters, tries):
    word_result = ""
    
    for char in word:
        if char in guessed_letters:
            word_result += f"{char} "
        else:
            word_result += "_ "

    return f"Word status: {word_result}\nTry amount left: {tries}\nguessed letters: {' '.join(guessed_letters)}"


def has_win(word, guessed_letters):
    for char in word:
        if char not in guessed_letters:
            return False

    return True


def main():
    guessed_letters = []
    tries = 8
    user_input = menu()
    if user_input == 1:
        random_word = get_random_word()
        user_letter_guess = get_user_guess(guessed_letters)
        guessed_letters.append(user_letter_guess)
        print(display_result(random_word, guessed_letters, tries))
        print(has_win(random_word, guessed_letters))

if __name__ == "__main__":
    main()