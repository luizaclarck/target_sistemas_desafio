def inverte_nome(nome):
    lista = list(nome)
    ultima_posicao = len(lista) - 1
    novo_nome = ''
    for x in lista:
        novo_nome += lista[ultima_posicao]
        ultima_posicao -= 1
        
    print(novo_nome)

inverte_nome('luiza')
