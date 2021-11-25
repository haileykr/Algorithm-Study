"""
숫자문자열 및 영단어


https://programmers.co.kr/learn/courses/30/lessons/81301 
"""


def solution(s):
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    i = 0
    answer = ''
    while i < len(s):
        if s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            answer += str(s[i])
            i += 1
        else:
            j = i + 2
            while True:
                if s[i:j] in dic:
                    answer += str(dic[s[i:j]])
                    i = j
                    break
                else:
                    j += 1
    return int(answer)


# Second Solution
def solutions(s):
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    answer = s
    for key, value in dic.items():
        answer = answer.replace(key, value)

    return int(answer)
