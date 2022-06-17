import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

maior = 0
menor = 999999999
total_valores = 0
dias_validos = 0

for i in dados:
    if(i['valor'] != 0.0):
        dias_validos += 1
        if i['valor'] > maior:
            maior = i['valor']
        if (i['valor'] < menor):
            menor = i['valor']
        total_valores += i['valor']

media = total_valores / dias_validos
dias_mes_valor_maior_que_media = []

for i in dados:
    if (i['valor'] != 0.0):
        if (i['valor'] > media):
            dias_mes_valor_maior_que_media.append(i['dia'])


print(f'Maior valor: {maior:.2f}')
print(f'Menor valor: {menor:.2f}')
print(f'Média: {media:.2f}')
print(f'Dias do mês que tiveram um faturamente maior que a média: {dias_mes_valor_maior_que_media}')
