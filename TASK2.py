# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = [2, 0, 5, 6]
res_list = []
if len(my_list) % 2 == 0:
    for i in range(int(len(my_list)/2)):
        res_list.append(my_list[i]*my_list[len(my_list)-i-1])
    print(res_list)

else:
    for i in range(int(len(my_list)/2)+1):
        if i == (int(len(my_list)/2)+1):
            res_list.append(my_list[i]**2)
        else:
            res_list.append(my_list[i]*my_list[len(my_list)-i-1])
    print(res_list)
