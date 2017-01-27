import random
myNumber = random.randint(1,100)
myGuess = int(input("Guess a number between 1 - 100: "))
tries = 1

while myGuess != myNumber:
    if myGuess > myNumber:
        print ("Lower!")
    else:
        print ("Higher!")
    myGuess = int(input("Guess a number between 1 - 100: "))
    tries += 1
if myGuess == myNumber:
    print ("----------------------- ")
    print("Congrats!", myNumber, "is the answer.")
    print("You tried", tries, "time(s)!")

