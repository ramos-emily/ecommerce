import pandas as pd
import os

data = {
    'tituloProduto': ['furadeira', 'parafusadeira'],
    'preco': [500, 250],
    'descricao': ['furar paredes', 'parafusar coisas'],
    'imgProduto': ['/images', '/images'],
    'categoriaProduto': ['ferramentas', 'ferramentas'],
    'classProduto': ['manual', 'manual'],
    'exibirHome': [True, False]
}

df = pd.DataFrame(data)

caminho_atual = os.getcwd()
caminho_final = caminho_atual.replace('\\', '/')

df.to_csv(caminho_final+'/data/ferramentas.csv', index=False)

print(caminho_atual)