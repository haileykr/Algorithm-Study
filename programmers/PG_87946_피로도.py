'''
피로도


https://programmers.co.kr/learn/courses/30/lessons/87946

12/05/21
'''


import itertools


def solution(k, dungeons):
    answer = 0
    dungeonsList = list(itertools.permutations(dungeons))
    for perm in dungeonsList:
        currK, curr = k, 0
        for x, y in perm:
            if currK >= x:
                currK -= y
                curr += 1
        if curr > answer:
            answer = curr

    return answer
