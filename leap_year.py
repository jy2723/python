'''
@Author: YASHWANTH J

@Date: 2024-01-18 11:50:30

@Last Modified by: YASHWANTH J

@Last Modified time: 2024-01-18 11:50:30

@Title : Leap Year
'''
year = int(input("enter year:"))
while year>0:
    if len(str(year)) == 4:
        if (year % 400 == 0) and (year % 100 == 0):
            print("leap year")
        elif (year % 4 == 0 ) and (year % 100 != 0):
            print("leap year")
        else :
            print("not leapyear")
        break
    else:
        print("enter correct year")
        break