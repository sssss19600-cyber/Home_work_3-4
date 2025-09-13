a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = a + b
    print("Result:", result)
elif operation == "-":
    result = a - b
    print("Result:", result)
elif operation == "*":
    result = a * b
    print("Result:", result)
elif operation == "/":
    if b == 0:
        print("Division by zero")
    else:
        result = a / b
        print("Result:", result)

#Простий калькулятор, сам робив