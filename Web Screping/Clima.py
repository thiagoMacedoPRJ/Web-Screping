import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}


def clima():
             print("")

             a = input('Qual localização você quer saber?: ')
                          
             url = f'https://www.google.com/search?q=clima de {a}'

             req = requests.get(url, headers = headers)

             Beaut = BeautifulSoup(req.content, 'html.parser')

             try:
                          resultado = Beaut.find('div', attrs={'class': 'vk_bk TylWce'})

                          rs = resultado.find('span')

                          cl =  Beaut.find('div', attrs={'class': 'wtsRwe'})

                          lct =  Beaut.find('div', attrs={'class': 'wob_loc mfMhoc'})

                          data = Beaut.find('div', attrs={'class': 'wob_dts'})

                          tempo =  Beaut.find('div', attrs={'class': 'wob_dcp'})
             except:
                          print("")
                          print(f"ERRO AO TENTAR ENCONTRAR: {a}")
                          return clima()

             print("")

             print(f"Clima de {a}: {rs.text} °C, {tempo.text}")

             print("")

             print(f"Previsão de {cl.text.replace('%', '%, ')}")

             print(f"Localização atual: {lct.text}")

             print(f"Data: {data.text}")
             return clima()

clima()
