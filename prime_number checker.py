def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        else:
            return True
is_prime(2)
is_prime(3)
is_prime(4)
is_prime(5)
is_prime(6)
is_prime(7)

