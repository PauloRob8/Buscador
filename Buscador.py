from bs4 import BeautifulSoup
import requests
import requests_cache
import re


def main():
    url = input("Digite seu link:")
    palavra = input("Digite a palavra:")
    profundidade = int(input("Digite a profundidade da busca:"))

    get_deep_link(url, palavra, profundidade)


def get_palavra(url, palavra):
    try:

        response = requests.get(url)
        text = BeautifulSoup(response.text, 'lxml').text
        encontradas = re.findall('\w*.{0,11}' + palavra + '.{0,11}\w*', text, re.IGNORECASE)

        return encontradas

    except:

        pass


def get_deep_link(url, palavra, profundidade):
    links = []
    palavras = []

    auxiliar = 0
    profundidade = profundidade - 1

    requests_cache.install_cache('cache')

    if profundidade == -1:

        palavras.append(get_palavra(url, palavra))

    else:

        links.append(get_links(url))

        while auxiliar < profundidade:

            for i in range(len(links[auxiliar])):
                links.append(repetido(get_links(links[auxiliar][i]), links))

            auxiliar += 1

        palavras.append(get_palavra(url, palavra))

        for i in range(len(links)):

            for j in range(len(links[i])):
                palavras.append(get_palavra(links[i][j], palavra))

    print_relevancia(url, links, palavras)


def get_links(url):
    try:

        response = requests.get(url)
        html = BeautifulSoup(response.text, 'lxml')
        links_pagina = html.find_all('a')

        links = []

        for i in links_pagina:

            if (i.get('href') != None and str(i["href"]).startswith("http") and not str(i["href"]).endswith("pdf")):

                if (i["href"] not in links):
                    links.append(i.get('href'))

        return links


    except:

        pass


def clear(text):
    body = text.body


def repetido(link, links):
    link_formatado = []

    for j in range(len(link)):

        contador = 0
        cont_auxiliar = 0

        while contador < len(links):

            if link[j] not in links[contador]:
                cont_auxiliar = cont_auxiliar

            else:
                cont_auxiliar += 1

            contador += 1

        if (cont_auxiliar == 0):
            link_formatado.append(link[j])

    return link_formatado


def print_relevancia(url, links, palavras):
    novo_vetor_link = []

    contador = 1
    nivel_relevancia = ''

    for i in range(len(links)):

        for j in range(len(links[i])):
            novo_vetor_link.append(links[i][j])

    print("O 1° link ", url, "tem no total de ", len(palavras[0]), " encontradas.\n")

    while contador < len(novo_vetor_link):

        if len(palavras[contador]) == 0:
            nivel_relevancia = "Busca irrelevante"

        elif len(palavras[contador]) > 0 and len(palavras[contador]) < 10:
            nivel_relevancia = "Busca pouco relevante"

        elif len(palavras[contador]) >= 10 and len(palavras[contador]) < 25:
            nivel_relevancia = "Busca relevante"

        elif len(palavras[contador]) >= 25:
            nivel_relevancia = "Busca muito relevante"

        print("O " + str(contador + 1) + "° link " + str(novo_vetor_link[contador]) + "tem no total de " + str(
            len(palavras[contador])) + " palavras encontradas. " + nivel_relevancia + "\n")

        contador += 1


if __name__ == '__main__':
    main()