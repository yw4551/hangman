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
            print("Invalid input. Please enter a valid option (1, 2): ")
        except ValueError:
            print("Invalid input. Please enter a valid option (1, 2): ")


def get_random_word():
    words = [
        "apple",
        "algorithm",
        "backpack",
        "computer",
        "cryptography",
        "diamond",
        "elephant",
        "framework",
        "galaxy",
        "hierarchy",
        "interface",
        "journal",
        "keyboard",
        "library",
        "mechanism",
        "notebook",
        "ocean",
        "puzzling",
        "rhythm",
        "strategy",
        "universe",
        "velocity",
        "weather",
        "zodiac",
    ]

    return random.choice(words)


def get_user_guess(guessed_letters):
    while True:
        user_guess = input("Enter your guess or 'quit' to quit: ").lower()

        if user_guess == "quit":
            print("Good bye! See you again later.")
            quit()
        elif not user_guess.isalpha() or len(user_guess) != 1:
            print("Invalid input: Please enter a single letter.")
        elif user_guess in guessed_letters:
            print("Invalid input: Your tried this num already.")
        else:
            return user_guess


def display_word_result(word, guessed_letters):
    word_result = ""

    for char in word:
        if char in guessed_letters:
            word_result += f"{char} "
        else:
            word_result += "_ "

    return word_result


def display_result(word_result, guessed_letters, tries):
    return f"Word status: {word_result}\nTry amount left: {tries}\nguessed letters: {' '.join(guessed_letters)}\n"


def has_win(word, guessed_letters):
    for char in word:
        if char not in guessed_letters:
            return False

    return True


def final_result(has_win, tries, word, word_result):
    if has_win:
        return f"Great job you have win this game!\nYou guessed all letters with {tries} tries left.\nThe final word was {word}."
    else:
        return f"Sorry you lost this game.\nTry again a different time.\nyou guessed {word_result} out of {word}"


def main():
    guessed_letters = []
    tries = 8
    user_input = menu()

    if user_input == 1:
        print("Welcome to the hangman game.\nYou have 8 tries lets get started.\n")
        random_word = get_random_word()

        while tries > 0:
            word_result = display_word_result(random_word, guessed_letters)
            print(display_result(word_result, guessed_letters, tries))
            user_letter_guess = get_user_guess(guessed_letters)
            guessed_letters.append(user_letter_guess)

            if user_letter_guess not in random_word:
                print(
                    f"Sorry {user_letter_guess} is not in the word. You have lost a try."
                )
                tries -= 1
            else:
                print(f"Good job {user_letter_guess} is in the word.")

                if has_win(random_word, guessed_letters):
                    final_word_result = display_word_result(
                        random_word, guessed_letters
                    )
                    print(final_result(True, tries, random_word, final_word_result))
                    break
        else:
            final_word_result = display_word_result(random_word, guessed_letters)
            print("\n" + final_result(False, tries, random_word, final_word_result))

    else:
        print("Good bye! See you again later.")


if __name__ == "__main__":
    main()
