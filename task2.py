print("Python-калькулятор Нечайко Поліни! Можливі оператори: +, -, *, /")
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
while True:
    oper = input("Введіть оператор: ")
    if oper in ('+', '-', '*', '/'):
        print("Введено: перше число: ", a, "; друге число: ", b, "; оператор: ", oper)
        break
    else:
        print("Помилка! Введіть дійсний оператор: ")