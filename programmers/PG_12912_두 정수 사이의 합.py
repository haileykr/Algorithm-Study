"""
두 정수 사이의 합


https://programmers.co.kr/learn/courses/30/lessons/12912
"""


def solutions(a, b):
    return sum(range(min(a, b), max(a, b) + 1))

