from abc import ABC, abstractmethod
from typing import TypedDict


class SortResult(TypedDict):
    """Model the result of a sort execution"""
    sorted: list[int]
    swaps: int


class SortAlgorithm(ABC):

    __counter = 0

    def __call__(self, data: list[int]) -> SortResult:
        """Magic method to allow an object to be called as a function"""
        self.__counter = 0
        shallow = data.copy()
        result: SortResult = {
            "sorted": self._sort(shallow),
            "ops": self.__counter
        }
        return result

    def _incr(self, n=1):
        self.__counter += n

    @abstractmethod
    def _sort(self, data: list[int]) -> list[int]:
        """Method that each algorithm must define"""
        pass
