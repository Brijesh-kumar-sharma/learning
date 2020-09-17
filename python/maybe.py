def solution(l):
    l.sort(reverse=True)
    if sum(l)%3==0:
        return ''.join(str(_) for _ in l)
    rem=sum(l)%3
    if rem==1:
        rem1=None
        rem2_1=None
        rem2_2=None
        for i in l[::-1]:
            if i%3==1:
                if rem1==None:
                    rem1=i
                else:
                    pass
            elif i%3==2:
                if rem2_1==None:
                    rem2_1=i
                elif rem2_2==None:
                    rem2_2=i
                else:
                    pass
            if rem1!=None and rem2_1!=None and rem2_2!=None:
                break
        if rem1!=None:
            m=list(l[::-1])
            m.remove(rem1)
            a1=int(''.join(str(_) for _ in sorted(m,reverse=True)))
        else:
            a1=0
        if rem2_1!=None and rem2_2!=None:
            n=list(l[::-1])
            print("n=",n,rem2_1,rem2_2)
            n.remove(rem2_1)
            n.remove(rem2_2)
            a2=int(''.join(str(_) for _ in sorted(n,reverse=True)))
        else:
            a2=0
        if a1>a2:
            return a1
        else:
            return a2
    rem1_1=None
    rem1_2=None
    rem2=None
    for i in l[::-1]:
        if i%3==2:
            if rem2==None:
                rem2=i
            else:
                pass
        elif i%3==1:
            if rem1_1==None:
                rem1_1=i
            elif rem1_2==None:
                rem1_2=i
            else:
                pass
        if rem2!=None and rem1_1!=None and rem1_2!=None:
            break
    if rem2!=None:
        m=list(l[::-1])
        m.remove(rem2)
        a1=int(''.join(str(_) for _ in sorted(m,reverse=True)))
    else:
        a1=0
    if rem1_1!=None and rem1_2!=None:
        n=list(l[::-1])
        n.remove(rem1_1)
        n.remove(rem1_2)
        a2=int(''.join(str(_) for _ in sorted(n,reverse=True)))
    else:
        a2=0
    if a1>a2:
        return a1
    else:
        return a2
l=[5,5]
s=solution(l)
print(s)
