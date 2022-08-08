# We use multiprocess instead of multiprocessing (std) to deal
# more easily with  anonymous functions for data parallelism
from multiprocess import Pool  # type: ignore
from abc import ABC, abstractmethod

####                ####
## Interface contract ##
####                ####

Box = int
From = int
To = int
Query = tuple[From, To]
Result = int

class CountingStrategy(ABC):

    @abstractmethod
    def run(self, boxes: list[Box], queries: list[Query]) -> list[Result]:
        pass

    def __str__(self) -> str:
        return self.__class__.__name__


####                    ####
## Python Implementations ##
####                    ####

class Naive(CountingStrategy):
    """Using a for loop (bad practice in Python, very slow)"""

    def run(self, boxes: list[Box], queries: list[Query]) -> list[Result]:
        result = []
        for (f, t) in queries:
            s = 0
            for e in (boxes[i] for i in range(f - 1, t)):
                s += e
            result.append(s)
        return result


class SumBuiltin(CountingStrategy):
    """Using a for loop, and the internal builtin `sum`"""

    def run(self, boxes: list[Box], queries: list[Query]) -> list[Result]:
        result = []
        for (f, t) in queries:
            result.append(sum(boxes[i] for i in range(f - 1, t)))
        return result


class NaiveSlicing(CountingStrategy):
    """Using slicing (in place) instead of comprehension (copy)"""

    def run(self, boxes: list[Box], queries: list[Query]) -> list[Result]:
        result = []
        for (f, t) in queries:
            s = 0
            for e in boxes[f - 1:t]:
                s += e
            result.append(s)
        return result


class SumSlicing(CountingStrategy):
    """mixing slicing and internal builtin"""

    def run(self, boxes: list[Box], queries: list[Query]) -> list[Result]:
        result = []
        for (f, t) in queries:
            result.append(sum(boxes[f - 1:t]))
        return result


class OneLiner(CountingStrategy):
    """Getting rid of the for loop"""

    def run(self, boxes: list[Box], queries: list[Query]) -> list[Result]:
        return list(map(lambda e: sum(boxes[e[0] - 1:e[1]]), queries))

####                 ####
## Domain Optimization ##
####                 ####


class Cached(CountingStrategy):
    """Maintaining intermediate sums"""

    def run(self, boxes: list[Box], queries: list[Query]) -> list[Result]:
        cache = [0]
        for b in boxes:
            cache.append(cache[-1] + b)
        return list(map(lambda e: cache[e[1]] - cache[e[0] - 1], queries))

####              ####
## Data Parallelism ##
####              ####


class PooledNaive(CountingStrategy):
    """Leveraging manually data parallelism for the Naive strategy"""

    def __init__(self, pool_size: int) -> None:
        self.__pool_size = pool_size

    def run(self, boxes: list[Box], queries: list[Query]) -> list[Result]:
        with Pool(self.__pool_size) as pool:
            return pool.map(lambda q: self.__handle_a_query(boxes, q), queries)

    def __handle_a_query(self, boxes: list[Box], query: Query) -> Result:
        f, t = query
        s = 0
        for e in (boxes[i] for i in range(f - 1, t)):
            s += e
        return s

    def __str__(self) -> str:
        return f'{super().__str__()}_{self.__pool_size}'


class PoolWrapper(CountingStrategy):
    """Leveraging OOP to decorate any strategy with data parallelism"""

    def __init__(self, pool_size: int, strategy: CountingStrategy) -> None:
        self.__strategy = strategy
        self.__pool_size = pool_size

    def run(self, boxes: list[Box], queries: list[Query]) -> list[Result]:
        with Pool(self.__pool_size) as pool:
            return pool.map(lambda q: self.__handle_a_query(boxes, q), queries)

    def __handle_a_query(self, boxes: list[Box], query: Query) -> Result:
        return self.__strategy.run(boxes, [query])[0]

    def __str__(self) -> str:
        return f'Pooled({str(self.__strategy)})_{self.__pool_size}'
