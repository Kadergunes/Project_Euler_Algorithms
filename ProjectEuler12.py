import math
def divisor_finder(n):
    j = 0
    i = 1

    while i <= math.sqrt(n):
        if n % i == 0:
            j += 1
        i += 1

    if int(math.sqrt(n))**2 == n:
        return j*2 - 1
    else:
        return j*2


number=1
while True:
    x=(number*(number+1))/2
    if(divisor_finder(x))>500:
        print(x)
        break
    else:
        number=number+1






