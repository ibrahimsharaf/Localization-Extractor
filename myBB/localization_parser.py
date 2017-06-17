import re
import codecs
import itertools
import os
import json
import pathlib


def clean_html(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


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
        cleaned_text = clean_html(i)
        quoted_signle = re.findall(r"[\'](.*?)[\']", cleaned_text)
        quoted_double = re.findall(r"[\"](.*?)[\"]", cleaned_text)
        quoted = quoted_signle + quoted_double
        if quoted and len(quoted) == 2:
            values = values + quoted

    d = dict(itertools.zip_longest(*[iter(values)] * 2, fillvalue=""))
    return d


def get_all_files(directoryname):
    """
    Gets all configurations files inside a directory, parses them using parse_one_file function
    :param directoryname: directory
    :return: dumps localization dictionaries in JSON format
    """
    for path, subdirs, files in os.walk(directoryname):
        localization_values = {}
        language = os.path.basename(path)
        for name in files:
            file_name = pathlib.PurePath(path, name)
            localization_values.update(parse_one_file(file_name))
        print(len(localization_values))
        with open(language+'.json', 'w') as f:
            json.dump(localization_values, f)


def main():
    path = '/home/ibrahimsharaf/Desktop/MyBB'
    get_all_files(path)


if __name__ == "__main__":
    main()

