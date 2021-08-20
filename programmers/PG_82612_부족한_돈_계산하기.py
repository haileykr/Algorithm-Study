'''
돈 계산
https://programmers.co.kr/learn/courses/30/lessons/82612
08/2021
'''

def solution(price, money, count):
    mult = 0
    for i in range(1, count+1): mult += i
    remainder = money - price*mult

    return 0 if remainder >= 0 else -remainder