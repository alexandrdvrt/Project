#калькулятор

from colorama import init
from colorama import Fore, Back, Style
init()

print ( Back.GREEN)

d = (input ( "Что делаем? (+, -): " ))
a = float( input("Введи первое число: ") )
b = float( input("Введи второе число: ") )

if d == '+':
    print("Результат: ", a+b)
    
elif d == '-':
    print("Результат: ", a-b)
    
else:
    print ("Такой операции нет")

input()
