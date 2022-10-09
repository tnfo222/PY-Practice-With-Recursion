# Write code for algorithm 2 below


def nat_nums(lnum, hnum):
    if lnum > hnum:
        return
    else:
        print(lnum)
        nat_nums(lnum + 1, hnum)

n=10
nat_nums(1,n)