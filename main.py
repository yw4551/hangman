import random
import sys

MAX_TRIES = 8


def menu():
    print("\n===================")
    print("=  Hang Man Game  =")
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
    word_categories = {
        "animals": [
            "elephant",
            "giraffe",
            "kangaroo",
            "dolphin",
            "penguin",
            "cheetah",
            "octopus",
            "crocodile",
            "squirrel",
            "butterfly",
        ],
        "countries": [
            "argentina",
            "brazil",
            "canada",
            "denmark",
            "egypt",
            "france",
            "germany",
            "hungary",
            "italy",
            "japan",
        ],
        "fruits": [
            "apple",
            "banana",
            "cherry",
            "strawberry",
            "elderberry",
            "fig",
            "grapefruit",
            "honeydew",
            "kiwi",
            "lemon",
        ],
        "professions": [
            "architect",
            "baker",
            "carpenter",
            "dentist",
            "engineer",
            "farmer",
            "geologist",
            "hairdresser",
            "illustrator",
            "judge",
        ],
    }

    while True:
        cat_choice = input(
            "Please enter a category from the list (Animals, Countries, Fruits, Professions):"
        ).lower()
        if cat_choice in word_categories:
            print(f"Your choice is to play the {cat_choice}, Let's go.")
            return random.choice(word_categories[cat_choice])
        print("Invalid input: Please enter a category from the list")


def get_user_guess(guessed_letters):
    while True:
        user_guess = input("Enter your guess or 'quit' to quit: ").lower()

        if user_guess == "quit":
            print("Good bye! See you again later.")
            sys.exit()
        elif not user_guess.isalpha() or len(user_guess) != 1:
            print("Invalid input: Please enter a single letter.")
        elif user_guess in guessed_letters:
            print("Invalid input: Your tried this letter already.")
        else:
            return user_guess


def display_word_result(word, guessed_letters):
    return " ".join(char if char in guessed_letters else "_" for char in word)


def display_result(word_result, guessed_letters, tries, score):
    return f"Word status: {word_result}\nScore: {score}\nTry amount left: {tries}\nguessed letters: {' '.join(guessed_letters)}\n"


def has_win(word, guessed_letters):
    return all(char in guessed_letters for char in word)


def final_result(has_win, tries, word, word_result, score):
    if has_win:
        return f"Great job you have won this game!\nYou guessed all letters with {tries} tries left and a score of {score}.\nThe final word was {word}."
    else:
        return f"Sorry you lost this game.\nTry again a different time.\nyou guessed {word_result} out of {word}. Your score is {score}"


def main():
    guessed_letters = []
    tries = MAX_TRIES
    score = 0
    user_input = menu()
    streak = 0

    if user_input == 1:
        print(
            f"Welcome to the hangman game.\nYou have {MAX_TRIES} tries lets get started.\n"
        )
        random_word = get_random_word()

        while tries > 0:
            word_result = display_word_result(random_word, guessed_letters)
            print(display_result(word_result, guessed_letters, tries, score))
            user_letter_guess = get_user_guess(guessed_letters)
            guessed_letters.append(user_letter_guess)

            if user_letter_guess not in random_word:
                print(
                    f"Sorry {user_letter_guess} is not in the word. You have lost a try."
                )
                tries -= 1
                score -= 2
                streak = 0
            else:
                score += random_word.count(user_letter_guess) * 5
                streak += 1
                if streak >= 2:
                    score += streak * 2
                print(f"Good job {user_letter_guess} is in the word.")

                if has_win(random_word, guessed_letters):
                    final_word_result = display_word_result(
                        random_word, guessed_letters
                    )
                    score += tries * 5
                    print(
                        final_result(True, tries, random_word, final_word_result, score)
                    )
                    break
        else:
            final_word_result = display_word_result(random_word, guessed_letters)
            print(
                "\n" + final_result(False, tries, random_word, final_word_result, score)
            )

    else:
        print("Good bye! See you again later.")


if __name__ == "__main__":
    main()
