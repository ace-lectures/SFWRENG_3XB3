# flake8: noqa

import pytest
from macsort.factory import SortingFactory

####      ####
## Fixtures ##
####      ####


@pytest.fixture
def empty_array() -> list[int]:
    return []

@pytest.fixture
def one_elem() -> list[int]:
    return [42]

@pytest.fixture
def already_sorted() -> list[int]:
    return [4, 8, 15, 16, 23, 42]

@pytest.fixture
def shuffled() -> list[int]:
    return [23, 4, 8, 42, 15, 16]

####             ####
## Helper function ##
####             ####


def is_sorted(array):
    """an array is sorted if each element is smaller than the following one"""
    return all(a <= b for a, b in zip(array, array[1:]))

def test_is_sorted(empty_array, one_elem, already_sorted, shuffled):
    assert is_sorted(empty_array), "The empty array is sorted"
    assert is_sorted(one_elem), "An array with one single element is sorted"
    assert is_sorted(already_sorted), "An sorted array is sorted"
    assert not is_sorted(shuffled), "This shuffled array is not sorted"

####
## Testing sort algorithms
####


@pytest.fixture
def all_cases(empty_array, one_elem, already_sorted, shuffled):
    """Using fixture composition to bring all the cases together"""
    return [empty_array, one_elem, already_sorted, shuffled]

@pytest.mark.parametrize("algorithm_name", 
                         ['bubble', 'insertion', 'merge', 'quick', 'radix'])
def test_sorting_algorithms(algorithm_name, all_cases):
    algo = SortingFactory.build(algorithm_name)
    for case in all_cases:
        print(case)
        results = algo(case)
        assert is_sorted(results['sorted']), "the result of a sort application must be sorted"

