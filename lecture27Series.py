#1+2+3+4+5+.....+n

n= int(input("Enter  the  last  Number: "))
sum = 0
for  x in range(1,n+1,1):
    sum= sum + x

print(sum)

#2+4+6+8+10+.........n

n= int(input("Enter  the  last  Number: "))
sum = 0
for  x in  range(2,n+1,2):
    sum = sum+x

print(sum)

#1+3+5+7+.....+n

n= int(input("Enter  the  last  Number: "))
sum = 0
for  x in  range(1,n+1,2):
    sum = sum+x

print(sum)

#1*1+2*2+3*3+.....+n*n
n= int(input("Enter  the  last  Number: "))
sum = 0
for  x in  range(1,n+1,1):
    sum = sum+(x*x)

print(sum)


# 2*2+4*4+6*6.....+n*n
n= int(input("Enter  the  last  Number: "))
sum = 0
for  x in  range(2,n+1,2):
    sum = sum+(x*x)

print(sum)


#1*2*3*4*5*.....*n

n= int(input("Enter  the  last  Number: "))
sum = 1
for  x in range(1,n+1,1):
    sum= sum * x
print(sum)