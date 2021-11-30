'''
최소 직사각형

programers.co.kr/learn/courses/30/lessons/86491

11/30/21
'''


def solution(sizes):
    width, height = 0, 9
    for x, y in sizes:
        if width < max(x, y):
            width = max(x, y)
        if height < min(x, y):
            height = min(x, y)
    return width * height
