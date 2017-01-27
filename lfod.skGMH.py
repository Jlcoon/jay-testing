'''
myQuestion = input("Do you like programming?: ")

if myQuestion == 'yes':
    print ("Great! Programming is fun.")
elif myQuestion == 'no':
    print ("Hmm... alright then.")
else:
    print ("!ERROR! Please answer 'yes' or no'")


myAge = int(input("Enter your age: "))

if myAge >= 18:
    print ("Congrats! You're an adult.")
elif 13 <= myAge < 18:
    print ("You're a teenager.")
elif 5 <= myAge < 13:
    print ("You're kinda young...")
else:
    print ("Goodness! How old are you?")


myAnswer = ""
while not myAnswer:
    myAnswer = input("Guess Jay's favorite food: ")

    if myAnswer == "sushi":
        print ("CORRECT!")
    else:
        while not myAnswer == "sushi":
            print ("Wrong! Try again. ")
            myAnswer = input("Guess Jay's favorite food: ")
            if myAnswer == "sushi":
                print ("CORRECT!")
'''

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

