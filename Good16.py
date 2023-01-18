def check_brackets(formula, index, open_count, close_count):
    # Проверка конца формулы
    if index == len(formula):
        if open_count == close_count:
            print("Matching brackets!")
        else:
            print("Unmatched bracket at index: ", index - 1)
        return
    # Проверка на открывающую скобку
    if formula[index] == "(":
        open_count += 1
    # Проверка на закрывающую скобку
    elif formula[index] == ")":
        if open_count > close_count:
            close_count += 1
        else:
            print("Unmatched bracket at index: ", index)
            return
    # Рекурсивный вызов функции с обновленными значениями
    check_brackets(formula, index + 1, open_count, close_count)

formula = "2*(3+4)*)(5-6)"
check_brackets(formula, 0, 0, 0)
