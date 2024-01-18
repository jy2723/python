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