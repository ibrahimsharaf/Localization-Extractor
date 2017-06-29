import json
import itertools
from collections import Counter


def parse_singles(filename, language):
    data = [line.strip() for line in open(filename, 'r')]
    d = dict(itertools.zip_longest(*[iter(data)] * 2, fillvalue=""))
    with open(language+'.json', 'w') as file:
        json.dump(d, file)


def hits_score(hit_path, local_path, language):
    hits_lines = open(hit_path+language+'.txt').read().split("\n")
    local_data = open(local_path+language+'.json').read()
    d = json.loads(local_data)

    local_lines = []
    for key, value in d.items():
        local_lines.append(value)

    if language is not 'English':
        english_path = open('/home/ibrahimsharaf/Desktop/merged/English.json').read()
        english_dict = json.loads(english_path)
        for key, value in english_dict.items():
            local_lines.append(value)

    intersection = list((Counter(hits_lines) & Counter(local_lines)).elements())
    bp_set = set(intersection)
    hits_set = set(hits_lines)
    without_bp = hits_set-bp_set
    with open(language+'_hits.txt', 'w') as f:
        [f.write(i +'\n') for i in without_bp]
    score = len(bp_set)/len(hits_set) * 100
    return str(round(score,2))


def main():
    hits_path='/home/ibrahimsharaf/Desktop/hittext_sample/'
    localization_path='/home/ibrahimsharaf/Desktop/Localizations/'
    print(hits_score(hits_path, localization_path, 'English'))

if __name__ == "__main__":
    main()