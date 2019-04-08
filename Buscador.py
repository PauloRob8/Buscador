from bs4 import BeautifulSoup
import requests

def main():

    url = input("Digite seu link:")
    palavra = input("Digite a palavra:")
    profundidade = int(input("Digite a profundidade da busca:"))

    response = requests.get(url)
    html = BeautifulSoup(response.text,'lxml')
    links = html.find_all(palavra)

    for link in links:
        if(str(link["href"]).startswith("http")):
            print(link['href'])

def get_palavra(url,palavra):

    response = requests.get(url)


if __name__ == '__main__':
    main()
