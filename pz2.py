import numpy as np

# ЗАДАЧА 1
# Функция просто один раз выводит строку, циклов нет
# O(1)


# Задача 2
# Первый цикл проходит по всему списку - O(n)
# Второй цикл тоже n раз, обращение по индексу - O(1)
# Циклы идут друг за другом -> закон сложения
# O(n)


# Задача 3
# O(n^2)


# Задача 4
# 1) минимум во всём массиве - 3, меняем с 6-ю -> [3, 12, 4, 6, 8]
# 2)  минимум в [12, 4, 6, 8] - 4, меняем с 12 -> [3, 4, 12, 6, 8]
# 3) минимум в [12, 6, 8] - 6, меняем с 12 -> [3, 4, 6, 12, 8]
# 4) минимум в [12, 8] - 8, меняем с 12 -> [3, 4, 6, 8, 12]
# Остался один элемент 12, и он уже на месте

a = [6, 12, 4, 3, 8]

from random import *



for i in range(1000):
    a.append(randint(1, 100))

def selection_sort_for(arr):
    a = arr.copy()
    for i in range(len(a) - 1):
        min_i = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
    return a

def selection_sort_while(arr):
    a = arr.copy()
    i = 0
    while i < len(a) - 1:
        min_i = i
        j = i + 1
        while j < len(a):
            if a[j] < a[min_i]:
                min_i = j
            j += 1
        a[i], a[min_i] = a[min_i], a[i]
        i += 1
    return a

def find_smallest(a):
    smallest_i = 0
    for i in range(1, len(a)):
        if a[i] < a[smallest_i]:
            smallest_i = i
    return smallest_i

def selection_sort_2arr(arr):
    a = arr.copy()
    new_a = []
    for i in range(len(a)):
        smallest_i = find_smallest(a)
        new_a.append(a.pop(smallest_i))
    return new_a

def selection_sort_1arr(arr):
    a = arr.copy()
    for i in range(len(a) - 1):
        min_i = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_i]:
                min_i = j
        if min_i != i:
            a[i], a[min_i] = a[min_i], a[i]
    return a

print(selection_sort_for(a))
print(selection_sort_while(a))
print(selection_sort_2arr(a))
print(selection_sort_1arr(a))


# Задача 5
# Простое описание, a = [6, 12, 4, 3, 8]
# 1) 6>12? нет; 12>4? да, меняем; 12>3? да; 12>8? да -> [6, 4, 3, 8, 12]
# 2) 6>4? да; 6>3? да; 6>8? нет -> [4, 3, 6, 8, 12]
# 3) 4>3? да; 4>6? нет -> [3, 4, 6, 8, 12]
# 4) 3>4? нет -> [3, 4, 6, 8, 12]
# Всего n-1 = 4 прохода

def bubble_sort_for(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def bubble_sort_while(arr):
    a = arr.copy()
    n = len(a)
    swapped = True
    i = 0
    while swapped:
        swapped = False
        j = 0
        while j < n - 1 - i:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
            j += 1
        i += 1
    return a

print(bubble_sort_for(a))
print(bubble_sort_while(a))


# Задача 6
def selection_sort_v(arr, verbose=False):
    a = arr.copy()
    steps = 0
    if verbose:
        print('Исходный массив:', a)
    for i in range(len(a) - 1):
        min_i = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
        steps += 1
        if verbose:
            print('Шаг', steps, ':', a)
    print('Шагов потребовалось:', steps)
    print('Отсортированный массив:', a)
    return a

def bubble_sort_v(arr, verbose=False):
    a = arr.copy()
    n = len(a)
    steps = 0
    swapped = True
    if verbose:
        print('Исходный массив:', a)
    while swapped:
        swapped = False
        j = 0
        while j < n - 1 - steps:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
            j += 1
        steps += 1
        if verbose:
            print('Шаг', steps, ':', a)
    print('Шагов потребовалось:', steps)
    print('Отсортированный массив:', a)
    return a

selection_sort_v(a, verbose=True)
bubble_sort_v(a, verbose=True)


print("\n ____________________")
# Задача 7
# reverse=False - по возрастанию, reverse=True - по убыванию
def selection_sort(arr, verbose=False, reverse=False):
    a = arr.copy()
    steps = 0
    if verbose:
        print('Исходный массив:', a)
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            if reverse:
                if a[j] > a[m]:
                    m = j
            else:
                if a[j] < a[m]:
                    m = j
        a[i], a[m] = a[m], a[i]
        steps += 1
        if verbose:
            print('Шаг', steps, ':', a)
    print('Шагов потребовалось:', steps)
    print('Отсортированный массив:', a)
    return a

def bubble_sort(arr, verbose=False, reverse=False):
    a = arr.copy()
    n = len(a)
    steps = 0
    swapped = True
    if verbose:
        print('Исходный массив:', a)
    while swapped:
        swapped = False
        j = 0
        while j < n - 1 - steps:
            if reverse:
                need_swap = a[j] < a[j + 1]
            else:
                need_swap = a[j] > a[j + 1]
            if need_swap:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
            j += 1
        steps += 1
        if verbose:
            print('Шаг', steps, ':', a)
    print('Шагов потребовалось:', steps)
    print('Отсортированный массив:', a)
    return a

selection_sort(a, verbose=True, reverse=True)
bubble_sort(a, verbose=True, reverse=True)


print("\n ____________________")
# Задача 8
a20 = np.random.randint(0, 100, 20).tolist()
a50 = np.random.randint(0, 100, 50).tolist()

print('--- 20 элементов ---')
print(selection_sort(a20) == sorted(a20))
print(bubble_sort(a20) == sorted(a20))
print(selection_sort(a20, reverse=True) == sorted(a20, reverse=True))
print(bubble_sort(a20, reverse=True) == sorted(a20, reverse=True))

print('--- 50 элементов ---')
print(selection_sort(a50) == sorted(a50))
print(bubble_sort(a50) == sorted(a50))
print(selection_sort(a50, reverse=True) == sorted(a50, reverse=True))
print(bubble_sort(a50, reverse=True) == sorted(a50, reverse=True))


# Задача 9
def bin_search(a, x):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        if a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

L1 = np.sort(np.random.randint(0, 101, 50)).tolist()  # просто готовлю отсортированные данные
print(L1)
print(bin_search(L1, 10))


# Задача 10
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

L1 = np.random.randint(0, 101, 50).tolist()
print(L1)
print(linear_search(L1, 10))


# Задача 11
def find_min(a):
    m = a[0]
    for el in a:
        if el < m:
            m = el
    return m

def find_max(a):
    m = a[0]
    for el in a:
        if el > m:
            m = el
    return m

L1 = np.random.randint(0, 101, 50).tolist()
print(L1)
print(L1[0])
print(find_min(L1))
print(find_max(L1))
print(linear_search(L1, 10))

