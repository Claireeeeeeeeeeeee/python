#Write a python programme to calculate the ticket price of a movie theatre
# based on the age of the customer:
#0-5yrs=free
#6-12yrs=500
#13-17yrs=1000
#18+yrs=1500

year = int(input("Enter the year"))
if year>0 and year<=5:
    print("Free of charge")
elif year>6 and year<=12:
    print("You pay 500")
elif year>13 and year<=17:
    print("You pay 1000")
else:
    print("You pay 1500")
