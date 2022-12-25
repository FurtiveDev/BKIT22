def fibonachi(n):
    f = [0, 1]
    for i in range(n):
        yield f[i]
        f.append(f[i] + f[i + 1])