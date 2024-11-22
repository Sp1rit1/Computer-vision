import random
import  time

def bubble_sort(arr, sorting_order):
  for i in range(len(arr)):
    is_swapped = False
    for j in range(0, len(arr)-i-1):
      if (arr[j] > arr[j+1] and sorting_order == '+') or (arr[j] < arr[j+1] and sorting_order == '-'):
        is_swapped = True
        arr[j], arr[j+1] = arr[j+1], arr[j]
    if not is_swapped:
        break
  return arr


def gnome_sort(arr, sorting_order):
    index = 0
    while index < len(arr):
        if index == 0 or (arr[index] >= arr[index - 1] and sorting_order == '+') or (arr[index] <= arr[index - 1] and sorting_order == '-') :
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr

def sort_time(arr, type):
    start_sort_time = time.time()
    if (type == "bubble"):
        bubble_sort(arr, '+')
    elif (type == "gnome"):
        gnome_sort(arr, '+')
    else:
        print("Не указан тип сортировки")
    end_sort_time = time.time()
    return  end_sort_time - start_sort_time


array1 = [random.randint(1, 100) for _ in range(20)]
print("\n\nИсходный массив: \n", array1, "\n\n")
array2 = array1[:]

print("Результаты пузырьковой сортировки:\n")
print("\tОтсортированный массив:\n",bubble_sort(array1, '+'), '\n')
print("\tВремя сортировки: ", sort_time(array1, "bubble"), "\n\n")

print("Результаты гномьей сортировки:\n")
print("\tОтсортированный массив:\n",gnome_sort(array2, '+'), '\n')
print("\tВремя сортировки: ",sort_time(array2, "gnome"), "\n\n\n")

big_array1 = [random.randint(1, 100) for _ in range(10000)]
big_array2 = big_array1[:]
print("Проверка массива с 10 000 элементов: \n")
print("\tВремя пузырьковой сортировки: ", sort_time(big_array1, "bubble"), "\n")
print("\tВремя гномьей сортировки: ", sort_time(big_array2, "gnome"), "\n")
