# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random

n=int(input("Сколько кустов (размер списка)?: "))
list_1=[random.randint(1,10) for i in range(n)]
print(list_1)
if (list_1[-2]+list_1[-1]+list_1[0])>(list_1[-1]+list_1[0]+list_1[1]):
    max=list_1[-2]+list_1[-1]+list_1[0]
else: max=list_1[-1]+list_1[0]+list_1[1]

for i in range(len(list_1[:-2])):
    if (list_1[i]+list_1[i+1]+list_1[i+2])>max:
        max=list_1[i]+list_1[i+1]+list_1[i+2]
print(max)




