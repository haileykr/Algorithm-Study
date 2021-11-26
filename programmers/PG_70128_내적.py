"""
내적


https://programmers.co.kr/learn/courses/30/lessons/70128
"""


def solution(a, b):
    answer = 0
    for i, v in enumerate(a):
        answer += v + b[i]
    return answer

    # Second Solution
    return sum([x*y for x,y in zip(a,b)])