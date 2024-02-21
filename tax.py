year = int(input("Please enter the year: "))
if (year <= 1852):
    print("Not within the Gregorian calendar period")
elif (year % 4):
    print("common year")
elif (year % 100):
    print("leap year")
elif (year % 400):
    print( "common Year!")
else:
    print("Leap year")