import time

def introduction():
    print("Welcome to the Mysterious Journey!")
    print("You find yourself at a crossroads. Your choices will determine your fate.")
    print("Let the adventure begin!\n")

def make_choice(choices):
    print("Choose your path:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def forest_path():
    print("You enter a dense forest.")
    time.sleep(1)
    print("As you walk deeper, you hear strange sounds.")
    time.sleep(1)

    choices = ["Continue through the forest", "Turn back"]
    choice = make_choice(choices)

    if choice == 1:
        print("You venture deeper into the forest.")
        time.sleep(1)
        print("You encounter a friendly creature.")
        time.sleep(1)
        print("Congratulations! You made a new friend.")
    else:
        print("You decide to turn back. The journey ends here.")

def mountain_path():
    print("You choose to climb the towering mountains.")
    time.sleep(1)
    print("The ascent is challenging, but the view is breathtaking.")
    time.sleep(1)

    choices = ["Continue climbing", "Descend"]
    choice = make_choice(choices)

    if choice == 1:
        print("You reach the summit and discover a hidden treasure.")
        time.sleep(1)
        print("Congratulations! You've found the treasure.")
    else:
        print("You decide to descend. The journey ends here.")

def main():
    introduction()

    choices = ["Take the forest path", "Climb the mountains"]
    choice = make_choice(choices)

    if choice == 1:
        forest_path()
    else:
        mountain_path()

if __name__ == "__main__":
    main()
