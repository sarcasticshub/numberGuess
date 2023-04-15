import random

randNumber = random.randint(1, 100)
print (randNumber)
userGuess = None
guesses = 0

try:
    while userGuess != randNumber:
        userGuess = int(input(".....GUESS THE VALUE...... \n"))
        guesses += 1
        if userGuess == str:
             print ("ENTER THE VALID INTEGER VALUE")
             
        elif userGuess == randNumber:
                print("....YOU GUESS THE RIGHT NUMBER... ")
        else:
                if userGuess > randNumber:
                    print("ENTER THE SMALLER NUMBER ")
                else:
                    print("ENTER THE LARGER NUMBER ")


    print(f"YOU GUESS THE CORRECT NUMBER IN {guesses} GUESSES")
    
except Exception as e :
     print("ENTER THE VALID VALUE ...........")

else:
    with open("highscore.txt", "r")as f:
            highscore = int(f.read())
    with open("highscore.txt", "w")as f:
            if guesses < highscore:
                f.write(str(guesses))
                print(".........CONGRATULATION !!! YOU BREAK THE HIGHSCORE........")

     