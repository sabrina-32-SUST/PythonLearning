##Map
def  square(x):
    return x*x
num = [1,2,3,4,5]

result = list(map(square,num))
print(result)


#FIlter

num = [1,2,3,4,5,6,7,8]
result =  list(filter(lambda x:x%2==0,num))

print(result)


