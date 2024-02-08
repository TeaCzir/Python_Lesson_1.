# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные. Input: 5 -> 1 3 3 3 4  Output: 1 3 3 3 1

list_1 = [1, 4, 5, 3, 4, 3, 2]
l = ' '.join(map(str, list_1))

print(f'There are 7 ratings in the journal: {l}') 
size = 7
min = 0
max = 0
for i in range(size):
    if list_1[i] <= min:
        min = list_1[i]
   
    if list_1[i] >= max:
        max = list_1[i]

print([f'min = {min}, max = {max}'])
for i in range(size):
    c = 0
    if list_1[i] == max:
        c = i
        for j in range(size):
            list_1[c] = min
        print(list_1)  

# for i in range(size):
#     a = 0
#     if list_1[i] == min:
#         c = i
#         for j in range(size):
#             list_1[c] = max
#         print(list_1) 



