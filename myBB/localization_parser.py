import re
import codecs
import itertools
import os
import json


def parse_one_file(filename):
    """
    Parses localization values given a file
    :param filename: configurations file path
    :return: dict of key (English term) -> value (given language term)
    """
    with codecs.open(filename, "r",encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        lines = [x.strip() for x in lines]

    values = []
    for i in lines:
        quoted = re.findall(r"['\"](.*?)['\"]", i)
        if quoted and len(quoted) == 2:
            values = values + quoted

    d = dict(itertools.zip_longest(*[iter(values)] * 2, fillvalue=""))
    return d


def get_all_files(directoryname):
    """
    Gets all configurations files inside a directory, parses them using parse_one_file function
    :param directoryname: an arbitrary language file
    :return: dict of all localization values
    """
    files_name = []
    localization_values = {}
    for filename in os.listdir(directoryname):
        localization_values.update(parse_one_file(directoryname+'/'+filename))
    return localization_values


def main():
    path = '/home/ibrahimsharaf/Desktop/MyBB/english'
    d = (get_all_files(path))
    with open('english.json', 'w') as f:
        json.dump(d, f)


if __name__ == "__main__":
    main()

