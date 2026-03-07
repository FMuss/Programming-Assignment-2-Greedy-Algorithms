# Programming Assignment 2: Greedy Algorithms

**Faris Mussulman - 41342080**

## Build Instructions

No compilation required. Requires **Python 3**.

## Running the Program

```bash
python3 src/cache_policies.py <input_file>
```

**Example input:**
```bash
python3 src/cache_policies.py input/examples/cycle.in
```

**Example ouput:**
```
FIFO  : 60
LRU   : 60
OPTFF : 32
```

## Assumptions

**Input format:**

```
k m
r1 r2 r3 ... rm
```

- First line: integer k (cache capacity >=1) and integer m (number of requests)
- Second line: r1, r2, r3 ... rm (sequence of m requests)

**Console output:**

```
FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>
```

## Written Component

Written component answers are provided in `Programming Assignment 2: Greedy Algorithms Report.pdf`
