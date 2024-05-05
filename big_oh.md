# Big Oh Cheet Sheets :)

## Data Structures

A collection of values
Arrays

    search — O(n)
    lookup O(1) — fast
    push — O(1) or O(n) if use flexible key
    insert O(n) — linear time
    delete O(n)

Pros & Cons

    Pros: fast lookups, fast push/pop, ordered
    Cons: slow inserts, slow deletes, fixed size (if using static array)

Linked List

    prepend — O(1) //add at the beginning
    append — O(1) //add at the end
    lookup — O(n) //traversal, from the head to what we look for
    insert — O(n) //go one by one, find the index, and insert there
    delete — O(n) //we have to find the item

Pros & Cons

    Pros: fast insertion, fast deletion, ordered, flexible size
    Cons: slow lookup, more memory

Hash Tables

    search — O(1)
    insert — O(1)
    lookup — O(1) or O(n) if collision
    delete — O(1)

Pros & Cons

    Pros: fast lookups (good collision resolution needed), fast inserts, flexible keys
    Cons: unordered, slow key iteration

Stacks （LIFO)

    lookup — O(n) //you do not want to traverse the whole stack
    pop — O(1) //remove the last item on the list
    push — O(1) //add the item to the last on the list
    peek — O(1) //view the top of the last plate

Pros & Cons

    Pros: fast operations, fast peek, ordered
    Cons: slow lookup

Queues (FIFO)

    lookup — O(n) //you do not want to traverse the whole stack, lookup usually does not do
    enqueue — O(1) //push, add the person to the line, add to the last
    dequeue — O(1) //shift, remove the person from the line, take the first
    peek — O(1) //view the top of the last plate

Pros & Cons

    Pros: fast operations, fast peek, ordered
    Cons: slow lookup

Trees

Balanced BST

    lookup — O(log N)
    insert — O(log N)
    delete — O(log N)

Binary Tree

    lookup — O(n)
    insert — O(log N)
    delete — O(log N)

Graphs

    Pros: Relationship
    Cons: Scaling is hard

## Algorithms

The algorithm is a sequence of steps that correctly map every possible input to the problem to the correct output
Recursion

    Pros: DRY, Readability
    Cons: Large Stack

Bubble Sort (bubble up highest)

    Time — O(n²)
    Space — O(1)

Selection Sort (smallest places first)

    Time — O(n²)
    Space — O(1)

insertion Sort (insert to the right location)

    Time — O(n) — small dataset or nearly sorted
    Time — O(n²) — worst case
    Space — O(1)

Merge Sort (most often used, divide & conquer)

    Time — O(n log n)
    Space — O(n log n)

Quick Sort (most often used, divide & conquer)

    Time — O(n²) — worst the case you pick the bad pivot
    Time — O(n log n) — usually the fastest sorting algorithm on average
    Space — O(log n) — better than merge sort

Breadth First Search (node at the upper level)

    Pros: shortest path, closer nodes
    Cons: more memory than DFS

Depth First Search (node at the lower level)

    Pros: less memory, determine whether a path exists
    Cons: can get slow (especially if the tree or graph is very deep)