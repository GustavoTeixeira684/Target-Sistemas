
#Declarando Variáveis:

#Declarando array que armazena o faturamento dos diferentes estados:
faturamento_estados = [ ['SP', 67836.43],
                        ['RJ', 36678.66],
                        ['MG', 29229.88],
                        ['ES', 27165.48],
                        ['Outros', 19849.53] ]



faturamento_total = 0

  
#Calculando o faturamento total:
for i in faturamento_estados:
  faturamento_total += i[1]


# Método para calcular o percentual de cada estado:
def calculo_percentual(indice):

  percentual = faturamento_estados[indice][1] / faturamento_total * 100
  return percentual



print("Segue percentual do faturamento dos diferentes estados: \n")
for i in range(len(faturamento_estados)):
  print("->", faturamento_estados[i][0], "Representa %.2f"% calculo_percentual(i), "% do faturamento total\n")


  

