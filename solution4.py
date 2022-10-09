# Write code for algorithm 4 below
def pwr(base, exp):

    #base case
    if exp==0:
        return 1

    #invalid case
    elif exp < 1:
        print("invalid input")
    
    #calculate
    else:
        return base*pwr(base, exp-1)

base=3
exp=0
print(pwr(base,exp))