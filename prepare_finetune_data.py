import os
import json


src_dir = 'final_output/'


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


if __name__ == '__main__':
    files = os.listdir(src_dir)
    data = list()
    for file in files:
        info = open_file(src_dir + file)
        lastline = info.splitlines()[-1]
        info = info.replace(lastline, '')
        info = {'prompt': info, 'completion': lastline}
        data.append(info)
    with open('dalle.jsonl', 'w') as outfile:
        for i in data:
            json.dump(i, outfile)
            outfile.write('\n')