"""
Powerset
10/27/2021
"""
# Iteration
# O(n * 2^n) TS = O(n/2 * n^2 )
# def powerset(array):
# 	subsets = [[]]
# 	for el in array:
# 		for i in range(len(subsets)):
# 			currSubset = subsets[i]
# 			subsets.append(currSubset + [el])
# 	return subsets


# Recursion
# O(n * 2^n) TS = O(n/2 * n^2)
def powerset(array, idx=None):
    # ex. [1, 2, 3, 4]
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    el = array[idx]  # el = 4
    subsets = powerset(array, idx - 1)  # array slicing!
    # subsets = powerset([1, 2, 3, 4], 2) => powerset([1, 2, 3])
    for i in range(len(subsets)):
        currSubset = subsets[i]
        subsets.append(currSubset + [el])
    return subsets
