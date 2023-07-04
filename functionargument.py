def Majina(fname,lname,age):
    print("My name is " + fname +" " +lname + " and i'm " + age + " years old.")
Majina("Keith","Powers","30")
Majina("Gabrielle","Union","35")
Majina("Mike","Myles","29")
  #Create a function for the average of a list
# data=[2,3,5,7,11,13,17]
def Calculate_average(numbers):
    total=sum(numbers)
    count=len(numbers)
    average=total/count
    return average
dataset=[2,3,5,7,11,13]
answer=Calculate_average(dataset)
print("The average is", answer)

#     sum(data)
#     len(data)
#     a=float(input("The sum of data"))
#     b=float(input("The length of the data"))
#     results=a/b
#     print("The average is", results)
# average_of_the_numbers()
#



