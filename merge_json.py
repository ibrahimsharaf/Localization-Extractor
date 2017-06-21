import json


def merge(filename1, filename2, language):
    json_data1 = open(filename1).read()
    dict1 = json.loads(json_data1)
    json_data2 = open(filename2).read()
    dict2 = json.loads(json_data2)
    out = dict(list(dict1.items()) + list(dict2.items()))
    with open(language+'.json', 'w') as f:
        json.dump(out, f)

merge('/home/ibrahimsharaf/Desktop/myBBLocalization/english.json'
      , '/home/ibrahimsharaf/Desktop/vblocalization/English.json', 'English')