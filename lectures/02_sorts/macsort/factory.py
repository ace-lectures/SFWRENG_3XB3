# Sorting algorithm collections

import macsort.algorithms as algo
from macsort.interface import SortAlgorithm


class SortingFactory():

    @staticmethod
    def build(name: str) -> SortAlgorithm:
        selected = None
        match name:
            case 'bubble':
                selected = algo.BubbleSort()
            case 'insertion':
                selected = algo.InsertionSort()
            case 'merge':
                selected = algo.MergeSort()
            case 'quick':
                selected = algo.QuickSort()
            case 'radix':
                selected = algo.RadixSort()
            case _:
                raise ValueError(name)
        return selected
