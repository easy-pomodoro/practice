# This is guess the number game
import random
print("hello, What is your name?")
my_name = input()
print("well, " + my_name + " i am thinking between the number 1 and 20")
secretnumber=random.randint(1,20)

for guesseTaken in range(6):
    print("guess the number")
    guess=int(input())

    if guess<secretnumber:
        print("guess is too low")

    elif guess>secretnumber:
        print("guess is too high")    
    else:
        break


if guess ==secretnumber:
    print("great job you guess my number in," + str(guesseTaken) + " guesses")

else:
    print("nope the number i was thinking was of," + str(secretnumber))
