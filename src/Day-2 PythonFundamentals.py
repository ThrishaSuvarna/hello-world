
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

op = input("Enter operation (+, -, *, /): ")

match op:
    case '+':
        print("Result:", num1 + num2)
    case '-':
        print("Result:", num1 - num2)
    case '*':
        print("Result:", num1 * num2)
    case '/':
        if b != 0:
            print("Result:", num1 / num2)
        else:
            print("Division by zero not allowed")
    case _:
        print("Invalid operation")
#precedence
name=input("Enter your name: ")
print("Good Morning " +name+ "!")

#fstring
name = "Thrisha"
age = 21
print(f"My name is {name} and I am {age} years old.")







