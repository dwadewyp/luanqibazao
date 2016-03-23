__author__ = 'wyp'
import jieba
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand


def extract_text(url):
    page_source = requests.get(url).content
    bs_source = BeautifulSoup(page_source)
    report_text = bs_source.find_all('p')

    text = ''

    for p in report_text:
        text += p.get_text()
        text += '\n'

    return text




def word_frequency(text):
    from collections import Counter

    words = [word for word in jieba.cut(text,cut_all=True) if len(word) >= 2]
    c = Counter(words)

    for word_freq in c.most_common(10):
        print word_freq,type(word_freq),"word_freq"
        word, freq = word_freq
        print(word,freq)


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         url = 'http://www.gov.cn/guowuyuan/2016-03/05/content_5049372.htm'
#         text = extract_text(url)
#         word_frequency(text)

if __name__ == '__main__':
    url = 'http://www.gov.cn/guowuyuan/2016-03/05/content_5049372.htm'
    text = extract_text(url)
    word_frequency(text)