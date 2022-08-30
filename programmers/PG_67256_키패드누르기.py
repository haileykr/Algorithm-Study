"""
나머지 1인 수

https://school.programmers.co.kr/learn/courses/30/lessons/67256

"""


def solution(numbers, hand):
    answer = ""
    distance = {
        0: {2: 3, 5: 2, 8: 1, 0: 0},
        1: {2: 1, 5: 2, 8: 3, 0: 4},
        2: {2: 0, 5: 1, 8: 2, 0: 3},
        3: {2: 1, 5: 2, 8: 3, 0: 4},
        4: {2: 2, 5: 1, 8: 2, 0: 3},
        5: {2: 1, 5: 0, 8: 1, 0: 2},
        6: {2: 2, 5: 1, 8: 2, 0: 3},
        7: {2: 3, 5: 2, 8: 1, 0: 2},
        8: {2: 2, 5: 1, 8: 0, 0: 1},
        9: {2: 3, 5: 2, 8: 1, 0: 2},
        10: {2: 4, 5: 3, 8: 2, 0: 1},
        11: {2: 4, 5: 3, 8: 2, 0: 1}
    }

    # or could solve by saving coordinates
    # coordinates = {
    #   1: [0, 0], 2: [0, 1], 3: [0, 2],
    #   4: [1, 0], 5: [1, 1], 6: [1, 2],
    #   7: [2, 0], 8: [2, 1], 9: [2, 2],
    #   10: [3, 0], 0: [3, 1], 11: [3, 2]
    # }

    currLeftPosition = 10  # "*"
    currRightPosition = 11  # "#"

    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            currLeftPosition = number
        elif number in [3, 6, 9]:
            answer += "R"
            currRightPosition = number
        elif number in [2, 5, 8, 0]:
            leftDistance = distance[currLeftPosition][number]
            rightDistance = distance[currRightPosition][number]
            # numberCoord = coordinates[number]
            # leftCoord = coordinates[currLeftPosition]
            # rightCoord = coordinates[currRightPosition]

            # leftDistance = abs(leftCoord[0] - numberCoord[0]) + abs(leftCoord[1] - numberCoord[1])
            # rightDistance = abs(rightCoord[0] - numberCoord[0]) + abs(rightCoord[1] - numberCoord[1])

            if leftDistance < rightDistance or (leftDistance == rightDistance and hand == "left"):
                answer += "L"
                currLeftPosition = number
            else:
                answer += "R"
                currRightPosition = number
    return answer
