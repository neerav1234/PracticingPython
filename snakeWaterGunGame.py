import random


itr = 0
mypoints = 0
computerPoints = 0
lst = ["s", "w", "g"]
while itr < 10:
    choice = input(
        f"{itr+1}. Press s for snake w for water, g for gun: ",
    )
    comp = random.choice(lst)
    if choice == "s":
        if comp == "s":
            print("Computer's Choice was: ", comp)
            print("IT'S A TIE!")
            print(f"Your Score: {mypoints}, Computer's Score: {computerPoints}")
        elif comp == "w":
            print("Computer's Choice was: ", comp)
            print("YOU WIN!")
            mypoints += 1
            print(f"Your Score: {mypoints}, Computer's Score: {computerPoints}")
        else:
            print("Computer's Choice was: ", comp)
            print("YOU LOSE!")
            computerPoints += 1
            print(f"Your Score: {mypoints}, Computer's Score: {computerPoints}")
        
    elif choice == "w":
        if comp == "w":
            print("Computer's Choice was: ", comp)
            print("IT'S A TIE!")
            print(f"Your Score: {mypoints}, Computer's Score: {computerPoints}")
        elif comp == "g":
            print("Computer's Choice was: ", comp)
            print("YOU WIN!")
            mypoints += 1
            print(f"Your Score: {mypoints}, Computer's Score: {computerPoints}")
        else:
            print("Computer's Choice was: ", comp)
            print("YOU LOSE!")
            computerPoints += 1
            print(f"Your Score: {mypoints}, Computer's Score: {computerPoints}")
        
    elif choice == "g":
        if comp == "g":
            print("Computer's Choice was: ", comp)
            print("IT'S A TIE!")
            print(f"Your Score: {mypoints}, Computer's Score: {computerPoints}")
        elif comp == "s":
            print("Computer's Choice was: ", comp)
            print("YOU WIN!")
            mypoints == 1
            print(f"Your Score: {mypoints}, Computer's Score: {computerPoints}")
        else:
            print("Computer's Choice was: ", comp)
            print("YOU LOSE!")
            computerPoints += 1
            print(f"Your Score: {mypoints}, Computer's Score: {computerPoints}")
    else:
        print("#Invalid Input#")
        itr-=1
        
    itr += 1
    
print("\n\n*****Final Scores*****\n")
print(f"Your Final Score: {mypoints}, Computer's Final Score: {computerPoints}\n")

if mypoints > computerPoints:
    print("Yay! YOU WIN")
elif computerPoints > mypoints:
    print("You Lose!, BETTER LUCK NEXT TIME")
else:
    print("The Game is a TIE!")
