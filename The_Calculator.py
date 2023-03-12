def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

for o in operators:
    print(o)

symbol = input("Pick an operator from above: ")

calculation = operators[symbol]
answer = calculation(num1, num2)

print(f"{num1} {symbol} {num2} = {answer}")