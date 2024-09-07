a=[7,3,2]
t=18
p=[]
for i in range(len(a)):
    j=1
    k=0
    l=[]
    while(k<len(a)):
        if a[i]==t:
            l.append(a[i])
            p.append(l)
            break
        elif (a[i]*j)+a[k] < t:
            j+=1
        elif (a[i]*j)+a[k] == t:
            l=[a[i]]*j
            l.append(a[k])
            l.sort()
            if l not in p:
                p.append(l)
            l=[]
            j=1
            k+=1
        else:
            k+=1
            j=1
print(p)
    