import random

randomNumber = random.randrange(1, 100)

def main():
    print ""
    number = input("I have a number between 1 and 100. Can you guess my number in seven trys? Please type your first guess: ")
    guess(number)

def guess(number1):
    userGuess = 1
    while userGuess < 7:
        userGuess += 1
        if number1 > randomNumber:
            print "Too high. Try again."
            print ""
        elif number1 < randomNumber:
            print "Too low. Try again."
            print ""
        elif number1 == randomNumber:
           break
        number1 = input ("What number do you guess? ")
    if number1 == randomNumber:
       playAagain = raw_input ("Excellent! You guessed the number! Would you like to play again (y or n)? ")
       if playAagain == "y":
            main()
    else:
        playAagain = raw_input ("I'm sorry, you did not guess the number. Would you like to play again (y or n)? ")
        if playAagain == "y":
             main()

main()

'''
A) Python is an efficient object-oriented programming language. It is simple to use and easy to learn making it a popular
choice among programmers today. It requires little typing compared to languages such as java but some it is not "strongly
typed" which could introduce bugs into the program.

B) I enjoyed Python over Scratch myself, as someone with expeirience in multiple other programming languages I found Scratch
to be slow compared to Python. I do see how Scratch can help those just beginning in the programming world but once you start
working with other OOP languages such as Ruby you appreciate the speed and accuracy at which you can program with them. I found
Python to be quite simillar to Ruby which is why I was so comfortable with it right from the start.

C) I had two friends in the class and decided since I had the most expeirience with programming that I would work alone. I have
programmed in pairs before however and find it quite usefull to collaberate on ideas and have another mind around when you are
stuck.
'''
