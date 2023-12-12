def calcular_media_aritmetica(lista):

    soma = 0

    for x in lista:
        soma += x
    media = soma/len(lista)

    return media
   

def calcular_media_geometrica(lista):

    multiplicacao = 1

    for x in lista:
        multiplicacao *= x
    media = multiplicacao**(1/len(lista))

    return media
   

def calcular_media_harmonica(lista):

    soma_reciprocos = 0

    for x in lista:
        soma_reciprocos += 1 / x
    media_harmonica = len(lista) / soma_reciprocos

    return media_harmonica

   

def calcular_media_ponderada(lista, pesos):

    soma_multiplicadores = 0
    soma_pesos = 0

    for num in range(len(lista)):
        x = lista[num] * pesos[num]
        soma_pesos += pesos[num]
        soma_multiplicadores += x
    media_ponderada = soma_multiplicadores / soma_pesos

    return media_ponderada

 

def calcular_mediana(lista):

    lista.sort()

    if len(lista) % 2 == 1:
        indice_mediana = len(lista) // 2
        mediana = lista[indice_mediana]

    else:
        segundo_indice = len(lista) // 2
        primeiro_indice = segundo_indice - 1
        mediana = (lista[primeiro_indice] + lista[segundo_indice])/2

    return mediana

   

def calcular_moda(lista):

    moda = None
    maior = 0
    contagem = {}

    for num in lista:
        if num not in contagem:
            contagem[num] = 1
        else:
            contagem[num] += 1

    for valor, qtde in contagem.items():
        if qtde > maior:
            maior = qtde
            moda = valor

    return moda


def calcular_variancia_amostral(lista):

    soma = 0
    for x in lista:
        soma += x
    media = soma/len(lista)

    soma_quadrados_diferencas = 0
    for x in lista:
        soma_quadrados_diferencas += (x - media) ** 2

    variancia_amostral = soma_quadrados_diferencas / (len(lista) - 1)

    return variancia_amostral


def calcular_variancia_populacional(lista):

    soma = 0
    for x in lista:
        soma += x
    media = soma/len(lista)

    soma_quadrados_diferencas = 0
    for x in lista:
        soma_quadrados_diferencas += (x - media) ** 2

    variancia_populacional = soma_quadrados_diferencas / len(lista)

    return variancia_populacional

def calcular_desvio_padrao_amostral(lista):
    soma = 0
    for x in lista:
        soma += x
    media = soma/len(lista)
    
    soma_quadrados_diferencas = 0
    for x in lista:
        soma_quadrados_diferencas += (x - media) ** 2

    variancia_amostral = soma_quadrados_diferencas / (len(lista) - 1)
    desvio_padrao_amostral = variancia_amostral ** 1/2

    return desvio_padrao_amostral

def calcular_desvio_padrao_populacional(lista):

    soma = 0
    for x in lista:
        soma += x
    media = soma / len(lista)

    soma_quadrados_diferencas = 0
    for x in lista:
        soma_quadrados_diferencas += (x - media) ** 2

    desvio_padrao_amostral = (soma_quadrados_diferencas / (len(lista) - 1)) ** 1/2

    return desvio_padrao_amostral

# 1) Faça funções em Python em células do Jupyter Notebook para
# calcular a média:
# a. Aritmética
# b. Geométrica
# c. Harmônica
# d. Verifique que: 𝑥ҧ𝑎𝑟𝑖𝑡𝑚é𝑡𝑖𝑐𝑎 > 𝑥𝑔𝑒𝑜𝑚é𝑡𝑟𝑖𝑐𝑎 ҧ > 𝑥ҧℎ𝑎𝑟𝑚ô𝑛𝑖𝑐𝑎
# Use como entrada x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]

x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
media_aritmetica = calcular_media_aritmetica(x)
print(f'Media aritmética: {media_aritmetica}')
media_geometrica = calcular_media_geometrica(x)
print(f'Media geométrica: {media_geometrica}')
media_harmonica = calcular_media_harmonica(x)
print(f'Media harmônica: {media_harmonica}')

# 2) Faça uma função em Python em uma célula do Jupyter Notebook
# para calcular a média ponderada. Ela deve receber dois vetores
# (listas) como entrada. Use o mesmo x do exercício anterior com os
# pesos w = [113, 88, 58, 65, 71, 46, 36, 33, 37, 40, 24, 21, 20, 15, 20]

x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
w = [113, 88, 58, 65, 71, 46, 36, 33, 37, 40, 24, 21, 20, 15, 20]

media_ponderada = calcular_media_ponderada(x, w)
print(f'Média ponderada: {media_ponderada}')

# 3) Faça funções em Python em células do Jupyter Notebook para
# calcular a moda e a mediana:
# Para testar, use como entrada x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]

x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
mediana = calcular_mediana(x)
moda = calcular_moda(x)
print(f'Mediana: {mediana}')
print(f'Moda: {moda}')

# 4) Faça funções em Python em
# células do Jupyter Notebook
# para calcular a:
# a. Variância amostral
# b. Variância populacional
# c. Desvio padrão amostral
# d. Desvio padrão populacional
# e. Incerteza da média
# Não usar pacotes prontos!
# Cada função deve receber apenas o vetor/lista de dados numéricos.
# Use como entrada x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]

variancia_amostral = calcular_variancia_amostral(x)
print(f'Variância amostral: {variancia_amostral}')
variancia_populacional = calcular_variancia_populacional(x)
print(f'Variância populacional: {variancia_populacional}')
desvio_padrao_amostral = calcular_desvio_padrao_amostral(x)
print(f'Desvio padrão amostral: {desvio_padrao_amostral}')
desvio_padrao_populacional = calcular_desvio_padrao_populacional(x)
print(f'Desvio padrão populacional: {desvio_padrao_populacional}')
