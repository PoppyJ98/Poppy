#Begin with asking name and having it greet you back (maybe I can add 2 players?)
name1 = input("What is your name, Player 1?   ")
print ("Are you sure?   ")
while True:
     answer = input(" (yes/no)   ") 

     if answer == "yes":
        print("Hello," + name1 + "!")
        break
     else: 
        name1 = input ("Try again. What is your name??   ")   
#This is then repeated but a function can stop this
print("You are Player1, think of a secret number")
print("Next Player")

name2 = input("What is your name   ")
print ("Are you sure?   ")
while True:
     answer = input(" (yes/no)  ") 

     if answer == "yes":
        print("Hello," + name2 + "! You are Player2.")
        break
     else: 
        name2 = input ("Try again. What is your name??   ") 

print("Now let's play the number guessing game!")

secret = int(input("Player2, please close your eyes. Player1, please enter your secret number   "))
number = int(input("Player2, Try guess the secret number   "))
while True:
    if number==secret:
        break
    else:
        number=int(input("Not quite, try again!   "))
print ("You won!! You guessed the secret number!")

