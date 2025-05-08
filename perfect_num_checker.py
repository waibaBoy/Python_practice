def is_perferct(n):
    digits = str(n)
    total = 0
    for i in range(1, n):
        if n % i  == 0:
            total+= i
    return total == n
print(is_perferct(6))  # True
print(is_perferct(28))  # True
print(is_perferct(12))  # False