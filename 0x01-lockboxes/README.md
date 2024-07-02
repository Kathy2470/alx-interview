Lockboxes Problem
================

**Problem Statement**
--------------------

You have `n` lockboxes, and each lockbox contains a set of keys. The keys in each lockbox can be used to unlock other lockboxes. You are given a 2D array `boxes` where `boxes[i]` is an array of keys that can be used to unlock other lockboxes.

**Task**
--------

Write a function `canUnlockAll` that takes the 2D array `boxes` as input and returns `True` if all lockboxes can be unlocked, and `False` otherwise.

**Assumptions**
-------------

* A box can contain multiple keys to the same box.
* A box can contain keys that do not have corresponding boxes.
* The keys in each box are not necessarily unique.

**Example**
---------

Input: `boxes = [[1], [2], [3], [4], [5]]`
Output: `True`

Input: `boxes = [[1, 4], [2], [3], [4], [5]]`
Output: `False`

**Solution**
------------

The solution is implemented in Python and can be found in the `lockboxes.py` file.

**How to Run**
--------------

To run the solution, simply execute the `lockboxes.py` file using Python:
