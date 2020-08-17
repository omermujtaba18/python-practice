# Python Practice

This repo has two parts.
1. Algorithm and Data Strucutres
2. [Codewars](https://www.codewars.com/) Solutions

## 1. Codewars Solutions

The solutions are divided among three focus areas of Codewars
1. Fundamentals
2. Rank up
3. Practice and Repeat

**Note**: The questions are numbered in terms of difficulty with 1 being the least difficult.

## 2. Algorithm and Data Strucutres 

I am following the [Udacity Data Structures and Algorithms Course](https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513), this repo has all the practice problems that has been taught in the said course.

### Big(O)

#### Searching
- Binary Search O(log n)
- Linear Search O(n)

#### Sorting
- O ( comparisons/step * total steps )
- Bubble Sort O(n^2)
- Merge Sort O(n log n)
- Quick Sort Worst(n^2) , Best(n log n)

#### Heap
- O (n) Search
- Insert/Delete Worst O(log n),

#### BST
- O (n)

### Quick Algorithm
- Binary Search (Go to mid, divide in upper or lower half if search value is less or more)
- Linear Search (Iterate through every element)
- Bubble Sort (Move largest to the end, check first two and swicth if first is larger than second. Keep iterating until sorted)
- Merge sort (Divide in half, sort, and merge)
- Quick Sort

### Notes

- Fibonacci: In practice if we were to use recursion to solve this problem we should use a hash table to store and fetch previously calculated results. This will increase the space needed but will drastically improve the runtime efficiency.
- Fibonacci: The number of recursive calls grows exponentially with n.
- Tree Traversal: Pre-Order, In-Order, Post-Order
- Pre-Order: Check off self and go left to check off, then check off right
- In-Order: Check off self only after all left child are check off
- Post-Order: Checkoff the all leaf node (left-right), then check off parent 
- Heaps are stored in arrays
- Max Heap: Parent greater than child
- Min Heap: Parent less than child
- Heapify : Rearrange heap on insertion or deletion

### Useful Resources

- https://wiki.python.org/moin/TimeComplexity (TimeComplexity of different python functions)
- https://developers.google.com/edu/python/lists (Python lists)
- https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-queues (Python queues)
- https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks (Python stacks)
- https://algs4.cs.princeton.edu/22mergesort/ (Merge Sort)

### TODO
- Practice recursion more!
- Practice Hash tables (Custom Hash tables)
- Self-Balancing-Tree (Red-Black-Tree) rules
