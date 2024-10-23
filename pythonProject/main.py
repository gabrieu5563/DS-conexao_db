import pyodbc
import pandas as pd
import os

os.system("cls")
try:
    server = 'localhost'
    database = 'petshop'
    username = 'sa'
    password = '*123456HAS*'

    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    list_cadastro = conn.cursor()
except Exception as e:
    print(f"Erro: {e}")
    conexao = False
else:
    conexao = True
    print("Conectado")