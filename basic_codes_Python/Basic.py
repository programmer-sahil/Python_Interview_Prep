# check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")





# Find Maximum of Three Numbers
a = 10
b = 25
c = 7
print("Maximum is:", max(a, b, c))



# Basic Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("Invalid operator")



# Print 1-10 using for loop

for i in range(1, 11):
    print(i)



# Factorial of a Number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)



# Reverse of a String

text = input("Enter a string: ")
print("Reversed:", text[::-1])


# Check for palindrome

text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


# Sum of Elements in a List
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))
