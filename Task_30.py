# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

# def arithmetic_progression(arr):
   
#     #d = arr[1] + arr[n] // (n - 1)
#     # a = int(input('Enter the first element'))
#     # n = int(input('Enter saze: '))
#     # d = int(input('Enter difference: '))
#     for n in range(arr[0], (arr[1] + arr[n] // (n - 1)), len(arr)):
#         #d = (arr[1] + arr[n] // (n - 1))
#         return arr
    
# arithmetic_progression([7, 2, 5])
# print(arithmetic_progression([7, 2, 5]))

a1 = 7
d = 2
n = 5
for i in range(n):
    print(a1 + i * d, end=' ')
        

