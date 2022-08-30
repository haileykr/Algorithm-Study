'''
성격 유형 검사


- https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3

08/29/22
'''


def solution(survey, choices):
    answer = ''
    counts = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i, choice in enumerate(choices):
        if choice == 1:
            counts[survey[i][0]] += 3
        elif choice == 2:
            counts[survey[i][0]] += 2
        elif choice == 3:
            counts[survey[i][0]] += 1
        elif choice == 5:
            counts[survey[i][1]] += 1
        elif choice == 6:
            counts[survey[i][1]] += 2
        elif choice == 7:
            counts[survey[i][1]] += 3

    answer += "R" if counts["R"] >= counts["T"] else "T"
    answer += "C" if counts["C"] >= counts["F"] else "F"
    answer += "J" if counts["J"] >= counts["M"] else "M"
    answer += "A" if counts["A"] >= counts["N"] else "N"

    return answer
