""" Применение списка функций к списку чисел """


def apply_all_func(int_list: list[int], *functions: list) -> dict:
    res_dict = {}
    for f in functions:
        res_dict[f.__name__] = f(int_list)
    return res_dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
