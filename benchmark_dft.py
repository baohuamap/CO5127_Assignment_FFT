import time

import numpy as np
import scipy.fftpack
import pyfftw

from fft import fft
from dft import dft


def benchmark(func, x, runs=3):
    start = time.time()
    for _ in range(runs):
        func(x)
    end = time.time()
    return (end - start) / runs


if __name__ == "__main__":

    print("Benchmarking FFT implementations...")
    for i in [8, 10 , 12, 14]:
        # Generate test data
        N = 2**i
        x = np.random.random(N)

        print("==================================================")
        print(f"Data size: {N}")

        # Benchmark our implementation
        fft_time = benchmark(fft, x)
        print(f"Our FFT implementation: {fft_time:.6f} seconds")

        # Benchmark NumPy's implementation
        dft_time = benchmark(dft, x)
        print(f"Our DFT implementation: {dft_time:.6f} seconds")

        # Compare results
        fft_result = fft(x)
        dft_result = dft(x)
        print(f"Maximum difference fft vs dft: {np.max(np.abs(fft_result - dft_result))}")

        # Print speedup
        print(f"FFT speedup: {dft_time / fft_time:.2f}x")