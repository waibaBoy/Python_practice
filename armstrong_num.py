def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(digit)** power for digit in digits)
    return total == n
print(is_armstrong(153))  # True
print(is_armstrong(123))  # False
print(is_armstrong(9474))  # True