n=int(input())
s=input()
s=list(s)
s2=['']*n
s=s[::-1]
i=0
while(len(s)>=1):
    s2[i]=s.pop(0)
    if(len(s)==0):
        break
    s2[n-i-1]=s.pop(0)
    if(len(s)==0):
        break
    i=i+1
    
print("".join(s2[::-1]))