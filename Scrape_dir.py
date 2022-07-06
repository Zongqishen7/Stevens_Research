from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
# import requests package
import requests
import os
import codecs
# import BeautifulSoup from package bs4 (i.e. beautifulsoup4)
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
from urllib.request import Request, urlopen
import pandas as pd
import nltk

# Scrpae word dir on web
def download_evinwords (url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all("ol", {"class": "section-col list-unstyled"})
    words = []

    for div in divs:
        for i in div.find_all("li"):
            words.append(i.get_text())

    f = open('name.txt', mode='w')  # 打开文件，若文件不存在系统自动创建。
    for i in words:
        f.write(i + "\n")
    f.close()

url = 'https://www.words-to-use.com/words/going-green/'
download_evinwords(url)



# open fle as list
def open_file(path):
    pattern=r'\w[\w\',-]*\w'
    with open(path,'r') as f:
        envir = [line.strip() for line in f]
    envir = " ".join(envir)
    envir=nltk.regexp_tokenize(envir.lower(), pattern)
    return envir

path = "/Users/shenzongqi/Desktop/PythonProject/Stevens/2022_Research/envir_words.txt"
open_file(path)







