# calculatior////////

a= int(input("Enter number"))
b= int(input("Enter number"))



print("press 1 for addition")
print("press 2 for substraction")
print("press 3 for multiplication")
print("press 4 for division")
user = input("Enter your choice(1,2,3,4):")


if user == '1':
    result = a+b
    print("The result of addition is:",result)

elif user =='2':
    result = a-b
    print("The result of substraction is:",result)

elif user == '3':
    result = a*b
    print("The result of multiplication is:",result)

elif user == '4':
    result = a/b
    print("The result of division is:",result)

else:
    print("Invilid choice.. Please select a valid option..")