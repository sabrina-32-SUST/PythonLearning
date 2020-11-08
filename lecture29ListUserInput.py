


numOfWorsds  = 0
numOfLetters  = 0
numOfDigit  = 0

text = input("Enter a   text  of  numbers: ")

for  x  in  text:
    x = x.lower()
    if  x  >= 'a'  and x<='z':
        numOfLetters = numOfLetters+1
    elif x>='0' and  x<='9':
        numOfDigit = numOfDigit+1
    elif  x== ' ':
        numOfWorsds = numOfWorsds+1
print("Number  of Words: ", numOfWorsds)
print("Number  of Letter: ", numOfLetters)
print("Number  of Digit: ", numOfDigit)








