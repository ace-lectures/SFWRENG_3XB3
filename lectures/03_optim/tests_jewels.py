# flake8: noqa

from curses.ascii import CAN
import pytest
import jewels

####           ####
## Test fixtures ##
####           ####

@pytest.fixture
def demo() -> tuple[list[jewels.Box], list[jewels.Query]]:
    """Small demo case, from the problem description"""
    return (
        [3, 8, 2, 4, 7], 
        [(1,2), (2,4)]
        )

@pytest.fixture
def bigger() -> tuple[list[jewels.Box], list[jewels.Query]]:
    """ Bigger demo case (15 boxes and 10 queries)"""
    return (
        [28, 4, 100, 93, 20, 57, 94, 29, 13, 83, 18, 14, 34, 66, 55],
        [(3, 13), (1, 13), (4, 7), (1, 5), (11, 14), 
         (5, 6), (2, 3), (10, 14), (6,9), (6, 7)]
    )

####        ####
## Test Cases ##
####        ####

CANDIDATES: list[jewels.CountingStrategy] = [
    jewels.Naive(), jewels.SumBuiltin(), jewels.NaiveSlicing(),
    jewels.SumSlicing(), jewels.OneLiner(), jewels.Cached(),
    jewels.PoolWrapper(2,jewels.OneLiner()), jewels.PooledNaive(2)
]

# As strategies are custom objects, to properly name the test cases we need to
# provide as 'ids' a function that maps a given object to its string
# representation: We use an anonymous function that calls `str` to get the 
# name of a given strategy (its class name)

@pytest.mark.parametrize('strategy', CANDIDATES, ids = lambda x: str(x))
def test_on_demo_case(strategy, demo):
    boxes   = demo[0]
    queries = demo[1]
    assert strategy.run(boxes, queries)

@pytest.mark.parametrize('strategy', CANDIDATES, ids = lambda x: str(x))
def test_on_bigger_case(strategy, bigger):
    boxes   = bigger[0]
    queries = bigger[1]
    assert strategy.run(boxes, queries)
