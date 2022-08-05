import pyperf
import random
from macsort.factory import SortingFactory
from macsort.interface import SortAlgorithm


def main():
    """Running the complete benchmark"""
    random.seed(1659644754)
    the_array = gen_array(10000)
    algorithms = ['radix', 'quick', 'merge', 'insertion', 'bubble']
    do_bench(algorithms, the_array)


def gen_array(n: int) -> list[int]:
    """generate a random array of known size"""
    return random.sample(range(n), n)


def python_sort(array: list[int]):
    """Making list sorting compatible with PyPerf interface"""
    array.sort()


def do_bench(algorithms: list[SortAlgorithm], array: list[int]) -> None:
    """run the benchmark over a set of algorithm and the baseline"""
    runner = pyperf.Runner()
    # Baseline run
    runner.bench_func("python-sort", python_sort, array)
    # algorithms run
    for an_algorithm in algorithms:
        sorter = SortingFactory.build(an_algorithm)
        runner.bench_func(an_algorithm, sorter, array)


if __name__ == "__main__":
    main()
