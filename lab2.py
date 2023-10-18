number = int(input("Enter a four-digit number: "))
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10
if thousands + units == (tens - hundreds):
    print("YES")
else:
    print("NO")



age = int(input("Enter your age:\n "))
if age >= 18:
    print("Access allowed")
else:
    print("Access denied")



a = int(input("arithmetic progression:\n"))
b = int(input())
c = int(input())
if b - a == c - b:
    print("YES")
else:
    print("NO")


   
x1 = int(input("positions of rook:\n"))
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")



x1 = int(input("position of king:\n"))
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = (x2 - x1)
dy = (y2 - y1)
if dx <= 1 and dy <= 1:
    print("YES")
else:
    print("NO")


a = int(input("average number:\n"))
b = int(input())
c = int(input())
largest = max(a, b, c)
smallest = min(a, b, c)
middle = (a + b + c)/2 
print(middle)



month = int(input("month\n"))
days_in_month = {
    1: 31,  
    2: 28,  
    3: 31,  
    4: 30,  
    5: 31,  
    6: 30,  
    7: 31,  
    8: 31,  
    9: 30,  
    10: 31,  
    11: 30,  
    12: 31,  
}
if month in days_in_month:
    print(days_in_month[month])
else:
    print("Invalid month number\n")



weight = int(input("weight"))
if weight <= 60:
    print("Light weight")
elif weight <= 64:
    print("First welterweight")
elif weight <= 69:
    print("Welterweight")
else:
    print("Unknown category")




password = input("password\n")
confirmation = input()
if password == confirmation:
    print("Password accepted")
else:
    print("Password not accepted")



number = int(input("odd or even:\n"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")



a = int(input("smallest number\n"))
b = int(input())
if a < b:
    smallest = a
else:
    smallest = b
print(smallest)



age = int(input("age group\n"))
if age<=13:
    a="none"
    a=("childhood")
elif 14<=age<=24:
    a=("youth")
elif 25<=age<=59:
    a=("maturity")
else:
    a=("old age")
print(a)



a = int(input("triangle view\n"))
b = int(input())
c = int(input())
if a == b == c:
    triangle_type = "Equilateral"
elif a == b or b == c or c == a:
    triangle_type = "Isosceles"
else:
    triangle_type = "Versatile"
print(triangle_type)

