'''
신고 결과 받기

- programmers.co.kr/learn/courses/30/lessons/92334

08/28/22
'''
def solution(id_list, report, k):
    report_sets = {}
    answer = {}
    for id_name in id_list:
        answer[id_name] = 0
        report_sets[id_name] = set()
    for report_detail in report:
        [reporter, reportee] = report_detail.split(" ")
        report_sets[reportee].add(reporter)
    
    for report_sets_item in list(report_sets.values()):
        if len(report_sets_item) >= k:
            for reportee in report_sets_item:
                answer[reportee] += 1

    return list(answer.values())