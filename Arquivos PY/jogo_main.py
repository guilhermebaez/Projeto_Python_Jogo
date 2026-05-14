#Usando Tkinter para abrir a interface gráfica do jogo
#Importando a biblioteca
import tkinter as tk
import jogo_logica as JL


#Chamando as funções do módulo de lógica
palavra_secreta, dica_texto = JL.escolher_palavra()

#lista de letras já usadas
letras_usadas = []

#palavra escondida
palavra_oculta = []

# Cria os _
for letra in palavra_secreta:
    palavra_oculta.append("_")

# Tentativas
tentativas_restantes = 6

# Acertos
quantidade_acertos = 0

janela = tk.Tk() #Cria a janela principal

#Elementos da janela
janela.title("Jogo Das Palavras") #Título
janela.geometry("800x600") #Resolução
janela.configure(bg="RoyalBlue3") #Cor do fundo

#Para adicionar os elementos na tela utiliza-se LABEL - ELEMENTO QUE MOSTRA NA TELA
#ESTRUTURA:
# Título - GRANDE ASCII
# TEMA - MENOR ASCII

#TÍTULO
#Definindo o texto que irá ser usado
titulo_texto = """
***********************************************************
 ⠈⢹ ⢀⡀ ⢀⡀ ⢀⡀   ⢀⣸ ⢀⣀ ⢀⣀   ⣏⡱ ⢀⣀ ⡇ ⢀⣀ ⡀⢀ ⡀⣀ ⢀⣀ ⢀⣀
 ⠣⠜ ⠣⠜ ⣑⡺ ⠣⠜   ⠣⠼ ⠣⠼ ⠭⠕   ⠇  ⠣⠼ ⠣ ⠣⠼ ⠱⠃ ⠏  ⠣⠼ ⠭⠕
***********************************************************
"""
#Chama-se o LABEL do Tkinter para adcionar um elemento na tela
#Estrutura do label (onde irá colocar o elemento, opções)
#No caso do texto, o elemento será colocado na variável janela e as opções selecionarão qual será o texto, fonte, tamanho, cor e etc
titulo = tk.Label(janela, text=titulo_texto, font=("Courier", 14), bg="royalblue3", fg="white", justify="center")

#Torna visível o elemento criado na LABEL
titulo.pack()

#TEMA
tema_titulo = """
****************************************************
 ⡇  ⢀⡀ ⢀⣀ ⢀⣀ ⠄ ⢀⣀   ⢀⣸ ⢀⡀   ⡷⢾ ⡀⢀ ⣀⡀ ⢀⣸ ⢀⡀
 ⠧⠤ ⠣⠜ ⠣⠤ ⠣⠼ ⠇ ⠭⠕   ⠣⠼ ⠣⠜   ⠇⠸ ⠣⠼ ⠇⠸ ⠣⠼ ⠣⠜
 ****************************************************
"""
tema = tk.Label(janela, text = tema_titulo, font = ("Courier", 14), bg = "royalblue3", fg = "white", justify = "center")
tema.pack(pady = 0)


#Palavra
palavra = tk.Label(janela, text = f"Palavra: {' '.join(palavra_oculta)}", font = ("Courier", 14), bg = "royalblue3", fg = "white", anchor = "w")
#Utiliza-se Anchor quando quer posicionar um elemento em alguma coordenada dada por west, east, south e north

palavra.pack(anchor = "w", padx = 20, pady=5)
#padx = espaçamento da borda
#pady = espaçamento vertical entre elementos

#Dica
dica = tk.Label(janela, text = f"Dica: {dica_texto}", font = ("Courier", 14), bg = "royalblue3", fg = "white", justify = "center")
dica.pack(anchor = "w", padx = 20, pady=5)

#Letras usadas
letras = tk.Label(janela, text = f"Letras Usadas: {', '.join(letras_usadas)}", font = ("Courier", 14), bg = "royalblue3", fg = "white", justify = "center")
letras.pack(anchor = "w", padx = 20, pady=5)

#Tentativas
tentativas = tk.Label(janela, text = f"Tentativas: {tentativas_restantes}", font = ("Courier", 14), bg = "royalblue3", fg = "white", justify = "center")
tentativas.pack(anchor = "w", padx = 20, pady=5)

#Acertos
acertos = tk.Label(janela, text = f"Acertos: {quantidade_acertos}", font = ("Courier", 14), bg = "royalblue3", fg = "white", justify = "center")
acertos.pack(anchor = "w", padx = 20, pady=5)

# Título do Entry
label_input = tk.Label(janela, text="Digite uma letra:", font=("Courier", 12), bg="royalblue3", fg="white", anchor="center")
label_input.pack()

#Input do usuário: Quando o input não é no terminal, e sim na interface gráfica, utiliza-se o comando do Tkinter chamado tk.Entry
entrada = tk.Entry(janela, font = ("Arial", 14), width = 3, justify = "center")
entrada.pack(anchor = "center", padx = 20, pady = 5)

#Função para criar uma nova palavra após vencer a rodada

#Função para verificar a letra colocada pelo usuário
def verificar_letra():
    print("botão funcionou")
    #Transformando as variáveis de tentativas e de acertos em globais
    global tentativas_restantes
    global quantidade_acertos

    #Lendo o input do usuário
    letra = entrada.get().upper()

    #limpa o input automáticamente
    entrada.delete(0, tk.END)

    #valida a letra
    if not JL.validar_letra(letra, letras_usadas):
        return
    
    #adiciona letra usada
    letras_usadas.append(letra)

    #verifica se a letra existe
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_oculta[i] = letra
    else:
        tentativas_restantes -= 1

    #atualizando as labels em tempo real
    palavra.config(text = f"Palavra: {' '.join(palavra_oculta)}")

    letras.config(text = f"Letras Usadas: {', '.join(letras_usadas)}")

    tentativas.config(text = f"Tentativas: {tentativas_restantes}")

    # Vitória
    if "_" not in palavra_oculta:

        quantidade_acertos += 1

        acertos.config(text = f"Acertos: {quantidade_acertos}")

        print("Vitória")

    # Derrota
    if tentativas_restantes <= 0:

        print("Derrota")


#Criando um botão por usuário enviar a letra
botao = tk.Button(
    janela,
    text = "Enviar",
    font = ("Courier", 12),
    bg = "white",
    fg = "black",
    command = verificar_letra
)

botao.pack(pady = 10)

janela.mainloop() #Mantém a janela aberta