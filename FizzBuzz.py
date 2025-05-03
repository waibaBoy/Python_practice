import random


def fizzbuzz(limit = 100):
    result_list = []
    for num in range (1, limit + 1):
        if num % 3 == 0 and num % 5 == 0:
            result_list.append('FizzBuzz')
        elif num % 5 == 0:
            result_list.append('Buzz')
        elif num % 3 == 0:
            result_list.append('Fizz')
        else:   
            result_list.append(num)
    return result_list

print(fizzbuzz(15))
# fizzbuzz(15)
#     print(result_list)
# fizzbuzz()