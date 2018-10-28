def arithmetic (argument1, argument2, operation):
    if operation == "+":
        return argument1 + argument2
    elif operation == "-":
        return argument1 - argument2
    elif operation == "*":
        return argument1 * argument2
    elif operation == "/":
        return argument1 / argument2
    else:
        return "Неизвестный оператор"

argument1 = int(input())
argument2 = int(input())
operation = input()

answer = arithmetic(argument1,argument2,operation)

print(answer)