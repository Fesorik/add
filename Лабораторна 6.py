
from bs4 import BeautifulSoup
import requests


def countWords(string, words = {}):
    for word in string.split(' '):
        if not word in words:
            words[word] = 1
            continue

        words[word] += 1
    
    return words
request = requests.get('https://techrocks.ru/2018/01/20/programmers-blogs/')


if not request.ok:
    print('Eequest failed:', request.status_code)
else:
    page = BeautifulSoup(request.text, 'html.parser')
    paragraph = page.select('#post-content-body > div p')
    words = {}
    for string in paragraph:
        words = countWords(string.get_text(), words)
    
    aEls = page.select('a')
    picEls = page.select('img')


    print('Frequency - ', words)
    print('Paragraph - ', len(paragraph))
    print('Links - ', len(aEls))
    print('Pictures - ', len(picEls))