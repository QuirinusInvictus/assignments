'''
Сортирует лист сравнивая значения соседних чисел и если левое больше правого, меняет их местами. Остановится после того как все числа отсортированы
'''
def bubble_sort(list):
    swap = False#отсортирован ли лист?
    while not swap:
        swap = True
        for j in range(1,len(list)):
            if list[j-1] > list[j]:# проверка
                swap = False
                temp = list[j-1]#Замена значений
                list[j] = list[j-1]
                list[j-1] = temp
