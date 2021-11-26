"""
3진법 뒤집기
https://programmers.co.kr/learn/courses/30/lessons/68935
"""


def solution(n):
    answer = terToDec(decToTerReversed(n))
    return answer


def decToTerReversed(num):
    if num < 3:
        return str(num)
    converted = ''
    while num >= 3:
        q, r = divmod(num, 3)
        converted += str(r)
        num //= 3
    converted += str(q)
    return converted


def terToDec(num):
    answer = 0
    x = len(num) - 1
    for i in num:
        answer += int(i) * 3**x
        x -= 1
    return answer

# Second Solution
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n //= 3
    answer = int(tmp, 3)
    return answer