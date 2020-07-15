import jsonlines
import re
import os
import random


def get_jl_data(file_path:str) -> list:
    '''读取jl文件'''
    result = []
    with jsonlines.open(file_path, 'r') as f:
        for line in f:
            result.append(line)
    return result

def export_unique_data(file_path):
    jl_data_list = get_jl_data(file_path)
    links = set()

    with jsonlines.open(file_path + '_unique', mode='w') as writer:
        for data in jl_data_list:
            if data['url'] in links:
                print(data['url'] + ' exists')
                continue
            else:
                links.add(data['url'])
                writer.write(data)

# cnn的爬取结果需要去重, www.cnn.com和edition.cnn.com中的新闻可能重复，也可能重新定向
def export_unique_cnn(file_path):
    jl_data_list = get_jl_data(file_path)
    links = set()

    with jsonlines.open(file_path + '_unique', mode='w') as writer:
        for data in jl_data_list:
            url = re.sub(r'www.cnn.com', 'edition.cnn.com', data['url'])
            if url in links:
                print(data['url'] + ' exists')
                continue
            else:
                links.add(url)
                writer.write(data)

def random_sampling(file_path:str, sample_number:int=100):
    jl_data_list = get_jl_data(file_path)
    titles = []
    for data in jl_data_list:
        titles.append(data['title'])

    return random.choices(titles, k=sample_number)