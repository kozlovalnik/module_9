
def is_prime(func):
    def wrapper(num1, num2, num3):
        result = func(num1, num2, num3)
        for i in range(result):
            if i > 1 and not result % i:
                print('Составное')
                return result
        print('Простое')
        return result
    return wrapper


@is_prime
def sum_three(num1, num2, num3):
    return num1 + num2 + num3

result = sum_three(2, 3, 6)
print(result)
