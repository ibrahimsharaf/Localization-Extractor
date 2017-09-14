# -*- coding: utf-8 -*-
import json
import codecs

def merge(filename1, filename2, language):
    dict1 = json.load(codecs.open(filename1, 'r', encoding='utf-16'))
    dict2 = json.load(codecs.open(filename2, 'r', encoding='utf-16'))
    out = dict(list(dict1.items()) + list(dict2.items()))
    with open(language+'.json', 'w', encoding='utf-16') as f:
        json.dump(out, f, ensure_ascii=False)

merge('/home/ibrahimsharaf/Desktop/NewForums/phpBB/singles/portuguese.json'
      , '/home/ibrahimsharaf/Desktop/NewForums/phpBB/portuguese.json', 'portuguese')