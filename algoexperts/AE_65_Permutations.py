"""
Permutations
10/29/2021
"""

# First Solution
# O(n!*n^2) Time | O(n!*n) Space
def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper(newArray, newPermutation, permutations)





# Second Solution
# O(n!*n) Time|Space
def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(idx, array, permutations):
    if idx == len(array)-1:
        permutations.append(array[:])  # snapshot!
    else:
        for j in range(idx, len(array)):
            swap(array, idx, j)
            permutationsHelper(idx+1, array, permutations)
            swap(array, j, idx)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]