from collections import defaultdict

def create_frequency_list(arr):
    # создаем словарь с ключом - элементом массива, значением - счетчиком
    frequency_list = defaultdict(int)
    for item in arr:
        frequency_list[item] += 1

    print("List before pruning:")
    for key, value in frequency_list.items():
        print(f'{key}: {value}')

    # удаляем элементы со счетчиком не равным 1
    for key in list(frequency_list.keys()):
        if frequency_list[key] != 1:
            del frequency_list[key]
    print("List after pruning:")
    for key, value in frequency_list.items():
        print(f'{key}: {value}')

# Usage example
arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 6, 6]
create_frequency_list(arr)
