def maior(l):
    m = l[0]
    for i in range(len(l)-1):
        if m < l[i+1]:
            m = l[i+1]
        elif m > l[i+1]:
            m = m
    return m

