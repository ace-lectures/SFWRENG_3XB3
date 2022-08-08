import multiprocessing  # type: ignore
import random
from benchmark import BenchmarkSpace, run_benchmark
from jewels import CountingStrategy, Naive, Cached, OneLiner
from jewels import PooledNaive, PoolWrapper

SEED = 1659813756
NB_BOXES = 999
NB_QUERIES: list[int] = [5000]
QUERY_LENGTHS: list[int] = [50, 100, 200, 300, 400, 500]

CANDIDATES: list[CountingStrategy] = [Naive(), Cached()]
NB_CPUS = multiprocessing.cpu_count()
POOLED = [PooledNaive(x) for x in range(1, NB_CPUS + 1)]
CANDIDATES.extend(POOLED)
WRAPPED = [PoolWrapper(x, Naive()) for x in range(1, NB_CPUS + 1)]
CANDIDATES.extend(WRAPPED)
CANDIDATES.append(PoolWrapper(3, OneLiner()))


def main():
    # Initializing the randome seed once and for all!
    random.seed(SEED)
    space = BenchmarkSpace(NB_BOXES)
    space.with_nb_queries(NB_QUERIES)\
         .with_queries_length(QUERY_LENGTHS)\
         .with_strategies(CANDIDATES)
    run_benchmark(space)


if __name__ == "__main__":
    main()
