def queue(queuers, pos):
    t=0
    while True:
        queuers[0] -= 1
        t += 1
        if queuers[pos] == 0:
            return t
        if queuers[0]>0:
            queuers.append(queuers[0])
        queuers.remove(queuers[0])
        if pos <= 0:
            pos = len(queuers)-1
            continue
        pos -= 1
