

string_orig = input("Digite um string qualquer:")
string_invertida = ""

#Usando um For decrescente para percorrer a string de trás para frente:
for i in range(len(string_orig) - 1,-1,-1):
  string_invertida += string_orig[i]

#Exibindo string invertida
print(string_invertida)