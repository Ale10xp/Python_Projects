from random import randint as rd

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
phonetic_alphabet = ["alpha", "bravo", "charlie", "delta", "echo", "fox", "golf", "hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniforme", "victor", "whiske", "x-ray", "yanke", "zulu"]


import re

import time

def random_alphabet(times):

    temp_list_alphabet = alphabet
    temp_list_phonetic_alphabet = phonetic_alphabet
    points = 0
    
    for i in range(times):
        number = rd(0, len(temp_list_alphabet))
        
        print(temp_list_alphabet[number].title())
        
        guess = input("guess: ")
        
        if guess == temp_list_phonetic_alphabet[number]:
            print("YES!")
            points+=1
            
        else:
            print("no, its" + temp_list_phonetic_alphabet[number])

            
        temp_list_alphabet.pop(number)
        temp_list_phonetic_alphabet.pop(number)
            

    print("Total points: " + str(points) + " of " + str(times) + " (" + str((points/times)*100) + "%)")


def double_random_alphabet(times):

    temp_list_alphabet = alphabet
    temp_list_phonetic_alphabet = phonetic_alphabet
    points = 0
    
    for i in range(times):
        number = rd(0, len(temp_list_alphabet)-1)
        number_two = rd(0, len(temp_list_alphabet)-1)
        
        print(temp_list_alphabet[number].title() + " and " +temp_list_alphabet[number_two].title())
        guess = input("guess: ")
        
        #guesses = guess.split("and")
        guess = re.sub(" ", "", guess)
        guess = guess.lower()
        

        guesses = guess.split(",")
        #for i in range(len(guesses)):
            #guesses[i] = re.sub(" ", "", guesses[i])


        
        if (guesses[0] == temp_list_phonetic_alphabet[number]) and (guesses[1] == temp_list_phonetic_alphabet[number_two]):
            print("\nYES!")
            #print(temp_list_alphabet[number].title() + " and " + temp_list_alphabet[number_two].title() + " is equal to" )
            print(temp_list_phonetic_alphabet[number].title() + " and " + temp_list_phonetic_alphabet[number_two].title() + "\n")
            points+=1
            
        else:
            print("no, its: " + temp_list_phonetic_alphabet[number] + " and " + temp_list_phonetic_alphabet[number_two])

            
        temp_list_alphabet.pop(number)
        temp_list_phonetic_alphabet.pop(number)
            

    print("Total points: " + str(points) + " of " + str(times) + " (" + str((points/times)*100) + "%)")
    time.sleep(7)



def array_random_alphabet(times, array):

    

    temp_list_alphabet = alphabet
    temp_list_phonetic_alphabet = phonetic_alphabet
    points = 0

    
    for i in range(array):

        numbers = [rd(0, len(temp_list_alphabet)-1) for x in range(array)]
        print(numbers)
        print(i)
        print(numbers[i])
        
        first_element = temp_list_phonetic_alphabet[numbers[i]]
        
        second_element = None
        
        if i == int((len(numbers)-1)):
            second_element = temp_list_phonetic_alphabet[numbers[0]]
        else:
            second_element = temp_list_phonetic_alphabet[numbers[i+1]]
                                                 
        arwers = [first_element, second_element]

        first_element = str(first_element)
        second_element = str(second_element)
        
                                                 
        print(temp_list_alphabet[temp_list_phonetic_alphabet.index(first_element)].title() + " and " + temp_list_alphabet[temp_list_phonetic_alphabet.index(second_element)].title())
        guess = input("guess: ")
        guess = guess.lower()

        #guess = re.sub(" ", "", guess)
        #guesses = guess.split(",")

        guesses = guess.split("and")
        for i in range(len(guesses)):
            guesses[i] = re.sub(" ", "", guesses[i])


        
        if (guesses == arwers):
            print("\nYES!")
            print(temp_list_alphabet[temp_list_phonetic_alphabet.index(first_element)].title() + " and " + temp_list_alphabet[temp_list_phonetic_alphabet.index(second_element)].title() + " is equal to" )
            print(arwers[0].title() + " and " + arwers[1].title() + "\n")
            points+=1
            
        else:
            print("no, its: " + arwers[0].title() + " and " + arwers[1].title())

            
        temp_list_alphabet.pop(temp_list_phonetic_alphabet.index(first_element))
        temp_list_phonetic_alphabet.pop(temp_list_phonetic_alphabet.index(first_element))
        #print("Poped from list: " + first_element.title() + " and " +second_element.title())
        temp_list_alphabet.pop(temp_list_phonetic_alphabet.index(second_element))
        temp_list_phonetic_alphabet.pop(temp_list_phonetic_alphabet.index(second_element))
            


    print("Total points: " + str(points) + " of " + str(times) + " (" + str((points/times)*100) + "%)")
    time.sleep(7)




number_of_attemps = int(input("Choose the number of attemps: "))


array_random_alphabet(number_of_attemps, number_of_attemps)
