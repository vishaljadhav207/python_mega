
try:
    width = float(input("enter rectangular width: "))
    length = float(input("enter reactangular length: "))
    area = width * length
    print(area)
except ValueError:
    print("please enter no")
