def largest_power(n):
    if n == 1:
        return (0, -1)
    elif n <= 4:
        return (1, -1)
    else:
        high = -1
        occ = 0
        for k in range(n)[::-1]:
            for z in range(2, 50):
                if round(k**(1/z))**z == k and high == -1:
                    high = k
                    occ += 1
                elif round(k**(1/z))**z == k:
                    occ += 1
            if max != -1 and occ != 0:
                return high, occ