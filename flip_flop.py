def flip_flop(a):
    e=len(a)-1
    s=0
    while (s<e):
        if (a[s] != a[e]):
            return False
        s=s+1
        e=e-1
    return True

a=(1,2,3,4,3,2,1)
if (flip_flop (a)):
    print("Tuple is flip flop")

else:
    print("Tuple is not flip flop")
