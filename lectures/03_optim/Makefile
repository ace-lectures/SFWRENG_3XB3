## install the software dependencies

SOURCES := $(shell find . -name '*.py')
TESTS := $(shell find . -name 'tests_*.py')
MAIN_NOTEBOOK := plot_benchs.ipynb
BENCHMARK := outputs/pyperf_measurements.json
BENCHMARK_PAR := outputs/pyperf_measurements_par.json
OUTPUT_FILES := $(shell find . -name 'outputs/*.pdf')

# Install software dependencies
install: 
	pipenv install --dev

# start a shell in the virtual environment
shell:
	pipenv shell

# Execute the benchmark
benchmark:
	pipenv run python benchmark_sequential.py -o $(BENCHMARK)

benchmark_par:
	pipenv run python benchmark_parallel.py -o $(BENCHMARK_PAR)

# Start Jupyter server and open the main notebook
jupyter:
	pipenv run python -m jupyter lab $(MAIN_NOTEBOOK)

# Run flake8 on top of the source files
lint:
	pipenv run python -m mypy $(SOURCES)
	pipenv run python -m flake8 --ignore=E266,E302 $(SOURCES)

# Run tests and compute coverage infos
test:
	pipenv run python -m coverage run -m pytest -v $(TESTS)
	pipenv run python -m coverage report 

# clean temporary files
clean:
	rm -rf .vscode
	rm -rf .pytest_cache .vscode __pycache__ .coverage .mypy_cache
	rm -rf .ipynb_checkpoints outputs/.ipynb_checkpoints

# Delete the virtual environment for this project
clobber:
	rm -rf $(BENCHMARK) $(BENCHMARK_PAR) $(OUTPUT_FILES)
	pipenv --rm