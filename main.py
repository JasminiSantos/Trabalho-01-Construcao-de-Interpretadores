# Trabalho 01 de Construção de Interpretadores
# Jasmini Rebecca Gomes dos Santos
# Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  determinar  se  uma  string de entrada  faz  parte  da  linguagem  𝐿    definida  por  𝐿 = {𝑥 | 𝑥 ∈ {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.  

def leitor_strings(lista):
  for i in range(1,len(lista)):
    contadorB = 0
    contadorA = 0
    resultado = True
  
    for j in range(len(lista[i])):
      if (lista[i][j] == "a" or lista[i][j] == "b" or lista[i][j] == "c"):
        if (lista[i][j] == "a" and j == len(lista[i])-1):
          resultado = False
        elif (lista[i][j] == "b" and contadorA == 1 and contadorB == 0 and j == len(lista[i]) - 1):
          contadorB += 1
          resultado = False
          break
        elif (lista[i][j] == "b" and contadorA == 1):
          contadorB += 1   
        elif ((lista[i][j] == "c" or lista[i][j] == "a") and contadorB < 2 and contadorA == 1):
          resultado = False
          break
        elif (lista[i][j] == "c" and contadorB >= 2 and contadorA == 1):
          contadorA = 0
          contadorB = 0
        elif ((lista[i][j] == "a" and contadorB >= 2 and contadorA == 1) or (lista[i][j] == "a" and contadorA == 0)):
          contadorA = 1
          contadorB = 0
      else:
        resultado = False
  
    if(resultado == True):
      print(lista[i] + ": pertence.")
    else:
      print(lista[i] + ": não pertence.")

lista1 = open('texto1.txt').read().split()
lista2 = open('texto2.txt').read().split()
lista3 = open('texto3.txt').read().split()

leitor_strings(lista1)
leitor_strings(lista2)
leitor_strings(lista3)