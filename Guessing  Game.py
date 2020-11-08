from  random  import randint
n = int(input("Enter  Number: "))
point = 0

for x in range(1,n+1):
    guessNumber = int(input("Enter  your  guess: "))
    randomNumber = randint(1, 10)
    print("Random  Number  is: ", randomNumber)
    if guessNumber == randomNumber:
        point = point + 1
        print("you  have  won &  get point: ", point)

    else:
        point = point - 1

        print("you  have  Lost & get point: ", point)


