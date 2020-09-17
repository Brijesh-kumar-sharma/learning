list=[1,2,2,3,3,3,4,5,5]

count=0
n=int(input())

for i in range(1,10):
    for x in list:
        if(x==i):
            count+=1
    print("x=",count)        
    if(count>n):
        for x in range(count):
            list.remove(i)
    count=0
print(*list,sep=' ')
