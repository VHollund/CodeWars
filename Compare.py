def comp(array1, array2):
    if isinstance(array1, list) and isinstance(array2, list) and len(array2) == len(array1):
        array1, array2 = sorted([abs(x) for x in array1]), sorted([abs(x) for x in array2])
        for i, x in enumerate(array1):
            if array2[i] != x**2:
                return False
        return True
    return False
