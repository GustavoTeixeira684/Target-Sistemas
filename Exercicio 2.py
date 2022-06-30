#Questão 2)

try:
  value = int(input("Digite o valor inteiro desejado: "))
  
  #Declaração de variáveis
  fib1, fib2, term = 0, 1, 0
  verifier = False

  #Bloco do código onde verifica se o valor inserido faz parte da sequência de Fibonacci
  if value == 0 or value == 1:
    verifier = True
  else:
    while term <= value:
      term = fib1 + fib2
      if term == value:
        verifier = True
        break
      fib1 = fib2
      fib2 = term
  
    #Bloco do código onde informa o usuário se o valor informado está presente na sequência de Fibonnaci
  if verifier == True:
    print("O número informado pertence a sequência de Fibonacci.")
  else:
    print("O número informado NÃO pertence a sequência de Fibonacci.")

#Tratamento de erro
except:
  print("Por favor, digite um valor numérico inteiro")

