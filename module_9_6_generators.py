''' Функция генерации всех подстрок заданной строки '''

def all_variants(text: str):
    for cur_len in range(len(text)):
        for i in range(len(text) - cur_len):
            yield text[i: i + cur_len + 1]

a = all_variants("abc")

for i in a:
    print(i)
