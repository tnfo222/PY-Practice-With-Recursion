# Write code for algorithm 3 below

def fib_num(n):

    #base case
    if n <= 1:
        return n
    
    #Fib seq
    else:
        return(fib_num(n-1) + fib_num(n-2))

#test case
n=4
for i in range(n):
    print(fib_num(i))