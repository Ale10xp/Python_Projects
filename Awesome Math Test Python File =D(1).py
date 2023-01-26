import random
import math

def exponentiation(number, exponent):
    return number**exponent

def equationGeneration(x, a, b):
    c = ( ((a*(x**2)) + (b*x)) *-1)
    if c >= 0:
        c = "+" + str(c)
    else:
        str(c)
        
    return str(a) + "x²" + "+" + str(b) + "x" + str(c)  + " = 0"

def Cgenerator(x, a, b):
    return ( ((a*(x**2)) + (b*x)) *-1)

def firstSolutionFinder(a, b, c):
    xu = ( ( ((-1)* b) + math.sqrt((b**2) - (4*a*c) ))/2*a )      
    return xu

def secondSolutionFinder(a, b, c):
    xd = ( ( ((-1)* b) - math.sqrt((b**2) - (4*a*c) ))/2*a )      
    return xd

print("Welcome to the math game!")
print("In this game, you will be presented with a number and an exponent and you have to guess the result of raising the number to that exponent.")
print("Then, you will be presented with a quadratic equation and you have to guess the solutions to the equation. ")

score = 0

for level in range(1, 4):
    print("Level ", level)
    print("Guess the result of raising the number to that exponent")
    first = random.randint(-2, 2)
    second = random.randint(1, 3)

    result = exponentiation(first, second)

    print("The number: " + str(first) + " elevated to " + str(second))
    guess = input("ITS.....: ")
    try:
        guess = int(guess)
        if guess == result:
            print("CORRECT! ITS: " + str(result))
            score +=1
        else:
            print("no =(.... it just: " + str(result))
    except ValueError:
        print("You should enter a number")

    print("an Equation for the (first - second) number: " + equationGeneration(first - second, first, second) + "\n Find the two square of.... ")

    FirstGuess = input("First Square: ")
    SecondGuess = input("Second Square: ")

    f_Number = firstSolutionFinder(first, second, Cgenerator(first - second, first, second))
    s_Number = secondSolutionFinder(first, second, Cgenerator(first - second, first, second))

    try:
        FirstGuess = float(FirstGuess)
        if FirstGuess == f_Number:
            print("EXACTLY!! THE FIRST SQUARE IS: "  + str(f_Number))
            score +=1
        else:
            print("no... the first is: " + str(f_Number))
    except ValueError:
        print("You should enter a number")
