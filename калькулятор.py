def add(num1, num2):
    return num1+num2

def diff(num1, num2):
    return num1-num2, num2-num1
    
def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2, num2/num1

def sq(num1, num2):
    return num1**num2

print(''' Выберите действие: 
      1 - сложение
      2 - вычитание
      3 - умножение
      4 - деление
      5 - возведение в степень
      ''')

giv = int(input("Выберите операцию от 1 до 5: "))

num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))

if giv == 1:
    print(add(num1, num2))
elif giv == 2:
    print(diff(num1, num2))
elif giv == 3:
    print(mul(num1, num2))
elif giv == 4:
    print(div(num1, num2))
elif giv == 5:
    print(sq(num1, num2))
else :
    print("Нет такой функции")
    