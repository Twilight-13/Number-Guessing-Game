import random

print("Welcome to Number Guessing Game!")
print("I am Arijit Singha Roy, the Developer.")

print("Let the guessing game begin!")
print("You will get 10 guesses until you guess the correct number.")

starting_number = int(input("Enter the starting number: "))
ending_number = int(input("Enter the ending number: "))
print("Your Number Range is {} to {}".format(starting_number, ending_number))

trophy = [
    "       $$$$$$$$$$$       ",  # Top of the cup
    "      $$$$$$$$$$$$$      ",  # Top of the cup
    "     $$$$$$$$$$$$$$$     ",  # Wider top
    "    $$$$         $$$$    ",  # Handles
    "   $$$$           $$$$   ",  # Handles
    "   $$$$           $$$$   ",  # Cup body
    "    $$$$         $$$$    ",  # Cup body
    "     $$$$$$$$$$$$$$$     ",  # Bottom of the cup
    "      $$$$$$$$$$$$$      ",  # Stem top
    "       $$$$$$$$$$$       ",  # Stem bottom
    "          $$$$$          ",  # Base connector
    "        $$$$$$$$$        ",  # Base
    "       $$$$$$$$$$$       ",  # Larger base
    "      $$$$$$$$$$$$$      ",  # Largest base
]

loser = [
    "L               OOOOO     SSSSS   EEEEE  RRRRR  ",
    "L              O     O   S       E      R    R ",
    "L              O     O    SSSS   EEEE   RRRRR  ",
    "L              O     O       S   E      R   R  ",
    "LLLLLLLLLL      OOOOO    SSSSS   EEEEE  R    R ",
]

random_number = random.randint(starting_number, ending_number)

guesses = 0
while guesses < 10:
    guess = int(input("Guess the number: "))
    if guess == random_number:
        print("Congrats! You guessed the correct number.")
        for row in trophy:
            print(row)
        guesses += 1
        break
    elif guess >= random_number * 1.5:
        print("Too high!")
        guesses += 1
    elif guess <= random_number * 0.5:
        print("Too low!")
        guesses += 1
    elif random_number * 0.75 >= guess > random_number * 0.5:
        print("Guess a little bit higher!")
        guesses += 1
    elif random_number * 1.25 <= guess < random_number * 1.5:
        print("Guess a little bit lower!")
        guesses += 1
    elif random_number * 0.85 >= guess > random_number * 0.75:
        print("Almost there, just a little bit higher!")
        guesses += 1
    elif random_number * 1.15 <= guess < random_number * 1.25:
        print("Almost there, just a little bit lower!")
        guesses += 1
    elif random_number * 0.95 >= guess > random_number * 0.85:
        print("Just a tiny bit higher!")
        guesses += 1
    elif random_number * 1.05 <= guess < random_number * 1.15:
        print("Just a tiny bit lower!")
        guesses += 1
    elif random_number * 0.99 >= guess > random_number * 0.95:
        print("Just a teeny tiny bit higher!")
        guesses += 1
    elif random_number * 1.01 <= guess < random_number * 1.05:
        print("Just a teeny tiny bit lower!")
        guesses += 1
    else:
        print("Nah! Not quite there!")
        guesses += 1
else:
    print("Sorry, All guesses used...you lost!")
    for row in loser:
        print(row)
