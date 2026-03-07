#!/usr/bin/env python3
import sys
from collections import deque, OrderedDict


def fifo(k, requests):
    cache = set()
    queue = deque()
    misses = 0

    for r in requests:
        if r in cache:
            continue
        misses += 1
        if len(cache) == k:
            evicted = queue.popleft()
            cache.remove(evicted)
        cache.add(r)
        queue.append(r)

    return misses


def lru(k, requests):
    cache = OrderedDict()
    misses = 0

    for r in requests:
        if r in cache:
            cache.move_to_end(r)
            continue
        misses += 1

        if len(cache) == k:
            cache.popitem(last=False)
        cache[r] = True

    return misses


def optff(k, requests):
    cache = set()
    misses = 0

    for i, r in enumerate(requests):
        if r in cache:
            continue
        misses += 1

        if len(cache) == k:
            farthest_page = None
            farthest_index = -1
            for page in cache:
                for j in range(i + 1, len(requests)):
                    if requests[j] == page:
                        if j > farthest_index:
                            farthest_index = j
                            farthest_page = page
                        break
                else:
                    farthest_page = page
                    break

            cache.remove(farthest_page)
        cache.add(r)

    return misses


def main():
    if len(sys.argv) != 2:
        print("Usage: cache_policies.py <input_file>")
        return

    try:
        with open(sys.argv[1]) as f:
            first_line = f.readline().split()
            k = int(first_line[0])
            m = int(first_line[1])
            second_line = f.readline().split()
            requests = [int(x) for x in second_line]

        if m != len(requests):
            print("Provided number of requests does not match actual number of requests")
            return

        if k <= 0:
            print("Cache size k must be a positive integer")
            return

        print(f"FIFO  : {fifo(k, requests)}")
        print(f"LRU   : {lru(k, requests)}")
        print(f"OPTFF : {optff(k, requests)}")

    except FileNotFoundError:
        print(f"File not found: {sys.argv[1]}")
    except (ValueError, IndexError):
        print("Invalid input")


if __name__ == "__main__":
    main()