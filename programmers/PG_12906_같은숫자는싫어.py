def solution(arr):
    answer = [arr[0]]
    for number in arr[1: ]:
        if number != answer[-1]:
            answer.append(number)
    return answer