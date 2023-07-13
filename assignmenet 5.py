def recur(n):
    if n == 0:
        return n
    else:
        return n + recur(n-1)
k= recur(10)

print(k)