import pandas as pd
import os
import sqlite3

conn = sqlite3.connect('db.sqlite3')

caminho_atual = os.getcwd()
caminho_final = caminho_atual.replace('\\', '/')

df = pd.read_csv(caminho_final+'/data/ferramentas.csv')

df.columns =['tituloProduto', 'preco', 'descricao', 
             'imgProduto', 'categoriaProduto', 
             'classProduto', 'exibirHome']

df.to_sql('api_produto', conn, if_exists='append', index=False )

conn.close()

print('dados inseridos com sucesso! :)')