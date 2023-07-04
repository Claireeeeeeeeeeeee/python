# number = int(input("Enter the number"))
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
print("Please select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
select=int(input("Select operation"))
if select==1:
    print("The sum is" ,num1+num2)
elif select==2:
    print("The difference is" ,num1-num2)
elif select==3:
    print("The product is" ,num1*num2)
elif select==4:
    print("The expo is" ,num1-num2)
else:
    print("Invalid input")



# print("The difference is" ,num1-num2)
# print("The product is" ,num1*num2)
# print("The expo is",num1/num2)
