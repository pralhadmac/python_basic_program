num = int(input("Please enter the number : "))

a = 0
b = 1

for i in range(num):
    print(a, end=" ")
    a, b = b, a + b