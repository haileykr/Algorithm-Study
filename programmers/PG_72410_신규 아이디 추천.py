"""
신규 아이디 추천

문자열 치환 문제


https://programmers.co.kr/learn/courses/30/lessons/72410
"""

import re


def solution(new_id):
    answer = new_id.lower()
    answer = re.sub("[^a-z0-9\-_.", "", answer)
    answer = re.sub("\.+", ".", answer)
    answer = re.sub("^[.]|[.]$", "", answer)
    answer = "a" if len(answer) == 0 else answer[:15]
    answer = re.sub("[.]$", "", answer)
    while len(answer) > 0 and len(answer) < 3:
        answer += answer[-1]
    return answer
