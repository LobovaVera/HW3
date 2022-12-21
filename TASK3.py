# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Решение подходит только для вещественных чисел, у которых после запятой не более 10 цифр
# Кирилл, как решить такую задачу для любого вещественного числа? :'(  это ужасно, что питон делает с вещественными числами при любой операции - я в панике и отчаянии
your_list = [1.1, 2451.2, 3.1, 5, 10.0001]
temp =0
our_list = []
temp_list = []
for i in range(len(your_list)):
    temp = int(your_list[i])
    print(temp)
    temp_list.append(your_list[i]-temp)
    print(temp_list)
    if temp_list[i] !=0:
        our_list.append(round((temp_list[i]), 10))

print(our_list)

#find min and max
maxx = 0

for el in our_list:
    if el > maxx:
        maxx = el
minn = maxx
for el in our_list:
    if el < minn:
        minn = el
print(round((maxx-minn), 10))
