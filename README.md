# Assignment 4: Heap Data Structures

Stephanie Peguero
MSCS532-B01

## Project Overview
This repository contains two primary Python implementations.
1. `heapsort.py`: An in-place comparison sort utilizing a binary max-heap.
2. `priority_queue.py`: A task scheduler simulation utilizing a max-priority queue, enhanced with a hash map (dictionary) for constant-time index tracking.
3. `sorting_comparison.py`: A script to empirically benchmark Heapsort against Merge Sort and Randomized Quicksort.

## How to Run the Code

To run the priority queue simulation:
1. Execute the command: `python3 priority_queue.py`

To run the empirical sorting benchmark:
1. Execute the command: `python3 sorting_comparison.py`

## Summary of Findings
The empirical testing confirmed the theoretical analysis. Heapsort provided highly consistent execution times across random, sorted, and reverse-sorted arrays due to its structural reliance on the max-heap properties, guaranteeing an O(n log n) worst-case time complexity. The Max-Priority Queue successfully maintained O(log n) time complexity for insertions and extractions. By utilizing an index-tracking dictionary, the queue also maintained O(log n) time complexity for the increase-key operation by eliminating the need for an O(n) linear search.
