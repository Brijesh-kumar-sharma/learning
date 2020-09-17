def solution(n):
    s=[]
    s.append(l[n+1])
    s.append(l[n+2])
    s.append(l[n+3])
    s.append(l[n+4])
    s.append(l[n+5])
    return s





def concatenate(l):
        result=''
        for element in l:
            result+=str(element)
        return result


def nextPrime(num):
    while True:
        num+=1
        for i in range(2,num):
            if num%i==0:
                break
        else:
            return num


def primeProducer(N):
    num,count=1,1
    while count<=N:
        num=nextPrime(num)
        yield num
        count+=1

N=4000
list=[x for x in primeProducer(N)]


print(list)

l=[]
for x in list:
    if(x>=10 and x<100):
        m=x%10
        x=x-m
        n=x//10
        l.append(n)
        l.append(m)
    elif(x>=100 and x<1000):
        m=x%10
        n=x//10
        o=n%10
        n=n-o
        n=n//10
        l.append(n)
        l.append(o)
        l.append(m)


    elif(x>=1000 and x<10000):
        y=x%10
        x=x//10
        m=x%10
        n=x//10
        o=n%10
        n=n-o
        n=n//10
        l.append(n)
        l.append(o)
        l.append(m)
        l.append(y)

    elif(x>=10000 and x<100000):
        z=x%10
        x=x//10
        y=x%10
        x=x//10
        m=x%10
        n=x//10
        o=n%10
        n=n-o
        n=n//10
        l.append(n)
        l.append(o)
        l.append(m)
        l.append(y)
        l.append(z)
    elif(x>=100000 and x<1000000):
        w=x%10
        x=x//10
        z=x%10
        x=x//10
        y=x%10
        x=x//10
        m=x%10
        n=x//10
        o=n%10
        n=n-o
        n=n//10
        l.append(n)
        l.append(o)
        l.append(m)
        l.append(y)
        l.append(z)
        l.append(w)
    elif(x>=1000000 and x<10000000):
        k=x%10
        x=x//10
        w=x%10
        x=x//10
        z=x%10
        x=x//10
        y=x%10
        x=x//10
        m=x%10
        n=x//10
        o=n%10
        n=n-o
        n=n//10
        l.append(n)
        l.append(o)
        l.append(m)
        l.append(y)
        l.append(z)
        l.append(w)
        l.append(k)

    elif(x>=10000000 and x<100000000):
        a=x%10
        x=x//10
        k=x%10
        x=x//10
        w=x%10
        x=x//10
        z=x%10
        x=x//10
        y=x%10
        x=x//10
        m=x%10
        n=x//10
        o=n%10
        n=n-o
        n=n//10
        l.append(n)
        l.append(o)
        l.append(m)
        l.append(y)
        l.append(z)
        l.append(w)
        l.append(k)
        l.append(a)
    elif(x>=100000000 and x<1000000000):
        b=x%10
        x=x//10
        a=x%10
        x=x//10
        k=x%10
        x=x//10
        w=x%10
        x=x//10
        z=x%10
        x=x//10
        y=x%10
        x=x//10
        m=x%10
        n=x//10
        o=n%10
        n=n-o
        n=n//10
        l.append(n)
        l.append(o)
        l.append(m)
        l.append(y)
        l.append(z)
        l.append(w)
        l.append(k)
        l.append(a)
        l.append(b)


   
        


        
    else:
        l.append(x)



print(l)
n=int(input())
n=n-1


#print("main output")
so=solution(n)
print(concatenate(l))


print(so)
print(concatenate(so))





        
        


        




