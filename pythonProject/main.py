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
    inst_cadastro = conn.cursor() #objeto utilizado pra fazer instrução sql
except Exception as e:
    print(f"Erro: {e}")
    conexao = False
else:
    conexao = True
    print("Conectado")

while conexao: #só entra se conexao for true
    os.system("cls")

    print("""
MENU
0 - SAIR
1 - Cadastrar pets
        """)
    ex = input("Escolha uma opção: ")
    try:
        ex = int(ex)
    except ValueError:
        print("Opção inválida.")
    else:
        match ex:
            case 0:
                conexao = False

            case 1:
                try:
                    tipo = input("Tipo.....")
                    nome = input("Nome.....")
                    idade = int(input("Idade....."))

                    cadastro = f"""
                            INSERT INTO petshop (tipo_pet, nome_pet, idade)
                            VALUES ('{tipo}', '{nome}', '{idade}')
                        """

                    inst_cadastro.execute(cadastro)
                    conn.commit()
                except ValueError:
                    print("Digite uma idade válida")
                except e:
                    print(f"Erro em alguma transação da tabela {e}")
                else:
                    print("Dados gravados com sucesso")

            case _:
                print("Opção inválida")