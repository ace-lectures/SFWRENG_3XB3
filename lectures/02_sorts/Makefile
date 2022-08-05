## install the software dependencies

SOURCES := $(shell find . -name '*.py')
MAIN_NOTEBOOK := sort_demo.ipynb

# Install software dependencies
install: 
	pipenv install --dev

# start a shell in the virtual environment
shell:
	pipenv shell

# Execute the benchmark
benchmark:
	pipenv run python benchmark.py -o outputs/pyperf_measurements.json

# Start Jupyter server and open the main notebook
jupyter:
	pipenv run python -m jupyter lab $(MAIN_NOTEBOOK)

# Run flake8 on top of the source files
lint:
	pipenv run python -m flake8 $(SOURCES)

# Run tests and compute coverage infos
test:
	pipenv run python -m coverage run -m pytest -v tests_sorts.py
	pipenv run python -m coverage report 

# clean temporary files
clean:
	rm -rf .vscode
	rm -rf .pytest_cache .vscode __pycache__ .coverage
	rm -rf .ipynb_checkpoints macsort/.ipynb_checkpoints outputs/.ipynb_checkpoints
	rm -rf macsort/__pycache__

# Delete the virtual environment for this project
clobber:
	rm -rf outputs/pyperf_measurements.json outputs/*.pdf
	pipenv --rm