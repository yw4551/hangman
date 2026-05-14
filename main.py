import random
import sys
from data import word_categories

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


def start_game():
    print(
        f"Welcome to the hangman game.\nYou have {MAX_TRIES} tries lets get started.\n"
    )
    return get_random_word()


def get_random_word():
    # the words are stored in data.py
    while True:
        cat_choice = input(
            "Please enter a category from the list (Animals, Countries, Fruits, Professions):"
        ).lower()
        if cat_choice in word_categories:
            print(f"Your choice is to play the {cat_choice}, Let's go.")
            return random.choice(word_categories[cat_choice])
        print("Invalid input: Please enter a category from the list")


def get_user_guess(guessed_letters, correct_letters):
    while True:
        user_guess = input("Enter your guess or 'quit' to quit: ").lower()

        if user_guess == "quit":
            print("Good bye! See you again later.")
            sys.exit()
        elif (
            not (user_guess.isalpha() and user_guess.isascii()) or len(user_guess) != 1
        ):
            print("Invalid input: Please enter a single letter.")
        elif user_guess in guessed_letters or user_guess in correct_letters:
            print("Invalid input: Your tried this letter already.")
        else:
            return user_guess


def handel_wrong_letter(user_letter_guess, guessed_letters, score, tries, streak):
    print(f"Sorry {user_letter_guess} is not in the word. You have lost a try.")
    guessed_letters.append(user_letter_guess)
    tries -= 1
    score -= 2
    streak = 0

    return tries, score, streak


def handel_correct_answer(
    correct_letters, user_letter_guess, random_word, score, streak
):
    correct_letters.append(user_letter_guess)
    score += random_word.count(user_letter_guess) * 5
    streak += 1

    if streak >= 2:
        score += streak * 2
    print(f"Good job {user_letter_guess} is in the word.")

    return score, streak


def play_turn(random_word, correct_letters, guessed_letters, tries, score, streak):
    word_result = display_word_result(random_word, correct_letters)
    print(display_result(word_result, guessed_letters, tries, score))
    user_letter_guess = get_user_guess(guessed_letters, correct_letters)

    if user_letter_guess not in random_word:
        tries, score, streak = handel_wrong_letter(
            user_letter_guess, guessed_letters, score, tries, streak
        )
    else:
        score, streak = handel_correct_answer(
            correct_letters, user_letter_guess, random_word, score, streak
        )

    return tries, score, streak


def display_word_result(word, correct_letters):
    return " ".join(char if char in correct_letters else "_" for char in word)


def display_result(word_result, guessed_letters, tries, score):
    return f"Word status: {word_result}\nScore: {score}\nTry amount left: {tries}\nguessed letters: {' '.join(guessed_letters)}\n"


def has_win(word, guessed_letters):
    return all(char in guessed_letters for char in word)


def final_result(has_win, tries, word, word_result, score):
    if has_win:
        return f"Great job you have won this game!\nYou guessed all letters with {tries} tries left and a score of {score}.\nThe final word was {word}."
    else:
        return f"Sorry you lost this game.\nTry again a different time.\nyou guessed {word_result} out of {word}. Your score is {score}"


def win_result(random_word, correct_letters, tries, score):
    final_word_result = display_word_result(random_word, correct_letters)
    score += tries * 5
    print(final_result(True, tries, random_word, final_word_result, score))


def lost_result(random_word, correct_letters, tries, score):
    final_word_result = display_word_result(random_word, correct_letters)
    print("\n" + final_result(False, tries, random_word, final_word_result, score))


def main():
    guessed_letters = []
    correct_letters = []
    tries = MAX_TRIES
    score = 0
    streak = 0
    user_input = menu()

    if user_input == 2:
        print("Good bye! See you later.")
        return

    random_word = start_game()

    while tries > 0:
        tries, score, streak = play_turn(
            random_word, correct_letters, guessed_letters, tries, score, streak
        )

        if has_win(random_word, correct_letters):
            win_result(random_word, correct_letters, tries, score)
            break
    else:
        lost_result(random_word, correct_letters, tries, score)


if __name__ == "__main__":
    main()
