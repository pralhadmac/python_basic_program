# # 🔹 1. Basic Input / Output
#
# message = "Print “Hello World”"
# print(f"{message}")
#
# # Take input from user and print it
# a= input("Please eneter the user name : ")
# print(a)
#
# # Swap two numbers (with & without temp variable)
# print("Swap two number with temp : ")
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# print(f"First number = {num1} and Second number = {num2}")
# temp = num1
# num1 = num2
# num2 = temp
# print(f" With temp result : First number = {num1} and Second number = {num2}")
# num1, num2 = num2 , num1
# print(f" Without temp result : First number = {num1} and Second number = {num2}")
# # Check even or odd
#
# # Check positive, negative, or zero
#
# num3 = int(input("Please enter the number : "))
# if num3 > 0:
#     print(f"{num3} is positive")
# elif num3 < 0:
#     print(f"{num3} is negative")
# else:
#     print(f"{num3} is Zero")
#
# # Find largest of two numbers
# num4 = int(input("Please enter the First number : "))
# num5 = int(input("Please enter the second number : "))
# if num4 > num5:
#     print(f"{num4} is largest from {num5}")
# else:
#     print(f"{num5} is largest from {num4}")
#
# # Find largest of three numbers
# num6 = int(input("Please enter the First number : "))
# num7 = int(input("Please enter the second number : "))
# num8 = int(input("Please enter the three number : "))
# if num6 > num7 and num6 > num8:
#     print(f"Largest number is {num6}")
# elif num7 > num6 and num7 > num8:
#     print(f"Largest number is {num7}")
# else:
#     print(f"Largest number is {num8}")
# 🔹 2. Number Programs

# Check prime number
num = int(input("Please enter the number : "))
if num <= 1:
    print("Not a prime number.")
else:
    for i in range(2,num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number.")

# Print prime numbers in a range
limit = int(input("Please enter the number : "))

for num in range(2, limit + 1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(f"{num}")
# Factorial of a number
num = int(input("Please enter the number : "))

fact = 1

for i in range(1,num + 1):
    fact = fact * i

print("Factorial : ",fact)
# Fibonacci series
num = int(input("Please enter the number : "))

a = 0
b = 1

for i in range(num):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
# Reverse a number
num = int(input("Please enter the number : "))

reverse = 0
while num > 0:
    reverse = reverse *10 + num % 10
    num = num //10

print("Reversed number = ", reverse)

# Check palindrome number

# Check Armstrong number

# Sum of digits of a number

# Count digits in a number

# 🔹 3. String Programs (VERY IMPORTANT)

# Reverse a string

# Check palindrome string

# Count vowels and consonants

# Count characters in a string

# Find duplicate characters in a string

# Remove spaces from string

# Check anagram

# Convert string to upper/lower case

# Find first non-repeating character

# 🔹 4. List Programs (Most Asked)

# Find largest & smallest number in list

# Remove duplicates from list

# Sort list (with & without sort())

# Reverse a list

# Count frequency of elements

# Find second largest number

# Merge two lists

# Check list is empty or not

# Find common elements in two lists

# 🔹 5. Dictionary Programs

# Create dictionary and access values

# Iterate over dictionary

# Count frequency of words using dictionary

# Sort dictionary by key

# Sort dictionary by value

# Merge two dictionaries

# 🔹 6. Tuple & Set Programs

# Convert list to tuple

# Find length of tuple

# Set operations (union, intersection, difference)

# Remove duplicates using set

# 🔹 7. Functions

# Create a function with parameters

# Function with return value

# Lambda function example

# Recursive function (factorial)

# 🔹 8. OOPs (Basic Interview Level)

# Create a class and object

# Constructor example

# Single inheritance example

# Method overriding

# Encapsulation example

# 🔹 9. File Handling (Basic)

# Read a file

# Write data to file

# Append data to file

# Count number of lines in file

# 🔹 10. Exception Handling

# Try-Except example

# Handle ZeroDivisionError

# Custom exception

# 🔹 11. Python Logic / Output Questions

# Difference between == and is

# Mutable vs Immutable example

# Shallow vs Deep copy

# List comprehension example

# Generator example

# 🔹 12. Automation-Relevant Basics (Bonus ⭐)

# Read data from CSV file

# Read data from Excel (openpyxl)

# Wait using time.sleep()

# Count words in a string (real test case logic)

# Validate email using regex
