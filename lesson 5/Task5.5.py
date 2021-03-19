'''
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
 Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
'''

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list=[]
repeat_numbers={}

for a in range(len(src)):
    if src[a] not in repeat_numbers.keys():
        result_list.append(src[a])
        repeat_numbers[src[a]]=1
    elif repeat_numbers[src[a]]<=1:
        result_list.pop(result_list.index(src[a]))
        repeat_numbers[src[a]]=2

print(result_list)

