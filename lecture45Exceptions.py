# try:
#
#     num1 = input("enter number1: ")
#     num2 = input("enter number2: ")
#     result = num2/num1
#     print(result)
#
#
# except(ZeroDivisionError, ValueError) :
#     print("You  have  entered  incorrect  input")
#
# finally:
#     print("Successful")



def  voter(age):
    if age<18:
        raise   ValueError("Invalid  Voter")
    return "You  are  allow  to  Vote"

print(voter(19))

try:
    print(voter(17))
except ValueError as  error:
    print(e)


