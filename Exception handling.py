try:
    a = int(input("enter the a value"))
    b = int(input("enter the a value"))
    c = a / b
    print("value of c:", a / b)
except Exception:
    print("cannot divide by zero")


    #universal exception of  error
try:
    a = int(input("enter the a value"))
    c = a / b
    print("value of c:", a / b)
except Exception:
    print("b value is not mentioned")
    print("After exception")

""" 
    # exceptions for each type of errors
try:
    a = int(input("enter the a value"))
    c = a / b
    print("value of c:", a / b)
except NameError:
    print("b value is not mentioned")
try:
    a = 10
    b = 0
    print("div=", a / b)
except ZeroDivisionError:
    print("Arithmatic exception")
try:
    a = int(input("enter a value"))
    b = int(input("enter b value"))
    print("div=", a + b)
except ValueError:
    print("Value error")
try:
    a = [10, 20, 30, 40, 50, 60]
    print(a[0])
    print(a[7])
except IndexError:
    print("Array index out of bound")
try:
    dic = {"one": "1", "two": "2", "three": "3"}
    print(dic["five"])
    # file not found
    fp = open("sathya,txt")
except KeyError:
    print("key error")
try:

except IOError:
    print("file input or output error")
"""