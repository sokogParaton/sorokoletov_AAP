# ЗАДАЧА 1
# Программа - это представление алгоритма;
# процесс - деятельность, связанная с выполнением программы;
# алгоритм - последовательность действий
#
#
# Задача 2
# 1) Приготовление еды по рецепту
# 2) Сбор на учебу с утра
# 3) Инструкция по сборке мебели
#
#
# Задача 3
# 1) Монет в кармане конечное число
# 2) Алгоритм не имеет конца, он зациклен

# Задача 4
# 1) O(log n)
# 2) O(n)
# 3) O(n)


# Задача 5
# 2048 элементов: просто за 2048 шагов, бинарный за 11
#
# Если увеличить в 2 раза, то за 4096, бинарный за 12

# Задача 6
def bin_search_one(a):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == 0:
            low = mid + 1
        if a[mid] == 1:
            if a[mid - 1] == 0:
                return mid
            else:
                high = mid - 1

def liner_search(a):
    for i in range(len(a)):
        if a[i] == 1:
            return i
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
print(bin_search_one(a))
print(liner_search(a))

# Задача 7
def first_x(a, x):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] < x:
            low = mid + 1
        elif a[mid] > x:
            high = mid - 1
        else:
            if mid == 0 or a[mid - 1] != x:
                return mid
            high = mid - 1
    return -1

def last_x(a, x):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] < x:
            low = mid + 1
        elif a[mid] > x:
            high = mid - 1
        else:
            if mid == len(a) - 1 or a[mid + 1] != x:
                return mid
            low = mid + 1
    return -1

def count_x(a, x):
    first = first_x(a, x)
    if first == -1:
        return 0
    return last_x(a, x) - first + 1

b = [1, 3, 5, 7, 9, 2, 4, 6, 8]

def first_even(b):
    low, high = 0, len(b) - 1
    while low <= high:
        mid = (low + high) // 2
        if b[mid] % 2 == 1:
            low = mid + 1
        else:
            if mid == 0 or b[mid - 1] % 2 == 1:
                return mid
            high = mid - 1
    return -1

print(first_even(b))


# Задача 8




