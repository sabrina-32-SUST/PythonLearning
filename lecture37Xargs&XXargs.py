#Xargs

def  student(*details):
    print(details)
student(1010,"Sabrina")
student(3432,"Nusrat",3.00)

def  add(*numbers):
    sum = 0
    for  num in numbers:
        sum = sum+num
    print(sum)

add(20,21)
add(4,3,2,1)

#XXargs


def  students(**detail):
    print(detail)
students(id=1001,name="Sabrina")