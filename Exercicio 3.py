import json

#Lendo arquivo Json
with open("Json/dados.json", encoding='utf-8') as dados_json:
    
  dados = json.load(dados_json)

#Methods:

#Calcular Menor Faturamento:
def menor_faturamento():
  
  valor = dados[0]['valor']
  
  for i in dados:
    if i['valor'] > 0:
      if i['valor'] < valor:
        valor = i['valor']
        dia = i['dia']
        
  return valor, dia

#Calcular Maior Faturamento:
def maior_faturamento():
  
  valor = dados[0]['valor']

  for i in dados:
    if i['valor'] > valor:
      valor = i['valor']
      dia = i['dia']
        
  return valor, dia


#Calcular dias com faturamento maior que a média:
def faturamento_acima_media():
  contador, soma, media = 0, 0, 0
  
  #Calcula a média:
  for i in dados:
    if i['valor'] > 0.0:
      soma += i['valor']
      contador += 1
    
  media = soma/contador
  contador = 0

  #Calcula quantos valores de faturamento são superiores à média:
  for i in dados:
    if i['valor'] > media:
      contador += 1

  return contador

    


#Declarando variáveis:
faturamento, dia = 0,0




#Exibe o menor dia de faturamento e valor (Somente valores maiores que 0.0):
  
faturamento,dia = menor_faturamento()

print("\nO menor valor de faturamento ocorrido em um dia do mês é: R$%.2f"% faturamento, " no dia: ", dia)

#Exibe o maior dia de faturamento e o valor:

faturamento,dia = maior_faturamento()

print("\nO maior valor de faturamento ocorrido em um dia do mês é: R$%.2f"% faturamento, " no dia: ", dia)

#Exibe quantos dias tiveram faturamento acima da média

print("\n", str(faturamento_acima_media()), " dias tiveram um faturamento acima da média do mês.")
