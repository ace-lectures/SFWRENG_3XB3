# The Jewel Factory

  - Author: [Sebastien Mosser](mossers@mcmaster.ca])
  - version: 2022.08

## Description

A jewel factory is organized as the following: gems are stored in boxes, aligned on a shelf. Each boxe contains a given number of gems.

When a jeweller is creating a new piece of jewellery, they need to always know how many remaining gems they can use for their creation. It is important to answer to this query as fast as possible, to not slow down their creativity process.

Your job is to create a program that, considering the current state of the shelf, can answer to the numerous queries a jeweller can make to know how many gems are available in the boxes they can see from their workstation. 

## Implementation

The signature of the principal function of this program is the following:

```python
## Types Aliasing for readability
Box  = int
From = int
To   = int
Query = tuple[From, To]
Result = int

## Signatures
def run(boxes: list[Box], queries: list[Query]) -> list[Result]:
  pass
```

Example:

```python
# We define five boxes.
my_boxes = [3, 8, 2, 4, 7]
# We define two queries over these five boxes
my_queries = [(1,2), (2,4)]
run(my_bozes, my_queries)  # returns [11, 14]
```
  - The first box contains 3 gems, the second one 8, the third one 2, the fourth one 4 and finally the fifth one 7.
  - The first query asks for the number of gems in the [1,2] interval. The asnwer is 11 (=3+8).
  - the second query asks for the number of gems in the [2,4] interval. The answer is 14 (=8+2+4)

## Constraints

The following constraints are enforced by design and does not need to be checked in the code:

  - $2 \le |\textrm{boxes}| \le 1,000$
  - $1 \le |\textrm{queries}| \le 50,000$
  - $\forall\ (\textrm{from},\textrm{to}) \in \textrm{queries},$ 1 ≤ from < to ≤ |boxes|

