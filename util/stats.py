from jl_utility import get_jl_data
import jsonlines
import os, glob
import re
import time

site_names_dict = {
    'abcnews'   : '美国广播公司(abc_us)',
    'bbcnews'   : '英国广播公司(bbc_uk)',
    'cbsnews'   : '哥伦比亚广播公司(cbs_us)',
    'cnn'       : 'cnn_us',
    'foxnews'   : '福克斯新闻网(foxnews_us)',
    'mirror'    : '镜报(mirror_uk)',
    'npr'       : '美国国家公共广播电台(npr_us)',
    'nytimes'   : '纽约时报(nytimes_us)',
    'tass_ru'   : '俄联社-塔新社(tass_ru)',
    'thetimes'  : '泰晤士报(times_uk)',
    'usatoday'  : '今日美国(usatoday_us)',
    'washingtonpost': '华盛顿邮报(washingtonpost_us)'
}

def get_stats(filepath, field='pub_date', start_date='2020-06-05', end_date='', sort=True):
    '''读取一个jl文件，然后根据field统计文章数量, 返回格式dict<tuple<field:str, num:int>>'''
    stats = {}
    if end_date == '': 
        end_date = time.strftime("%Y-%m-%d", time.localtime())

    for article in get_jl_data(filepath):
        pub_date = article[field]
        if pub_date < start_date and pub_date <= end_date:
            continue
        
        if stats.__contains__(pub_date):
            stats[pub_date] += 1
        else:
            stats[pub_date] = 1

    if sort:
        sorted_stats = sorted(stats.items(), reverse=True)
        return sorted_stats
    else:
        return stats

def get_average(stats:dict) -> float:
    total = 0.0
    for s in stats:
        total += s[1]
    return total / len(stats)

def export_jl_stats():
    files = glob.glob('*.jl')
    files.remove('default.jl')
    with jsonlines.open('util/stats.jl', 'w') as writer:
        for file in files:
            stats = get_stats(file)
            values = []
            for s in stats:
                values.append(s)
            writer.write({"site":file, "stats": values})
    print('export stats done')
    return

def main():
    files = glob.glob('*.jl')
    files.remove('default.jl')
    with open('util/stats.txt', 'w', encoding='utf-8') as f:
        for file in files:
            stats = get_stats(file)
            average = get_average(stats)
            site_name = re.split(r'\.', file)[0]
            f.write("%s每日爬取新闻数量统计结果(2020-06-05至今): \n" % site_names_dict[site_name])
            f.write("每日平均: %.2f \n" % average)
            for s in stats:
                f.write(str(s) + '\n')

# export_jl_stats()
# jl_data = get_jl_data('util/stats.jl')
# print(jl_data[0]['site'])
# print(jl_data[0]['stats'])