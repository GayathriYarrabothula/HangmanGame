import random

words = [
    # Fruits
    "Apple", "Banana", "Orange", "Strawberry", "Mango",
    "Pineapple", "Grapes", "Watermelon", "Kiwi", "Peach",

    # Animals
    "Elephant", "Lion", "Tiger", "Giraffe", "Zebra",
    "Kangaroo", "Monkey", "Dolphin", "Penguin", "Koala",

    # Birds
    "Eagle", "Sparrow", "Peacock", "Owl", "Hawk",
    "Parrot", "Swan", "Flamingo", "Pigeon", "Hummingbird",

    # Food Items
    "Pizza", "Burger", "Pasta", "Sushi", "Chocolate",
    "Ice Cream", "Pancake", "Sandwich", "Salad", "Popcorn"
    ]

def runHangman():
    while(True):
        choice = random.randint(0, 39)
        if choice < 10:
            print("Hint: Name of a Fruit")
        elif choice < 20:
            print("Hint: Name of an Animal")
        elif choice < 30:
            print("Hint: Name of a Bird")
        else:
            print("Hint: Name of a Food item")
        original = words[choice]
        name = original
        n = len(original)
        guess = "-" * n
        chances = n + 2
        while chances > 0:
            print(guess)
            char = input()[0]
            if char in original:
                indx = original.index(char)
                guess = guess[:indx] + char + guess[indx+1:]
                original = original[:indx] + '0' + original[indx+1:]
            else:
                chances -= 1
                if chances == 0:
                    print("YOU LOST THE GAME")
                print(f"you have {chances} more chances")
            if guess == name:
                print("YOU WON THE GAME")
                break
        print("Do you want to play again? (y/n)")
        if(input() != 'y'):
            break

runHangman()