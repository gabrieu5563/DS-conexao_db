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
    inst_consulta = conn.cursor()
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
2 - Exibir dados 
3 - Editar pet - apertar enter pra deixar do jeito q ta - mostrar o animal que está sendo editado
4 - Excluir pet
5 - Excluir todos os pets
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

            case 2:
                lista_dados = []
                inst_consulta.execute("SELECT * FROM petshop")
                data = inst_consulta.fetchall() #pega todos os registros e joga no objeto data

                for i in data:
                    lista_dados.append(i)
                lista_dados = sorted(lista_dados)

                dados_df =pd.DataFrame.from_records(lista_dados, columns=['Id', 'Tipo', 'Nome', 'Idade'], index='Id')

                if dados_df.empty:
                    print("Não há pets cadastrados")
                else:
                    print(dados_df)
                os.system("pause")

            case 3:
                #editar pet
                id = input("Digite o id do pet que será editado: ")
                inst_consulta.execute("SELECT Id FROM petshop")
                data = inst_consulta.fetchall()
                if id in data:
                    inst_consulta.execute(f"SELECT * FROM petshop WHERE Id = '{id}'")
                    data = inst_consulta.fetchall()
                    print(data)
                else:
                    print("a")

            case _:
                print("Opção inválida")