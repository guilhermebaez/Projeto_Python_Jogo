#Gerando a lógica para abrir arquivos
#Importando biblioteca random
import random as rd
from datetime import datetime

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

#Função para salvar a pontuação do player
def salvar_pontos(nome, pontos):
    arq = open("pontuacoes.txt", "a", encoding="utf-8")
    arq.write(f"{nome};{pontos}\n")
    arq.close()

#Função para carregar o ranking dos jogadores
def carregar_rank():
    ranking = []
    arq = open("pontuacoes.txt", "r", encoding="utf-8")

    #Percorrendo o TXT e adicionando ele na lista
    for linha in arq:
        dados = linha.strip().split(";")

        # Verifica se a linha possui nome e pontos
        if len(dados) == 2:
            nome = dados[0]
            pontos = dados[1]
            ranking.append((nome, int(pontos)))
    arq.close()

    #Ordenando a maior pontuação para menor pontuação
    for i in range(len(ranking)): #Lê o rank X
        for j in range(i + 1, len(ranking)): #Lê o rank Y
            #comparando os pontos
            if(ranking[j][1] > ranking[i][1]): #Caso o ranking X seja maior que o ranking Y
                #Fazendo os nomes trocarem de posição
                troca = ranking[i] #Variável de troca para ordenar os rankings
                #Invertendo os rankings para ordenar do maior pro menor
                ranking[i] = ranking[j]
                ranking[j] = troca
    return ranking

#Função para salvar o histórico completo do jogo:
#O resultado de todas as partidas devem ser armazenadas em um arquivo, contendo, pelo menos, as seguintes informações: DATA, Nome do jogador, Pontuação, Número de tentativas, Palavra (ou frase) secreta
def salvar_historico(acerto, nome, pontos, tentativas, palavra):
    #Pegando a data atual do computador
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    #Abre o arquivo no modo append
    arq = open("historico_partidas.txt", "a", encoding="utf-8")

    #Escreve as informações da partida
    arq.write(
        f"{acerto} -  "
        f"Data: {data} | "
        f"Jogador: {nome} | "
        f"Pontos: {pontos} | "
        f"Tentativas Usadas: {tentativas} | "
        f"Palavra: {palavra}\n"
    )

    #Fecha o arquivo
    arq.close()