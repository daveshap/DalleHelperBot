import re
import openai
from time import time,sleep


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


openai.api_key = open_file('openaiapikey.txt')


def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=100, freq_pen=0.0, pres_pen=0.0, stop=['CUSTOMER:', 'ALL DONE']):
    max_retry = 5
    retry = 0
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    while True:
        try:
            response = openai.Completion.create(
                #engine=engine,
                model='davinci:ft-david-shapiro:dalle-assistant-2022-07-18-12-57-53',
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response['choices'][0]['text'].strip()
            text = re.sub('\s+', ' ', text)
            filename = '%s_gpt3.txt' % time()
            save_file('gpt3_logs/%s' % filename, prompt + '\n\n==========\n\n' + text)
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                return 'GPT3 error: %s' % oops
            print('Error communicating with OpenAI:', oops)
            print(prompt)
            exit()
            sleep(1)


if __name__ == '__main__':
    conversation = ['DALLE: What can I make for you today?']
    print('DALLE: What can I make for you today?')
    while True:
        a = input('CUSTOMER: ')
        conversation.append('CUSTOMER: %s' % a)
        block = '\n'.join(conversation) + '\n'
        completion = gpt3_completion(block)
        #response = 'DALLE: %s' % completion
        response = completion
        print(response)
        conversation.append(response)
        