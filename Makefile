.PHONY: benchmark clean

BENCHMARK_SCRIPT=benchmark.py

benchmark:
	python3 $(BENCHMARK_SCRIPT)

clean:
	rm -f *.pyc