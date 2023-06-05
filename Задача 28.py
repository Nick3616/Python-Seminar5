# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 
def recurs(a, b, c = 0):
    if a == 0:
        if b == 0:
            return c
        return  recurs(a, b - 1, c + 1)
    return  recurs(a - 1, b, c + 1)        

a = int(input("Введите число: "))
b = int(input("Введите число: "))
result = recurs(a, b)
print (result)