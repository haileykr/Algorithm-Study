"""
나머지 1인 수

https://programmers.co.kr/learn/courses/30/lessons/87389

"""


def solution(n):
    result = isPrimeNumber(n-1)
    return n-1 if result == -1 else result


def isPrimeNumber(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return i
    return -1
