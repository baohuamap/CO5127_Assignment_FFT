# CO5127_Assignment_FFT

Assignment for Advanced Algorithms (CO5127) - HCMUT Master Course

## Prerequisite

install requirements

```bash
pip install -r requirements.txt
```

## Run Benchmark

To run benchmark FFT vs Python libs
```bash
make benchmark
```

To run benchmark FFT vs DFT
```bash
make benchmark_dft
```

## Performance Comparison

Below is a comparison of execution times between DFT and FFT implementations (time in **second**):

| Input Size   | DFT      | FFT    | Speed-up | Error Rate |
| ------------ | -------- | ------ | -------- | ---------- |
| 2^8 (256)    | 0.0594   | 0.0011 | 53.48    | 1.13e-12   |
| 2^10 (1024)  | 0.9743   | 0.0043 | 225.88   | 2.93e-11   |
| 2^12 (4096)  | 16.0221  | 0.0174 | 921.43   | 5.35e-10   |
| 2^14 (16384) | 252.7801 | 0.0702 | 3602.39  | 1.09e-8    |


Below is a comparison of execution times between our FFT vs Python libs implementations (in **milisec**):

| Input Size   | Our FFT  | numpy  | scipy    | FFTW       |
| ------------ | -------- | ------ | -------- | ---------- |
| 2^8 (256)    | 1.03   | 0.018 | 0.013    | 0.018   |
| 2^10 (1024)  | 4.13   | 0.018 | 0.017   | 0.018   |
| 2^12 (4096)  | 16.81  | 0.037 | 0.025   | 0.037   |
| 2^14 (16384) | 68.35 | 0.147 | 0.091  | 0.147    |
| 2^16 (65536) | 280.24 | 0.79 | 0.38  | 0.79    |
