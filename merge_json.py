# -*- coding: utf-8 -*-
import json
import codecs
import os


def merge(filename1, filename2, language):
    dict1 = json.load(codecs.open(filename1, 'r', encoding='utf-16'))
    dict2 = json.load(codecs.open(filename2, 'r', encoding='utf-16'))
    out = dict(list(dict1.items()) + list(dict2.items()))
    with open(language+'.json', 'w', encoding='utf-16') as f:
        json.dump(out, f, ensure_ascii=False)


def get_files(directory1, directory2):
    def get_files_from_directory(dir_name):
        child_files = []
        for path, subdirs, files in os.walk(dir_name):
            language = os.path.basename(path)
            for name in files:
                child_files.append(path+'/'+name)
        return child_files
    files1 = get_files_from_directory(directory1)
    files2 = get_files_from_directory(directory2)
    for file1 in files1:
        for file2 in files2:
            if file1.split('/')[-1] == file2.split('/')[-1]:
                merge(file1, file2, file1.split('/')[-1].split('.')[0])

get_files('/home/ibrahimsharaf/Desktop/NewForums/xen+phpbb+vb', '/home/ibrahimsharaf/Desktop/NewForums/myBB')
