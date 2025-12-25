def asal_bulma_fonk(num):
    i=2
    if(num==2):
        return True
    else:
        while(i<num):
            if(num%i==0):
                return False
            else:
                i=i+1
        return True

def fonk_2(num):
    asal_list=[]
    j=2
    while(len(asal_list)<num):
        if(asal_bulma_fonk(j)==True):
            asal_list.append(j)
            j=j+1
        else:
            j=j+1
    a=asal_list[(num-1)]
    return a
b=10001
print(fonk_2(b))
