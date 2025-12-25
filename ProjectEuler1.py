number=0
total=0
list=[]

while(number<1000):

    if(number%3==0 or number%5==0):
        list.append(number)
        total+=number
        number=number+1
    else:
        number=number+1
print(total)



