#READ
file = open("student.txt", "r")
print(file.readable())
text = file.read()
print(text)
size = len(text)
print(size)

file.close()

#WRITE

file = open("student.txt","a")
print(file.writable())
file.write("\nMinhaz - Student of  SUST")
file.close()