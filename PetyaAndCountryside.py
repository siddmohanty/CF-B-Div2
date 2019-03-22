n=int(input())
arr=list(map(int, input().split()))
def findslopes(array, ind):
    c=0
    for i in range(ind, n-1):
        if(arr[i]>=arr[i+1]):
            c=c+1
        else:
            break
    for i in range(ind,0,-1):
        if(arr[i-1]<=arr[i]):
            c=c+1
        else:
            break
    return c+1

brr=[]
for i in range(0,len(arr)):
    brr.append(findslopes(arr,i))
brr.append(0)
print(max(brr))