# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные. Input: 5 -> 1 3 3 3 4  Output: 1 3 3 3 1

from random import randint

size = int(input("Введите колличество оценок в журнале: "))
list_1 = [randint(1, 5)]

# 1 Вариант.

min_num = list_1[0]
max_num = list_1[0]
i_max_num = [0]

for i in range(size - 1):
    num = randint(1, 5)
    list_1.append(num)
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
        i_max_num = [i + 1]
    elif num == max_num:
        i_max_num.append(i + 1)
print(list_1)        
for i in i_max_num:
    list_1[i] = min_num

print(list_1)
   
# 2 Вариант.

# list_1 = [randint(1, 5) for _ in range(size)]
# print(list_1)

# min_num = min(list_1)
# max_num = max(list_1)
# for i in range(len(list_1)):
#     if list_1[i] == max_num:
#         list_1[i] = min_num

# while max_num in list_1:
#     i_max_num = list_1.index(max_num)
#     list_1[i_max_num] = min_num
    
#print(list_1)




