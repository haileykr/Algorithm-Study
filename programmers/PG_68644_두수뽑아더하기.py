"""
두 수 뽑아 더하기 

https://programmers.co.kr/learn/courses/30/lessons/68644 
"""


def solution(numbers):
    answer = set()
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    answerList = list(answer)
    answerList.sort()
    return answerList
