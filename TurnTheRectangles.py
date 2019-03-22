n=int(input())
r=[]
maxm=[]
minm=[]
flag=1
for i in range(0,n):
    s=input()
    s=list(s.split(' '))
    mxm=max(int(s[0]), int(s[1]))
    mnm=min(int(s[0]), int(s[1]))
    maxm.append(mxm)
    minm.append(mnm)

for i in range(0,n-1):
    if(maxm[i]<maxm[i+1]):
        maxm[i+1]=minm[i+1]
        if(maxm[i]<maxm[i+1]):
            flag=0
            break
        else:
            continue
    else:
        continue
if(flag==0):
    print("NO")
else:
    print("YES")