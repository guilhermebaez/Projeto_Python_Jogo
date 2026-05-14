#Gerando a lógica para abrir arquivos
#Importando biblioteca random
import random as rd

#Função para carregar palavras
def carregar_palavras():
    #Dict para guardar as palavras e dicas do TXT em python
    palavras = {}

    #Abrindo o arquivo
    arq = open("palavras.txt", "r", encoding="utf-8")

    #Lendo cada linha do arquivo e separando ente palavra e dica pelo ";"
    for linha in arq:
        linha = linha.strip() #Remove espaços vazios e quebra delinha
        palavra, dica = linha.split(";") #Divide a linha entre a palavra e dica, usando strip localizando o ";"
        palavras[palavra] = dica #colocando os dados dentro do dicionário

    arq.close()
    return palavras

#Função para escolher as palavras
def escolher_palavra():
    palavras = carregar_palavras() #Aqui você chama a função que lê o TXT e cria o dicionário
    #Pegando, aleatóriamente, as palavras chaves (capitais) do dicionários e transformando em uma lista 
    palavra = rd.choice(list(palavras.keys())) #A função palavras.key lê apenas a palavra chave do dicionário
    dica = palavras[palavra] #Pega a dica correspondente a palavra chave

    return palavra, dica

#Validação da letra do usuário
def validar_letra(letra, usadas): #Valida a letra do usuário e compara com a lista de letras usadas
    letra = letra.upper() #transforma em maiúscula

    #Se a letra for vazia, retorna um valor falso
    if letra == "":
        return False
    
    #Verificando se o usuário colocou apenas uma letra
    if len(letra) != 1:
        return False
    
    #Verificando se a letra está no alfabeto
    if not letra.isalpha():
        return False
    
    #Verificando se a letra foi usada
    if letra in usadas:
        return False
    
    return True