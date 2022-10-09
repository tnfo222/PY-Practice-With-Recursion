# Write code for algorithm 1 below
def fun(n):

    #base case
    if n==0:
        return

    #Recursive case
    else:
        print(n)
        fun(n-1)

#test case
n=8
fun(n)


    #or
    #def count_down(n):
        #inherent base case
        #(will stop if n <= 0)
        #if n>0:
            #recursive case
            #print(n)
            #count_down(n-1)
   
        #test case
        #n=8
        #count_down(n)

