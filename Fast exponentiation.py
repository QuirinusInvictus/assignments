def fast_expon(numb, ind):
    def even(n):
        return not(n%2) #fine
    if ind == 0:
        return 1
    elif even(ind):
        return 2**fast_expon(numb, ind/2)
    else:
        return numb * fast_expon(numb, ind-1)
