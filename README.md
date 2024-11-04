# Lab 5
# Stack and queue in Python

This repository contains implementations of basic data structures in Python, specifically a Stack and a Queue, along with practical problems and exercises that utilize these structures.

## Table of Contents

- [Stack Implementation](#stack-implementation)
- [Queue Implementation](#queue-implementation)
- [Practical Problems](#practical-problems)
  - [Balanced Parentheses](#balanced-parentheses)
  - [Reverse a String](#reverse-a-string)
  - [Hot Potato Simulation](#hot-potato-simulation)


- [Exercises](#exercises)
  - [Evaluate Postfix Expressions](#evaluate-postfix-expressions)
  - [Queue Using Two Stacks](#queue-using-two-stacks)
  - [Task Scheduler Using Queue](#task-scheduler-using-queue)
  - [Convert Infix to Postfix](#convert-infix-to-postfix)

## Stack Implementation

The `Stack` class provides the following methods:
- `push(item)`: Adds an item to the top of the stack.
- `pop()`: Removes and returns the item from the top of the stack.
- `peek()`: Returns the item at the top of the stack without removing it.
- `is_empty()`: Checks if the stack is empty.
- `size()`: Returns the number of items in the stack.



# Lab 6
# Singly Linked List Implementation 

This practical contains a simple implementation of a singly linked list in Python. It provides various methods to manipulate and interact with the linked list, including appending nodes, inserting at specific positions, deleting nodes, searching for values, reversing the list, and merging two sorted linked lists.

## Features

- *Node Class*: Represents an individual node in the linked list.

- *LinkedList Class*: Implements the linked list with several methods:

  - append(data): Adds a new node with the specified data to the end of the list.

  - insert(data, position): Inserts a new node at a specified position.

  - delete(data): Removes the first node with the specified data.

  - search(data): Searches for a node containing the specified data and returns its position.

  - display(): Displays the contents of the linked list in a user-friendly format.

  - reverse(): Reverses the linked list in place.

  - find_middle(): Finds and returns the middle element of the linked list.

  - has_cycle(): Detects if the linked list contains a cycle.

  - remove_duplicates(): Removes duplicate values from the linked list.
  
  - merge_sorted(other_list): Merges two sorted linked lists into one sorted linked list.



# Lab 7
# Binary Search Tree (BST) Implementation in Python

This practical provides a Python implementation of a Binary Search Tree (BST) with various essential operations. The BST is implemented using two classes:

1. Node - Represents a single node in the BST.

2. BinarySearchTree - Implements the BST structure with methods for inserting, deleting, and traversing nodes, among other features.

## Features

This implementation includes the following features:

### 1. *Insertion*
   - Insert a new value into the BST, maintaining the binary search property.

### 2. *Search*
   - Search for a specific value in the BST. Returns True if found, otherwise False.

### 3. *Deletion*
   - Remove a specified node from the BST, adjusting the tree to maintain its structure.

### 4. *Traversals*
   - *In-order Traversal*: Visit nodes in ascending order.
   - *Pre-order Traversal*: Visit nodes in root-left-right order.
   - *Post-order Traversal*: Visit nodes in left-right-root order.
   - *Level-order Traversal*: Visit nodes level by level (breadth-first search).

### 5. *Maximum Value*
   - Find the maximum value present in the BST.

### 6. *Node Count*
   - Count the total number of nodes in the BST.

### 7. *Height of the BST*
   - Calculate the height (or depth) of the BST, defined as the longest path from the root to a leaf.

### 8. *Validity Check*
   - Check if the BST satisfies the binary search tree property.




# Lab 8
# Sorting Algorithms

This project implements several sorting algorithms in Python, including Bubble Sort, Merge Sort, Quick Sort, and a hybrid sorting algorithm that utilizes Insertion Sort for small subarrays. Additionally, it includes performance comparison and visualization of the sorting processes.

## Table of Contents

- [Features](#features)
- [Algorithms Implemented](#algorithms-implemented)
- [Usage](#usage)
- [Performance Comparison](#performance-comparison)
- [Visualization](#visualization)
- [Contributing](#contributing)
- [License](#license)

## Features

- Implementations of multiple sorting algorithms.
- Performance comparison of the algorithms on a large dataset.
- Visualization of the sorting process using Matplotlib.
- Optimizations for Bubble Sort and Quick Sort.
- Hybrid sorting algorithm using Insertion Sort for small subarrays.

## Algorithms Implemented

1. **Bubble Sort**
   - A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
   - Optimized to stop early if the array is already sorted.

2. **Merge Sort**
   - A divide-and-conquer algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves.

3. **Quick Sort**
   - Another divide-and-conquer algorithm that selects a 'pivot' element and partitions the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
   - An in-place version is implemented for improved space efficiency.

4. **Hybrid Merge Sort**
   - Combines Merge Sort and Insertion Sort, using Insertion Sort for small subarrays to improve performance.




# Lab 9
# Graph Implementation in Python

This project provides a comprehensive implementation of a Graph data structure in Python, along with various algorithms for graph traversal, pathfinding, cycle detection, and more.

## Table of Contents

- [Features](#features)
- [Classes and Methods](#classes-and-methods)
- [Usage](#usage)
- [Algorithms Implemented](#algorithms-implemented)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add vertices and edges to create a graph.
- Depth-First Search (DFS) and Breadth-First Search (BFS) traversal methods.
- Find all paths between two vertices.
- Check if the graph is connected.
- Detect cycles in a graph.
- Dijkstra's algorithm for finding the shortest path in a weighted graph.
- Check if the graph is bipartite.

## Classes and Methods

### Graph Class

- `__init__()`: Initializes an empty graph.
- `add_vertex(vertex)`: Adds a vertex to the graph.
- `add_edge(vertex1, vertex2)`: Adds an undirected edge between two vertices.
- `print_graph()`: Prints the graph in an adjacency list format.
- `dfs(start_vertex)`: Performs Depth-First Search starting from the specified vertex.
- `bfs(start_vertex)`: Performs Breadth-First Search starting from the specified vertex.
- `find_all_paths(start_vertex, end_vertex, path=[])`: Finds all paths from the start vertex to the end vertex.
- `is_connected()`: Checks if the graph is connected.

### Additional Functions

- `bfs_shortest_path(graph, start, goal)`: Finds the shortest path between two vertices using BFS.
- `has_cycle_graph(graph)`: Detects cycles in a graph.
- `dijkstra(graph, start)`: Implements Dijkstra's algorithm for shortest paths in a weighted graph.
- `is_bipartite(graph)`: Determines if the graph is bipartite.

