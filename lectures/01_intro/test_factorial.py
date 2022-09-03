from unittest import skip
import pytest
from mcmath.factorial import fac_acc, fac_acc_oneline, fac_for, fac_rec, fac_rec_oneline, fac_tailrec, fac_tailrec_oneline, fac_while, fac_oneline

## Set of functions to consider for testing
imperatives  = [fac_while, fac_for, fac_oneline]
recursives   = [fac_rec, fac_rec_oneline]
accumulative = [fac_acc, fac_acc_oneline]
tail_recs = [fac_tailrec, fac_tailrec_oneline]
all = imperatives + recursives + accumulative

## Tests

@pytest.mark.parametrize("function", all)
def test_factorial_implementations(function):
    assert function(0) == 1
    assert function(1) == 1
    assert function(5) == 120

@pytest.mark.parametrize("function", all)
def test_factorial_domain(function):
    with pytest.raises(ValueError):
        function(-1)  ## This should raises a ValueError Exception


@pytest.mark.parametrize("function", all)
def test_factorial_domain(function):
    with pytest.raises(ValueError):
        function(-1)  ## This should raises a ValueError Exception


@skip
@pytest.mark.parametrize("function", recursives + accumulative)
def test_factorial_stack_rec(function):
    """
        Max recursive stack is 1,000 calls in Python!
        so non terminal recusrsion might explode
    """
    assert function(1000)


@pytest.mark.parametrize("function", imperatives+ tail_recs)
def test_factorial_large(function):
    """
        Max recursive stack is 1,000 calls in Python!
        so non terminal recusrsion might explode
    """
    assert function(1000)
