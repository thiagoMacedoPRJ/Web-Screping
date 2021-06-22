import requests
from bs4 import BeautifulSoup

def pesqui():
    print("")
    pesquisa =  str(input('O QUE ESTÁ PROCURANDO?: '))

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

    url = f'https://www.google.com/search?q={pesquisa}'

    r =  requests.get(url, headers = headers)

    soup = BeautifulSoup(r.content, 'html.parser')

    html = soup.find('div', attrs={'class': 'I6TXqe osrp-blk'})

    try:
        resul = html.find('h2', attrs={'class': 'qrShPb kno-ecr-pt PZPZlf mfMhoc'})
        resull = html.find('div', attrs={'class': 'kno-rdesc'})
        resulll = resull.find('span')
    except:
        
        print("")
        print('RESULTADO {} NÃO ENCONTRADO!!'.format(pesquisa))
        return pesqui()

    print("")
    print(resul.text.upper(), resulll.text)
    return pesqui()


pesqui()
