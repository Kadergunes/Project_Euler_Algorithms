def fonk(numb):
    t1=0
    t2=0
    i=0
    while(i<=numb):
        t1=t1+(pow(i,2))
        t2=t2+i
        i=i+1
    return((pow(t2,2))-t1)

print("fark:",fonk(100))




