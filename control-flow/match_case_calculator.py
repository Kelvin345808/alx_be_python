# prompt the user to enter the two numbers 
num1 = float(input("enter the first number:")) 
num2 = float(input("enter the second number:")) 

# ask the user the operation to perform
operation = input("Choose the operation (+, -, *, /): ") 

# perform calculations using match case 
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")