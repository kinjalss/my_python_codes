#recrussion
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
fact(6)

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

num=int(input("enter a number")) 
for i in range(1,num+1):
	    print(fibo(i), end=" ") 