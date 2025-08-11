from collections import Counter

def solution(participant, completion):
    count = Counter(participant)
    for name in completion:
        count[name] -= 1
        if count[name] == 0:
            del count[name]
    return list(count.keys())[0]

from collections import Counter

def solution(participant,completion):
    diff = Counter(participant) - Counter(completion)
    return list(diff.keys())[0]