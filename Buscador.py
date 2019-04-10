from bs4 import BeautifulSoup
import requests
import re

def main():

    url = input("Digite seu link:")
    palavra = input("Digite a palavra:")
    profundidade = int(input("Digite a profundidade da busca:"))

    #response = requests.get(url)
    #html = BeautifulSoup(response.text ,'lxml')
    #links = html.find_all('a')


    #for link in links:
        #if(str(link["href"]).startswith("http")):
            #print(link['href'])

    get_palavra(url,palavra)

def get_palavra(url,palavra):

    try:

        response = requests.get(url)
        text = BeautifulSoup(response.text, 'lxml').text
        encontradas = re.findall('\w*.{0,11}' + palavra + '.{0,11}\w*', text, re.IGNORECASE)
        for palavra in encontradas:
            print('----' + palavra + '----')

    except:
        print("Link inválido")
        pass

def clear(text):

    body = text.body


if __name__ == '__main__':
    main()
