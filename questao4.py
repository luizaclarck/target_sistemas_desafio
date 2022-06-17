def calculaPorcentagem(valorTotal, valorEstado, estado):
    porcentagem = valorEstado * 100 / valorTotal 
    print(f'O percentutal de {estado} é igual a: {porcentagem:.2f}%')

estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

valorTotal = 0

for estado in estados:
    valorTotal += estados[estado]
    
for estado in estados:
    calculaPorcentagem(valorTotal, estados[estado], estado)
