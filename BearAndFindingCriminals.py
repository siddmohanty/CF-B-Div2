k=list(map(int, input().split()))
n=k[0]
a=k[1]
s=list(map(int, input().split()))

s2=s[0:a]
s2=s2[::-1]
s3=s[a-1:]


count=0
if(s2[0]==1 and s3[0]==1):
    count=1
for i in range(1, min(len(s2),len(s3))):
    if(s2[i]==1 and s3[i]==1):
        count+=2
extra=[]
if(len(s2)>len(s3)):
    extra=s2[len(s3):]
if(len(s2)<len(s3)):
    extra=s3[len(s2):]
count+=extra.count(1)
print(count)
