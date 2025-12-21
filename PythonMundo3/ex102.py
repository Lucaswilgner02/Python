def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(f' x', end=' ')
            else:
                print(f' = ', end=' ')
        f *= c
    return f


print(fatorial(2, True))
print(fatorial(10, True))