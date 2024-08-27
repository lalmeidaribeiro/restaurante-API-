import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url) #get verbo do http para solicitar alguns recuros 
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {} #Separar as informações por restaurante 

    for item in dados_json:#Acesso os dados do json 
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante: #Se o nome do restaurante não estiver na lista restaurante faça
            #Olhe com o os dados estão vindo da API - Nessa caso os dados estão dentro de uma lista e dentro da lista um dicionário 
            dados_restaurante[nome_do_restaurante] = [] #Ou seja, se não tiver, eu estou colocando dentro da lista a lista com as infos do restaurante na linha abaixo
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
else:
    print(f'O erro foi: {response.status_code}')

#salvando o cardápio do restaurnate em um arquivo .txt ou .json com o nome do restaurante
for nome_do_restaurante, dados in  dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante: #estou abrindo o arquivo que adicionei na minha váriavel nome_do_arquivo. Apos a virgula eu passo a letra do que qr que seja feito, nesse caso, quero escreverver.
        json.dump(dados,arquivo_restaurante,indent=4)