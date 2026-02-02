import math

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.sqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

total = 0
for num in range(2, 2_000_000):
    if is_prime(num):
        total += num

print(total)
