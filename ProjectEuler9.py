for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if c > b:  # a < b < c şartı
            if a*a + b*b == c*c:
                print("a =", a, "b =", b, "c =", c)
                print("a*b*c =", a * b * c)
                break
