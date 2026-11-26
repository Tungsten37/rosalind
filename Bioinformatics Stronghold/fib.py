def f(k,n1,n2):
    return n1*k+n2
n,k=map(int,input().split())
n1=0
n2=1
for i in range(n-1):
    new_n2=f(k,n1,n2)
    n1=n2
    n2=new_n2
print(n2)