'''
Add + and -!

https://programmers.co.kr/learn/courses/30/lessons/76501

11/23/21
'''


def solutions(absolutes, signs):
    answer = 0
    for index, number in enumerate(absolutes):
        answer += number if signs[index] else -number
    return answer
