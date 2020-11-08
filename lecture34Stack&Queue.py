from collections import deque
#Stacks
books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
books.append("Learn JavaScript")
print("Books are: ",books)

books.pop()
print("Now  top Book  is",books[-1])
books.pop()
print("Now  top Book  is",books[-1])


#QUEUE


bank = deque(["x","y","z"])
bank.append("a")
bank.append("b")
bank.append("c")
print(bank)
bank.popleft()
print(bank)



