import requests, os, bs4
url = 'http:// xkcd.com' #url inicial
os.makedirs('xkcd', exist_ok = True) #armazena as tirnhas em ./xkdc
while not url.endswith('#'):
    #faz download da pagina.
    print('downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)