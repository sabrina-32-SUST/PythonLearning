#READ
file = open("student.txt", "r")
print(file.readable())
text = file.read()
print(text)
size = len(text)
print(size)
 
file.close()

#WRITE

file = open("studentfile.txt","w")
print(file.writable())
file.close()