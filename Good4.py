# Начальный список
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("Начальный список : " + str(test_list))
 
res = [] # создаем пустой список
[res.append(x) for x in test_list if x not in res] # добавляем в список только уникальные элементы
 
# выводим список после удаления дубликатов
print ("The list after removing duplicates : " + str(res))
