def is_palindrome(n):
    return str(n) == str(n)[::-1]

largest = 0
a = b = 0#carapnalar icin

for i in range(100, 1000):
    for j in range(i, 1000):  #  gereksiz tekrarlar
        product = i * j
        if is_palindrome(product) and product > largest:
            largest = product
            a, b = i, j

print("En büyük palindrom:", largest)
print("Çarpanlar:", a, "x", b)


