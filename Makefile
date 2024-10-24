.PHONY: benchmark clean

benchmark:
	python3 benchmark.py

benchmark_dft:
	python3 benchmark_dft.py

clean:
	rm -f *.pyc