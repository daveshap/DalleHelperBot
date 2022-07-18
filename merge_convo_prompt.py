import os


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


if __name__ == '__main__':
    files = os.listdir('convos/')
    for file in files:
        convo = open_file('convos/%s' % file)
        prompt = open_file('prompts/%s' % file)
        result = convo + '\nCUSTOMER: ALL DONE\nDALLE: %s' % prompt
        save_file('final_output/%s' % file, result)