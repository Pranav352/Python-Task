# enter numbers and print that number of table


n=int(input("Enter a number:"))

print("Table for",n) #it print the n values

for i in range(1,11): #range between 1 to 11 it'll print 1 to 10
    result = n * i
    print(f"{n} * {i} = {result}")  # n value multiply with i and = result of multiply #f-string method
