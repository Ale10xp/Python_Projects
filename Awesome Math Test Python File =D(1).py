import random
import math

def expo(a, b):
    return a**b

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

    

#result = expo(input("The number: "), input("Elevated to: "))

first = random.randint(-2, 2)
second = random.randint(1, 3)
                        
result = expo(first, second)
                        
print(" the number: " + str(first) + " elevated to " + str(second))
guess = input("ITS.....: ")


if guess == result:
    print("CORRET! ITS: " + str(result))
else:
    print("no =(.... it just: " + str(result))


print("an Equation for the (first - second) number: " + equationGeneration(first - second, first, second) + "\n Find the two square of.... ")

FirstGuess = input("First Square: ")
SecondGuess = input("Second Square: ")

f_Number = firstSolutionFinder(first, second, Cgenerator(first - second, first, second))
s_Number = secondSolutionFinder(first, second, Cgenerator(first - second, first, second))

if FirstGuess == f_Number:
    print("EXACTLY!! THE FIRST SQUARE IS: "  + str(f_Number))
else:
    print("no... the first is: " + str(f_Number))

if SecondGuess == s_Number:
    print("and... CONGRATS the Second SQUARE IS: "  + str(s_Number))
else:
    print("and no... the second is: " + str(s_Number))
