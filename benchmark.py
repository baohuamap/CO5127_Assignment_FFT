import time

import numpy as np
import scipy.fftpack
import pyfftw

from fft import fft


def benchmark(func, x, runs=100):
    start = time.time()
    for _ in range(runs):
        func(x)
    end = time.time()
    return (end - start) / runs


if __name__ == "__main__":

    # Generate test data
    N = 2**12
    x = np.random.random(N)

    print("Benchmarking FFT implementations...")
    print(f"Data size: {N}")

    # Benchmark our implementation
    our_time = benchmark(fft, x)
    print(f"Our FFT implementation: {our_time:.6f} seconds")

    # Benchmark NumPy's implementation
    numpy_time = benchmark(np.fft.fft, x)
    print(f"NumPy's FFT implementation: {numpy_time:.6f} seconds")

    # Benchmark SciPy's implementation
    scipy_time = benchmark(scipy.fftpack.fft, x)
    print(f"SciPy's FFT implementation: {scipy_time:.6f} seconds")

    # Benchmark FFTW's implementation
    fftw_time = benchmark(pyfftw.builders.fft, x)
    print(f"FFTW's FFT implementation: {numpy_time:.6f} seconds")

    # Compare results
    our_result = fft(x)
    numpy_result = np.fft.fft(x)
    scipy_result = scipy.fftpack.fft(x)
    fftw_object = pyfftw.builders.fft(x)
    fftw_result = fftw_object()
    print(f"Maximum difference vs Numpy: {np.max(np.abs(our_result - numpy_result))}")
    print(f"Maximum difference vs SciPy: {np.max(np.abs(our_result - scipy_result))}")
    print(f"Maximum difference vs FFTW: {np.max(np.abs(our_result - fftw_result))}")

    # Print speedup
    print(f"NumPy speedup: {our_time / numpy_time:.2f}x")
    print(f"SciPy speedup: {our_time / scipy_time:.2f}x")
    print(f"FFTW speedup: {our_time / fftw_time:.2f}x")