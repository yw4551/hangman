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

def main():
    user_input = menu()
    if user_input == 1:
        random_word = get_random_word()
        print(random_word)

if __name__ == "__main__":
    main()