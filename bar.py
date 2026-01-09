def bar(l):
    r = max(l)
    c = len(l)
    for i in range(r):
        for j in range(c):
            if l[j]+i >= max(l):
                print('*',end='  ')
            else:
                print(' ',end='  ')
        print()
bar([2,5,6,0])
 