def sum_even_indices_times_last(arr):
    if not arr:  # Если массив пуст
        return 0
    sum_even = sum(arr[::2])  # Сумма элементов с чётными индексами
    last_element = arr[-1]  # Последний элемент
    return sum_even * last_element


print(sum_even_indices_times_last([0, 1, 2, 3, 4, 5]))
print(sum_even_indices_times_last([1, 3, 5]))
print(sum_even_indices_times_last([6]))
print(sum_even_indices_times_last([]))