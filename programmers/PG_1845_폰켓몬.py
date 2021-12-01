"""
폰켓몬

https://programmers.co.kr/learn/courses/30/lessons/1845 
"""


def solutions(nums):
    types = set()
    for i in nums:
        types.add(i)

    return min(len(types), len(nums)//2)
