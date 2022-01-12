import requests
from bs4 import BeautifulSoup

def loto():
             headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
             headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}


             url = 'https://www.google.com/search?q=lotofacil 2180'

             req = requests.get(url, headers = headers)

             sp = BeautifulSoup(req.content, 'html.parser')

             htmlE = sp.find('div', attrs={'class': 'ULSxyf'})

             '''######***_*****___-------------- PARTE 2 _________-------------***####### '''

             dt = htmlE.find('span', attrs={'class': 'qLLird'})

             data = dt.text[15:23]
             concurso = dt.text[9:13]
             
             url2 = f'https://www.google.com/search?q=que%20dia%20foi%20{data}'

             
             req2 = requests.get(url2, headers = headers2) # Requisição 2
             sp2 = BeautifulSoup(req2.content, 'html.parser') # logo em seguinda Bfs2

             resul2 = sp2.find('div', attrs={'class': 'vk_bk dDoNo FzvWSb XcVN5d'})
             resull2 = sp2.find('div', attrs={'class': 'vk_gy vk_sh'})
             
             print(concurso)
             print(resull2.text)

             


             '''######***_*****___-------------- FIM PARTE 2 _________-------------***####### '''


             resul = htmlE.find('div', attrs={'class': 'Z30kQd'})
             r = resul.text

             print(data)

             print(r[:2:1],r[2:4:1] , r[4:6:1] , r[6:8:1] , r[8:10:1] , r[10:12:1] , r[12:14:1] , r[14:16:1] , r[16:18:1] , r[18:20:1] , r[20:22:1], r[22:24:1], r[24:26:1], r[26:28:1], r[28:30:1])


loto()
