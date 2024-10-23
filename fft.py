import numpy as np

def fft(x):
    x = np.asarray(x, dtype=complex)
    N = len(x)

    if N <= 1:
        return x

    even = fft(x[0::2])
    odd = fft(x[1::2])

    twiddle_factors = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([even + twiddle_factors[:N//2] * odd,
                           even - twiddle_factors[:N//2] * odd])