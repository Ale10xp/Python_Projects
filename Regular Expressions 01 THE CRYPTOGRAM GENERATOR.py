# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import re 
text = input("Put Something to Crypto: ")
text = str(text)
text = text.lower()

search = re.search('[a]', text)

findall = re.findall('[a]', text)


otherText = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
otherText_n = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26"
print(search)

print(findall)
print("Splited text: ")
print(re.split(" ",text))


print(re.split("\s", otherText))
print(re.split("\s", otherText_n))

def cripto(args, args_two, text):
    nexttext = text
    for i in range(len(args)):
        nexttext = re.sub(args[i], args_two[i], nexttext)
    return nexttext
    

strings = ['a','e','i','o','u']

strings = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o', 'p','q','r','s','t', 'u','v','w','x','y','z']

strings = re.split("\s", otherText)
replaces = re.split("\s", otherText_n)

#replaces = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15', '16','17','18','19','20', '21','22','23','24','25','26']

#print(len(strings) )

#replaces = ["4","3","1","0","u"]
print("\nCrypted text:")
print(cripto(strings, replaces, text))

print("\nUncrypted text")
print(cripto(replaces, strings, text).title())
print("\nCrypt details: \nspace=0, a=1, b=2 ... z=26 ")
#print(list(map(text, cripto(strings, replaces, text))) )

#text = text.upper()

text = re.sub("a","4", text)
text = re.sub("e","3", text)
text = re.sub("i","1", text)
text = re.sub("o","0", text)
print("\nAnother Cryptogram")
print(text.lower())
