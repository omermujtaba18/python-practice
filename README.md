# Python Prep


### Big(O)

#### Searching
- Binary Search O(log n)
- Linear Search O(n)

#### Sorting
- O ( comparisons/step * total steps )
- Bubble Sort O(n^2)
- Merge Sort O(n log n)
- Quick Sort Worst(n^2) , Best(n log n)


### Quick Algorithm
- Binary Search (Go to mid, divide in upper or lower half if search value is less or more)
- Linear Search (Iterate through every element)
- Bubble Sort (Move largest to the end, check first two and swicth if first is larger than second. Keep iterating until sorted)
- Merge sort (Divide in half, sort, and merge)
- Quick Sort

### Notes

- Fibonacci: In practice if we were to use recursion to solve this problem we should use a hash table to store and fetch previously calculated results. This will increase the space needed but will drastically improve the runtime efficiency.
- Fibonacci: The number of recursive calls grows exponentially with n.

### Useful Resources

- https://wiki.python.org/moin/TimeComplexity (TimeComplexity of different python functions)
- https://developers.google.com/edu/python/lists (Python lists)
- https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-queues (Python queues)
- https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks (Python stacks)
- https://algs4.cs.princeton.edu/22mergesort/ (Merge Sort)

### TODO
- Practice recursion more!
- Practice Hash tables (Custom Hash tables)