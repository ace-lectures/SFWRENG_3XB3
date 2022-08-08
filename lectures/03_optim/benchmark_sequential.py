import random
from benchmark import BenchmarkSpace, run_benchmark
from jewels import CountingStrategy, Naive, SumBuiltin
from jewels import NaiveSlicing, SumSlicing, OneLiner, Cached


NB_BOXES = 999
SEED = 1659813756
CANDIDATES: list[CountingStrategy] = [
    Naive(), SumBuiltin(), NaiveSlicing(), SumSlicing(), OneLiner(), Cached()
]
NB_QUERIES: list[int] = [250, 500, 750, 1000]
QUERY_LENGTHS: list[int] = [50, 100, 200, 300, 400, 500]

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
