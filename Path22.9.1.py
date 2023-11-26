array = list(map(int, input("Введите целые числа в любом порядке, через пробел: ").split()))
element = int(input("Введите любое положительное целое число в диапазоне полученного списка: "))
import random
def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:

            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)
        return array
print(qsort_random(array, 0,len(array) - 1))
def binary_search(array, element, left, right):
    if left > right:
            return False
    middle = (right + left) // 2
    if array[middle - 1] < element and element <= array[middle]:
        return [middle]
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    elif element == array[middle - 1]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
left = int(array[0])
right = int(array[-1])
if element < left or element > right:
    print('Числа нет в диапазоне списка')
else:
    print(binary_search(array, element, 0, len(array) - 1))

