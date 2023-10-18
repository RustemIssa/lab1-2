print(4, 8, 15, 16, 23, 42)

print("4\n8\n15\n16\n23\n46")

n1 = int(input("n1 = "))
n2 = n1 + 1
n3 = n1 + 2
print(n1)
print(n2)
print(n3)

b = int(input())
c = int(input())
d = int(input())
print(b + c + d)

a = int(input("a = "))
print(a*a*a)
print(a*a*6)

n = int(input("n = "))
k = int(input("k = "))
p = k // n
o = k % n
print(p)
print(o)


number = int(input("Enter a four-digit number: "))


thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10


print("The digit in the thousands position is", thousands)
print("The digit in the hundreds position is", hundreds)
print("The digit in the tens position is", tens)
print("The digit in the units position is", units)

people = int(input())

if people % 2 == 0:
    people = people
else:
    people = people + 1

print(people / 2)

num = int(input("Введите целое число: "))

num1 = num << 1

print(f"Результат побитового сдвига влево на один бит: {num1}")

if num1 == 0:
    print("Результат равен нулю.")

    num1 = float(input("Пожалуйста, введите первое число: "))
num2 = float(input("Пожалуйста, введите второе число: "))

operation = input("Пожалуйста, выберите операцию (+, -, *, /): ")

result = None
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Ошибка: деление на ноль.")
    else:
        result = num1 / num2
else:
    print("Ошибка: неверная операция.")

if result is not None:
    print(f"{num1} {operation} {num2} = {result:.3f}")
