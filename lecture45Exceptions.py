try:
    list = [20, 0, 40, 50]
    result = list[0] / list[5]
    print(result)
    print("done")



except ZeroDivisionError:
    print("Dividing by  zero  is  not  possible")
 
finally:
    print("Successful")



