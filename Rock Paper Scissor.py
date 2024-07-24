import random

while True:
        print()
        user = input("Enter your choice (rock/paper/scissors): ")
        while user != "rock" and user != "paper" and user != "scissors":
            print()
            print("Invalid input.")
            print()
            user = input("Enter your choice (rock/paper/scissors): ")
        
        computer = random.choice(["rock", "paper", "scissors"])
        print()
        print("Computer chose : ",computer )
        
        if user == computer:
            print()
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
            print()
            print("You win!")
        else:
            print()
            print("Computer wins!")
