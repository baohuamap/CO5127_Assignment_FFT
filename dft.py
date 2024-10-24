import cmath

def dft(x):
    N = len(x)
    X = []
    for k in range(N):
        sum = 0
        for n in range(N):
            angle = 2j * cmath.pi * k * n / N
            sum += x[n] * cmath.exp(-angle)
        X.append(sum)
    return X
