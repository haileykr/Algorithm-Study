'''
상호 평가

programers.co.kr/learn/courses/30/lessons/83201

08/24/21
'''

def solution(scores):
    answer = ''
    num = len(scores)
    
    for i in range(num):
        col = []
        for row in scores:
            col.append(row[i])
        if (col[i] == max(col) or col[i] == min(col)) and col[i] not in col[:i] + col[i+1:]:
            answer += grade(sum(col[:i] + col[i+1:]) // (len(col) - 1))
        else:
            answer += grade(sum(col) // len(col))

    return answer

def grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score>=70: return 'C'
    elif score>=50: return 'D'
    else: return 'F'