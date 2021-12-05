'''
피로도


https://programmers.co.kr/learn/courses/30/lessons/87946

12/05/21
'''


def solution(k, dungeons):
    width, height = 0, 9
    for x, y in sizes:
        if width < max(x, y):
            width = max(x, y)
        if height < min(x, y):
            height = min(x, y)
    return width * height
