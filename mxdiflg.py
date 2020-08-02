
def mxdiflg(a1, a2):
    max=0
    for x in a1:
        for y in a2:
            if abs(len(x)-len(y))>max:
                max = abs(len(x)-len(y))
    return max
