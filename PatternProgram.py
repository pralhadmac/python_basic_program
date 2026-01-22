print(" Inverted pattern ")
n = 5

for i in range(n,0,-1):
    print("*" * i)

print("Right Angle Pattern")
n = 5
for i in range(0,n,+1):
    print("*" * i)

print(" Square Star Pattern")
n = 5
for i in range(n):
    print("*" * n)

print("Pyramid Pattern")
n = 5
for i in range(n):
    print(" " *(n - i - 1) + "*" *(2*i+1))

print("Inverted pyramid pattern")
n= 5
for i in range(n,0,-1):
    print(" "*(n-i)+"* " *i)

print("Inverted pyramid pattern with full fill")

n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2*i - 1))
