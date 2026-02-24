# Python 3 Cheatsheet: Math & Utilities

## Math
```python
divmod(8, 3)     # (2, 2) -> (quotient, remainder)
pow(a, b, m)     # (a ** b) % m
float('inf')     # Infinity
float('-inf')    # Neg Infinity
```

## Random
```python
import random
random.choice([1,2,3])
random.randint(0, 10)    # Inclusive
random.randrange(0, 10)  # Exclusive of stop
random.shuffle(lst)      # In-place shuffle
```

## Bisect (Binary Search)
For sorted lists.
```python
import bisect
arr = [1, 2, 4, 4, 6]
bisect.bisect_left(arr, 4)   # 2 (First insertion point)
bisect.bisect_right(arr, 4)  # 4 (Last insertion point)
bisect.insort(arr, 3)        # Insert maintaining order
```

## Bitwise
```python
a, b = 0b1100, 0b1010
a & b   # AND
a | b   # OR
a ^ b   # XOR
a >> 2  # Right Shift
a << 2  # Left Shift
```

## Control Flow Tricks
**For-Else**
Else runs only if loop completes without `break`.
```python
for item in container:
    if search(item):
        break
else:
    print("Not found")
```

**Ternary Operator**
```python
value = "A" if condition else "B"
```

## Regex
```python
import re
re.sub('a|e|i|o|u', '', "apple") # "ppl"
```
