s=list(map(int, input().split()))
l=s[0]
r=s[1]
x=s[2]
y=s[3]
def findgcd(a,b):
    M=max(a,b)
    m=min(a,b)
    while(m!=0):
        t=M%m
        M=m
        m=t
    return M

count=0
if(x!=y):
    if(True):
        prod=x*y
        a=[]
        for i in range(1,int(y**0.5)+1):
            if(y/i==int(y/i)):
                a.append(i)
                a.append(int(y/i))
        a=list(set(a))
        for i in a:
            b_i=prod/i
            if(int(b_i)==b_i):
                if(findgcd(b_i,i)==x and l<=i<=r and l<=b_i<=r):
                    count+=1
                else:
                    continue
if(x==y and l<=x<=r and l<=y<=r):
    count=1
print(count)