# print('------ Mini Calculator-------')

num1=float(input("Enter a first num  : "))
num2=float(input("Enter a second num : "))

print("Press 1 for Addition\nPress 2 for Substraction\nPress 3 for Multiplication\nPress 4 for Division ")
choice=int(input("Enter your choice 1-4 :"))
if (choice==1):
    print("The Addition of given two number is", num1+num2)
elif (choice==2):
    print("The Substraction  of given two number is", num1-num2)
elif (choice==3):
    print("The Multiplication  of given two number is", num1*num2)
elif(choice==4) :
    print("The Division  of given two number is ", num1/num2)
else:
    print("Invalid Input")
