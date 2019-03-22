import collections
s=list(map(int,input().split()))
n=s[0]
m=s[1]
mydict={}
arrofsize=[]
arrofwts=[]
for i in range(m):
    t=input().split()
    arrofsize.append(int(t[0]))
    arrofwts.append(int(t[1]))
arrofwts2=list(set(arrofwts))
for i in arrofwts2:
    counts=0
    for j in range(0,len(arrofwts)):
        if(i==arrofwts[j]):
            counts+=arrofsize[j]
    mydict[i]=counts

    
size=list(mydict.values())
wt=list(mydict.keys())
arr=sorted(mydict.items())
count=0
i=len(wt)-1
while(i>=0):
    w1=arr[i][0]
    s1=arr[i][1]
    if(n>=s1):
        count=count+(s1*w1)
        n=n-s1
        
    elif(n<s1):
        count=count+(n*w1)
        n=n-n
    i=i-1
print(count)