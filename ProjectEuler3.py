num=600851475143
mul_numb=2
mul_list=[]
largest_prime = 0

while(num>=mul_numb):
    if(num%mul_numb==0):
        mul_list.append(mul_numb)
        mul_numb=mul_numb+1
    else:
        mul_numb=mul_numb+1

for x in mul_list:
    if(x==2):
        largest_prime=2

    i=2
    j=0
    while(x>i):
        if(x%i==0):
            j=j+1
            i=i+1
        else:
            i=i+1
    if(j==0 and x>largest_prime):
        largest_prime=x
print(largest_prime)