from sys import maxsize

mindiff=maxsize+1
ans=""

def solve(arr, vidx, set1, set2, sos1, sos2):
    global mindiff, ans
    if(vidx==len(arr)):
        delta=abs(sos1-sos2)
        if(delta<mindiff):
            mindiff=delta
            sum1=sum(set1)
            sum2=sum(set2)
            if(sum1>sum2):
                sum1, sum2=sum2, sum1
            ans=str(sum1)+" "+str(sum2)
        return
    
    if(len(set1)<(len(arr)+1)//2):
        set1.append(arr[vidx])
        solve(arr, vidx+1, set1, set2, sos1+arr[vidx], sos2)
        set1.pop(len(set1)-1)
    
    if(len(set2)<(len(arr)+1)//2):
        set2.append(arr[vidx])
        solve(arr, vidx+1, set1, set2, sos1, sos2+arr[vidx])
        set2.pop(len(set2)-1)   

t=int(input())
for z in range(t):
    temp=input()
    arr=[]
    n=int(input())
    for k in range(n):
        x=int(input())
        arr.append(x)
    ta1=[]
    ta2=[]
    solve(arr, 0, ta1, ta2, 0, 0)
    print(ans)
    mindiff=maxsize+1
    ans=""
    
'''
input :

2

11
23
45
-34
12
0
98
-99
4
189
-1
4

6
1
2
3
4
5
6

output:

120 121
10 11
'''