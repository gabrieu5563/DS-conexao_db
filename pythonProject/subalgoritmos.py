def getId(id : int, inst_consulta) -> bool:
    lista_id = []

    inst_consulta.execute("SELECT Id FROM petshop")
    data = inst_consulta.fetchall()
    lista_id = [item[0] for item in data]

    return id in lista_id