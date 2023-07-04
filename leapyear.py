# create a python program to check if a given year is a leap year
# The year is divisible by 4 but not divisible by 100
# Except if it's also divisible by 400
year = int(input("Enter the year"))
if year % 400 == 0 or year % 4 == 0:
    print("It is a leap year")
elif year % 100 != 0:
    print("Not a leap year")

#Write a python programme to calculate the ticket price of a movie theatre
# based on the age of the customer
#