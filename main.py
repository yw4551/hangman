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

def main():
    print(menu())

if __name__ == "__main__":
    main()