import json
from collections import Counter


def hits_score(hit_path, local_path):
    hits_lines = open(hit_path).read().split("\n")
    local_data = open(local_path).read()
    d = json.loads(local_data)
    local_lines = []
    for key, value in d.items():
        local_lines.append(value)

    intersection = list((Counter(hits_lines) & Counter(local_lines)).elements())
    print(intersection)
    print(len(intersection))
    print(len(hits_lines))
    score = len(intersection)/len(hits_lines) * 100
    return score


hit='/home/ibrahimsharaf/Desktop/hittext_sample/'
loc='/home/ibrahimsharaf/Desktop/merged/'
print(hits_score(hit+'french.txt', loc+'French.json'))
