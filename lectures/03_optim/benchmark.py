import pyperf  # type: ignore
import random
from typing import TypedDict
from jewels import Box, Query, CountingStrategy


####                      ####
## Reifying the query space ##
####                      ####

class SpaceElement(TypedDict):
    name: str
    strategy: CountingStrategy
    boxes: list[Box]
    queries: list[Query]

class BenchmarkSpace():

    def __init__(self, nb_boxes: int) -> None:
        self.__nb_boxes: int = nb_boxes
        self.__strategies: list[CountingStrategy] = []
        self.__queries_lengths: list[int] = []
        self.__nb_queries: list[int] = []

    def with_strategies(self, strats: list[CountingStrategy]):
        self.__strategies.extend(strats)
        return self

    def with_queries_length(self, lengths: list[int]):
        self.__queries_lengths.extend(lengths)
        return self

    def with_nb_queries(self, nb_queries: list[int]):
        self.__nb_queries.extend(nb_queries)
        return self

    def finalize(self) -> list[SpaceElement]:
        result = []
        boxes = [random.randint(0, 100) for _ in range(self.__nb_boxes)]
        for length in self.__queries_lengths:
            for nb_q in self.__nb_queries:
                queries = self.__gen_queries(nb_q, length)
                for strategy in self.__strategies:
                    elem: SpaceElement = {
                        'name': self.__build_name(strategy, nb_q, length),
                        'strategy': strategy,
                        'boxes': boxes,
                        'queries': queries
                    }
                    result.append(elem)
        return result

    def __repr__(self) -> str:
        result = ""
        result += f'|boxes|        = {self.__nb_boxes}\n'
        result += f'|strategies|   = {len(self.__strategies)} ('
        result += ', '.join(map(lambda x: str(x), self.__strategies)) + ")\n"
        result += f'|query_length| = {len(self.__queries_lengths)} ('
        result += ', '.join(map(lambda x: str(x), self.__queries_lengths)) + ")\n"  # noqa: E501
        result += f'|nb_queries|   = {len(self.__nb_queries)} ('
        result += ', '.join(map(lambda x: str(x), self.__nb_queries)) + ")\n"
        size = len(self.__nb_queries)
        size *= len(self.__queries_lengths)
        size *= len(self.__strategies)
        result += f'==>> |space|   = {size}'
        return result

    def __gen_queries(self, nb_queries: int, length: int) -> list[Query]:
        """Generate nb_queries queries of size length over nb_boxes boxes"""
        queries = []
        for _ in range(nb_queries):
            f = random.randint(1, self.__nb_boxes - length)
            t = f + length
            queries.append((f, t))
        return queries

    def __build_name(self, strategy: CountingStrategy,
                     nb_queries: int, length: int) -> str:
        return f'{strategy}-{self.__nb_boxes}-{nb_queries}-{length}'


####                 ####
## Running a benchmark ##
####                 ####

def run_benchmark(space: BenchmarkSpace):
    runner = pyperf.Runner()
    elements: list[SpaceElement] = space.finalize()
    for e in elements:
        runner.bench_func(e['name'], e['strategy'].run,
                          e['boxes'], e['queries'])
