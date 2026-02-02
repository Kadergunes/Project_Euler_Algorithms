list_t=[]
total=1
list_a=[]

list_two=[1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20]

def bolenler(value):
    i=1
    while(i<=value):
        if(value%i==0):
            list_a.append(i)
            i=i+1
        else:
            i=i+1
    return list_a

for x in list_two:
    bolenler(x)

for y in list_a:
    if y not in list_t:
        list_t.append(y)

for a in list_t:
    total=total*a

print(list_t)
print("total:",total)








