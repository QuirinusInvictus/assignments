'''
Возвращает отсортированный лист
'''
def merge_sort(list):
    def merge(left,right):#Сравнивает 2 отсортированных листа и соеденяет их вместе по возрастанию
        result = []
        i, j = 0, 0#сколько ушло из правого и левого листа
        while i < len(left) and j < len(right):#сравниваем значения и добавляем наименьший из них в результат
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):#Если левый лист был больше добавляем оставшиеся значения в конец
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result
    def sort(list):#рекурсивно делим лист пополам до еденичных листов, затем поочерёдно соединяем
        if len(list)<2:#Базовый случай
            return list[:]
        else:
            middle = len(list)//2#Ищем середину
            left = sort(list[:middle])#создаём левый лист
            right = sort(list[middle:])#Создаём правый
            return merge(left, right)#соединяем првый и левый
    return sort(list)
