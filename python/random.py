

def result(N):
    for num in range(N):
        if num%3==0:
            l2.append(num)
        else:
            pass
def concatenate(l):
        result=''
        for element in l:
            result+=str(element)
        return result

l2=[]
l=[3,1,1]
sorted(l)
N=int(concatenate(l))


result(N)
print(l2)
le=len(l2)
print(le)      
for i in range(1,le):
    if  (1 in l2):
        print(l2[i])
   
