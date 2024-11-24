first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(first_str) - len(second_str) for (first_str, second_str) in zip(first, second) if
                len(first_str) != len(second_str))

second_result = (len(first_str) == len(second_str) for i in range(min(len(first), len(second))) if
                 (first_str := first[i]) and (second_str := second[i]))

print(list(first_result))
print(list(second_result))
