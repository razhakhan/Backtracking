def prints(arr,s,n):
    l=[]
    for i in range(s,n):
        l.append(arr[i])
    print(*l)
    return
    
def permutation(arr, s, n):
    if(s==n):
        prints(arr,0,n)
    for i in range(s, n):
        arr[i], arr[s] = arr[s], arr[i]
        permutation(arr, s+1, n)
        arr[i], arr[s]=arr[s], arr[i]
        
arr=[1,2,3]
n=len(arr)
permutation(arr,0,n)
