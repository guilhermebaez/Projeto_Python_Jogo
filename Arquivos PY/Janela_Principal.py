#Usando Tkinter para abrir a interface gráfica do jogo
#Importando a biblioteca
import tkinter as tk

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
palavra = tk.Label(janela, text = "Palavra: ", font = ("Courier", 14), bg = "royalblue3", fg = "white", anchor = "w")
#Utiliza-se Anchor quando quer posicionar um elemento em alguma coordenada dada por west, east, south e north

palavra.pack(anchor = "w", padx = 20, pady=5)
#padx = espaçamento da borda
#pady = espaçamento vertical entre elementos

#Dica
dica = tk.Label(janela, text = "Dica: ", font = ("Courier", 14), bg = "royalblue3", fg = "white", justify = "center")
dica.pack(anchor = "w", padx = 20, pady=5)

#Letras usadas
letras = tk.Label(janela, text = "Letras Usadas: ", font = ("Courier", 14), bg = "royalblue3", fg = "white", justify = "center")
letras.pack(anchor = "w", padx = 20, pady=5)

#Tentativas
tentativas = tk.Label(janela, text = "Tentativas: ", font = ("Courier", 14), bg = "royalblue3", fg = "white", justify = "center")
tentativas.pack(anchor = "w", padx = 20, pady=5)

#Acertos
acertos = tk.Label(janela, text = "Acertos: ", font = ("Courier", 14), bg = "royalblue3", fg = "white", justify = "center")
acertos.pack(anchor = "w", padx = 20, pady=5)

# Título do Entry
label_input = tk.Label(janela, text="Digite uma letra:", font=("Courier", 12), bg="royalblue3", fg="white", anchor="center")
label_input.pack()

#Input do usuário: Quando o input não é no terminal, e sim na interface gráfica, utiliza-se o comando do Tkinter chamado tk.Entry
entrada = tk.Entry(janela, font = ("Arial", 14), width = 3, justify = "center")
entrada.pack(anchor = "center", padx = 20, pady = 5)

janela.mainloop() #Mantém a janela aberta