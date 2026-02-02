import math
def divisor_finder(n):
   j=0
   i=1
   divisor=[]
   final_divisor=[]
   while(i<=math.sqrt(n)):
        if(n%i==0):
            i=i+1
            #j=j+1
            divisor.append(i)
        else:
            i=i+1
   for x in divisor:
       if x not in final_divisor:
           final_divisor.append(x)
           j=j+1
   return j



   #return (j*2)#

number=1
#while True:
#    x=(number*(number+1))/2
#    if(divisor_finder(x))>500:
        #print(number)
#        print(x)
#        break
#    else:
#        number=number+1


print(divisor_finder(16))



