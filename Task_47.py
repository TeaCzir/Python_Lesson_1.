# Задача №47. 1) У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите 
# ничего сломать): transformation = <???> values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  или любой другой список transormed_values = list(map(transformation, 
# values)) Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation. Однако вы поняли, что для вашей текущей 
# задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть. Напишите такое лямбда-выражение transformation, 
# чтобы transformed_values получился копией values. 2) Есть код: transformation = <???> values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой 
# список transformed_values = list(map(transformation, values)) if values == transformed_values: print(‘ok’) else: print(‘fail’) - В переменную 
# transformation нужно прописать такую функцию, что бы в переменной transformed_values получилась копия списка values
transformation = lambda x: x values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] 
# или любой другой список transformed_values = list(map(transformation, values)) 
# if values == transformed_values: print('ok') else: print('fail')

# def noname(x, y): # return x * y noname(2,3) f = lambda x, y: x * y

my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2] 
res_list = filter(lambda x: x % 2 == 0, my_list) 
print(res_list) 
print(list(res_list)) 
res_list=[] 
f = lambda x: x % 2 == 0 
for el in my_list: 
    if f(el): 
        res_list.append(el) 
        print(res_list)

my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2] 
# res_list = filter(lambda x: x % 2 == 0, my_list) 
# # print(res_list) 
# # print(list(res_list)) 
# # res_list=[] 
# # f = lambda x: x % 2 == 0 
# # for el in my_list: # if f(el): 
# # res_list.append(el) # print(res_list) 
# # f = lambda x: x % 2 == 0 
# # res_list = [el for el in my_list if f(el)] 
# # print(res_list)

my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2] 
# res_list = map(lambda x: x ** 2 , my_list) 
# # print(res_list) # print(list(res_list)) 
# #1 res_list = list(map(lambda x: x % 2 == 0, my_list)) 
# print(res_list) 
# #2 res_list=[] 
# f = lambda x: x % 2 == 0 
# for el in my_list: res_list.append(f(el)) 
# print(res_list) 
# #3 f = lambda x: x % 2 == 0 
# res_list = [f(el) 
# for el in my_list] 
# print(res_list)


var2 = '10 8 3 5 7 9' 
var3 = '10 3 8 4 5' 
str_1 = list(map(int,var2.split())) 
str_2 = list(map(int,var3.split())) 
list_1 = set(str_1) 
list_2 = set(str_2) 
list_3 = list_1.intersection(list_2) #list_3.sort() print(*sorted(list_3))


