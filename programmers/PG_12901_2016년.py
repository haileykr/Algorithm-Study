def solution(a, b):
    weekdays = ["FRI",
                "SAT",
                "SUN",
                "MON",
                "TUE",
                "WED",
                "THU"]
    numOfDays = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    currDays = sum(numOfDays[:a]) + b

    return weekdays[(currDays-1) % 7]
