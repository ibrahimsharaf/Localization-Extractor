import json
import codecs
import glob
import itertools
import os

from collections import Counter


def parse_singles(filename, language):
    """
    Parse single localization settings
    """
    data = [line.strip() for line in open(filename, 'r')]
    d = dict(itertools.zip_longest(*[iter(data)] * 2, fillvalue=""))
    with open(language+'.json', 'w', encoding='utf-16') as file:
        json.dump(d, file, ensure_ascii=False)


def get_all_localization_data(path):
    """
    Collect all keys and values from localization json files
    """
    keys = []
    values = []
    files = glob.glob(path)
    for file in files:
        loc_dict = json.load(codecs.open(file, 'r', encoding='utf-16'))
        keys += list(loc_dict.keys())
        values += list(loc_dict.values())
    keys =[key.strip().lower() for key in keys]
    values = [value.strip().lower() for value in values]
    keys_file = open('keys.txt', 'w', encoding='utf-16')
    for key in keys:
        keys_file.write("%s\n" % key)
    vals_file = open('values.txt', 'w', encoding='utf-16')
    for val in values:
        vals_file.write("%s\n" % val)
    return


def hits_score(hits_path, locals_path):
    hits_lines = open(hits_path, encoding='utf-8').read().split("\n")
    local_lines = open(locals_path, encoding='utf-16').read().split("\n")

    intersection = list((Counter(hits_lines) & Counter(local_lines)).elements())
    bp_set = set(intersection)
    hits_set = set(hits_lines)
    without_bp = hits_set - bp_set
    with open('results.txt', 'w', encoding='utf-16') as f:
        [f.write(i + '\n') for i in bp_set]
    score = len(bp_set)/len(hits_set) * 100
    return str(round(score,2))


def find_boilerplates(keywords):
    hits = []
    keywords = keywords.lower().strip()
    for file in os.listdir('localizations'):
        file = os.path.abspath(os.path.join('localizations', file))
        loc_dict = json.load(codecs.open(file, 'r', encoding='utf-16'))
        for key, value in loc_dict.items():
            if all(sub in key.lower() for sub in keywords.split()) or all(sub in value.lower() for sub in keywords.split()):
                hits.append((key.strip(), value.strip()))
    return hits


if __name__ == "__main__":
    print(find_boilerplates('like post'))
