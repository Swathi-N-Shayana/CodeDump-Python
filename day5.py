#Read an integer N. For all non-negative integers i<N , print  i^2 
n = int(input())
if(n>0):
    for i in range(0,n):
        print(i*i)
