def permutationEquation(p):
    t=[]
    for i in range(1,n+1):
        x=p.index(i)
        y=p.index(x+1)
        t.append(y+1)
    return t
