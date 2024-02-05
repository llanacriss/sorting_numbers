import tkinter
from tkinter import ttk
from tkinter.messagebox import showerror
from timeit import default_timer as timer
from unittest import *

#Сортировка пузырьком
def bubble_sort(list):
    last_elem_index = len(list) - 1
    for passNo in range(last_elem_index, 0, -1):
        for i in range(passNo):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

#Сортировка подсчетом
def counting_sort(list, largest):
    c = [0]*(largest + 1)
    for i in range(len(list)):
        c[list[i]] = c[list[i]] + 1
    c[0] = c[0] - 1
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None]*len(list)
    for x in reversed(list):
        result[c[x]] = x
        c[x] = c[x] - 1
    return result

#Две функции для пирамидальной сортировки
#Функция преобразования в двоичную кучу
def heapify(list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and list[i] < list[left]:
        largest = left
    if right < n and list[largest] < list[right]:
        largest = right
    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, n, largest)

#Пирамидальная сортировка
def heap_sort(list):
    n = len(list)
    for i in range(n, -1, -1):
        heapify(list, n, i)
    for i in range(n -1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)
    return list

#Сортировка слиянием
def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)

        a = 0
        b = 0
        c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a += 1
            else:
                list[c] = right[b]
                b += 1
            c += 1
        while a < len(left):
            list[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            list[c] = right[b]
            b += 1
            c += 1
        return list

#Быстрая сортировка
def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i < pivot]
        greater = [i for i in list[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

#Поразрядная сортирока
def radix_sort(list):
    max_digit = max([len(str(num)) for num in list])
    radix = 10
    lists = [[] for i in range(radix)]
    for i in range(0, max_digit):
        for e in list:
            digit = (e // radix ** i) % radix
            lists[digit].append(e)
        list = [x for queue in lists for x in queue]
        lists = [[] for i in range(radix)]
    return list


#Действия, происходящие по нажатию кнопки "Start"
def click():
    try:
        my_list = [int(x) for x in entry.get().split(',')]
        m = max(my_list)
        if combobox.get() == 'Пузырьком':
            label['text'] = bubble_sort(my_list)
            start = timer()
            bubble_sort(my_list)
            end = timer()
            time_label['text'] = 1000000 * (end - start)
        elif combobox.get() == 'Подсчетом':
            warning_label = ttk.Label(
                text='Сортировка Подсчетом производит сортировку только \nдля натуральных чисел. \n'
                     'При применении данной сортировки для целых отрицательных \nчисел, результат сортировки '
                     'может быть некорректным.', foreground='red', borderwidth=2, relief="ridge", padding=8)
            warning_label.pack(anchor=tkinter.NW, padx=6, pady=6)
            label['text'] = counting_sort(my_list, m)
            start = timer()
            counting_sort(my_list, m)
            end = timer()
            time_label['text'] = 1000000 * (end - start)
        elif combobox.get() == 'Пирамидальная':
            label['text'] = heap_sort(my_list)
            start = timer()
            heap_sort(my_list)
            end = timer()
            time_label['text'] = 1000000 * (end - start)
        elif combobox.get() == 'Слиянием':
            label['text'] = merge_sort(my_list)
            start = timer()
            merge_sort(my_list)
            end = timer()
            time_label['text'] = 1000000 * (end - start)
        elif combobox.get() == 'Быстрая':
            label['text'] = quick_sort(my_list)
            start = timer()
            quick_sort(my_list)
            end = timer()
            time_label['text'] = 1000000 * (end - start)
        elif combobox.get() == 'Поразрядная':
            label['text'] = radix_sort(my_list)
            warning2_label = ttk.Label(
                text='Поразрядная сортировка производит сортировку только \nдля натуральных чисел. \n'
                     'При применении данной сортировки для целых отрицательных \nчисел, результат сортировки '
                     'может быть некорректным.', foreground='red', borderwidth=2, relief="ridge", padding=8)
            warning2_label.pack(anchor=tkinter.NW, padx=6, pady=6)
            start = timer()
            radix_sort(my_list)
            end = timer()
            time_label['text'] = 1000000 * (end - start)
    except:
        showerror(title='Ошибка', message='Необходимо ввести целые числа через запятую!')

window = tkinter.Tk()
window.title('Сортировка чисел')
window.geometry("450x450")

entry_label = ttk.Label(window, text='Введите целые числа через запятую: ')
entry_label.pack(anchor=tkinter.W, padx=8, pady=8)
entry = ttk.Entry(window)
entry.pack(anchor=tkinter.W, padx=8, pady=8)

sorting = ['Пузырьком', 'Подсчетом', 'Пирамидальная', 'Слиянием', 'Быстрая', 'Поразрядная']
combobox_label = ttk.Label(window, text='Выберите способ сортировки: ')
combobox_label.pack(anchor=tkinter.W, padx=8, pady=8)
combobox = ttk.Combobox(window, values=sorting)
combobox.pack(anchor=tkinter.W, padx=8, pady=8)

button = ttk.Button(window, text='Start', command=click)
button.pack(anchor=tkinter.W, padx=8, pady=8)

res_label = ttk.Label(text='Результат сортировки: ')
res_label.pack(anchor=tkinter.NW, padx=6, pady=6)
label = ttk.Label()
label.pack(anchor=tkinter.NW, padx=6, pady=6)

res2_label = ttk.Label(text='Время, затраченное на сортировку (в микросекундах): ')
res2_label.pack(anchor=tkinter.NW, padx=6, pady=6)
time_label = ttk.Label()
time_label.pack(anchor=tkinter.NW, padx=6, pady=6)

window.mainloop()

