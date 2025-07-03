# # diamond pattern

# #     *
# #   * * *
# # * * * * *
# #   * * *
# #     *

n = 3

for i in range(n): #upper part

    for j in range(n - i - 1):
        print(" ", end=" ")
 
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()


for i in range(n - 1): #lower part

    for j in range(i + 1):
        print(" ", end=" ")
 
    for j in range(2 * (n - i - 2) + 1):
        print("*", end=" ")
    print() 