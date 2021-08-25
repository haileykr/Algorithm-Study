'''
직업군 추천

programers.co.kr/learn/courses/30/lessons/84325

08/26/21
'''


def solution(table, languages, preference):
    scoreTable = {}
    scores = []

    for element in table:
        job, lang5, lang4, lang3, lang2, lang1 = element.split(' ')
        scoreTable[job] = ['', lang1, lang2, lang3, lang4, lang5]

    for job in scoreTable:
        score = 0
        for i in range(len(languages)):
            if languages[i] in scoreTable[job]:
                score += scoreTable[job].index(languages[i]) * preference[i]
        scores.append([score, job])

    scores.sort(key=lambda x: [-x[0], x[1]])

    return scores[0][1]
