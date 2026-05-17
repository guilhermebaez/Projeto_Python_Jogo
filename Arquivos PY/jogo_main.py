#Usando Tkinter para abrir a interface gráfica do jogo
#Importando a biblioteca
import tkinter as tk
import jogo_logica as JL

nome_jogador = input("Digite seu nome para iniciar o jogo: ")

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
def nova_rodada():
    #transformando variáveis em globais
    global palavra_secreta
    global dica_texto
    global palavra_oculta
    global letras_usadas
    global tentativas_restantes
    global quantidade_acertos 

    #escolhendo uma palavra nova
    palavra_secreta, dica_texto = JL.escolher_palavra()

    #Reseta a lista de letras usadas
    letras_usadas = []

    #Reseta a lista que guarda a palavra secreta
    palavra_oculta = []

    #Voltando os "_" no lugar das letras
    for letra in palavra_secreta:
        palavra_oculta.append("_")

    # Atualiza tela
    palavra.config(
        text = f"Palavra: {' '.join(palavra_oculta)}"
    )

    dica.config(
        text = f"Dica: {dica_texto}"
    )

    letras.config(
        text = f"Letras Usadas: "
    )

    #Limpa mensagem anterior - Dava erro mostrando sempre "Você acertou"
    status.config(text = "")

#Função para inicar um novo jogo
def novo_jogo():
    global quantidade_acertos

    # Zera os pontos
    quantidade_acertos = 0

    #Reseta as tentativas
    tentativas_restantes = 6
    
    # Atualiza label
    acertos.config(
        text = f"Acertos: {quantidade_acertos}"
    )
    tentativas.config(
        text = f"Tentativas: {tentativas_restantes}"
    )

    # Inicia nova rodada
    nova_rodada()

#Função para verificar a letra colocada pelo usuário
def verificar_letra():
    print("botão funcionou") #Mensagem de debug
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
    #Join - Junta elementos da lista usando espaço
    #Config - altera um widget, ou seja, um elemento do TK que já existe
    palavra.config(text = f"Palavra: {' '.join(palavra_oculta)}") #Mostra a palavra atualizada

    letras.config(text = f"Letras Usadas: {', '.join(letras_usadas)}") #Mostra a letras usadas

    tentativas.config(text = f"Tentativas: {tentativas_restantes}") #Mostra a quantidade de tentativas restante

    # Vitória
    if "_" not in palavra_oculta:

        quantidade_acertos += 1

        acertos.config(text = f"Acertos: {quantidade_acertos}")

        status.config(text = "Você acertou!")

        #Salvando histórico - Rodada ganha
        
        tentativas_usadas = 6 - tentativas_restantes
        if (tentativas_usadas == 0):
            tentativas_usadas = "Acertou Em Cheio"
        else:
            tentativas_usadas = tentativas_usadas

        acerto = "ACERTO"
        JL.salvar_historico(
            acerto,
            nome_jogador,
            quantidade_acertos,
            tentativas_usadas,
            palavra_secreta
        )

        janela.after(2000, nova_rodada)

    # Derrota
    if tentativas_restantes <= 0:
        #Salvando nome e pontos no arquivo TXT
        JL.salvar_pontos(nome_jogador, quantidade_acertos)

        acerto = "DERROTA"
        tentativas_usadas = "JOGADOR PERDEU"
        JL.salvar_historico(
            acerto,
            nome_jogador,
            quantidade_acertos,
            tentativas_usadas,
            palavra_secreta
        )

        #Escondendo a janela principal do jogo
        janela.withdraw()

        # Janela de derrota
        tela_derrota = tk.Toplevel() #TK.toplevel é uma função que abre um pequeno pop-up
        ranking = JL.carregar_rank()
        #Configurando o pop-up de derrota
        tela_derrota.title("Derrota")
        tela_derrota.geometry("500x400")
        tela_derrota.configure(bg = "darkred")

        # Mensagem da tela de derrota
        msg = tk.Label(
            tela_derrota,
            text = "Você perdeu!",
            font = ("Courier", 16),
            bg = "darkred",
            fg = "white"
        )

        msg.pack(pady = 20)
        #Mostrando o ranking 
        titulo_rank = tk.Label(
            tela_derrota,
            text = "MELHORES TENTATIVAS",
            font = ("Courier", 14),
            bg = "darkred",
            fg = "gold"
        )
        titulo_rank.pack(pady = 10)

        #Loop para o rank aparecer
        for i in range(min(5, len(ranking))):
            nome = ranking[i][0]
            pontos = ranking[i][1]

            texto = (f"{i + 1}° Lugar: {nome} - {pontos} pontos")
            jogador_label = tk.Label(
                tela_derrota,
                text = texto,
                font = ("Courier", 12),
                bg = "darkred",
                fg = "white"
            )
            jogador_label.pack()
        
        #Função para mostrar a tela escondida novamente usando o comando deiconify() - mostra a janela escondida por withdraw
        def reiniciar():

            tela_derrota.destroy()

            janela.deiconify()

            novo_jogo()

        # Botão jogar novamente
        btn_reiniciar = tk.Button(
            tela_derrota,
            text = "Tentar Novamente",
            #Quando o botão jogar novamente for apertado:
            #A tela de derrota irá fechar e a função nova rodada irá ser chamada, abrindo uma nova tela de jogo
            command = reiniciar
        )

        btn_reiniciar.pack(pady = 10)

        # Botão sair
        btn_sair = tk.Button(
            tela_derrota,
            text = "Sair",
            #Ao botão ser apertado, a 
            command = janela.quit
        )

        btn_sair.pack(pady = 10)

# Label de status do jogo
# Status é uma label vazia que será configurada de acordo com a situação do jogo
status = tk.Label(
    janela,
    text = "",
    font = ("Courier", 12),
    bg = "royalblue3",
    fg = "yellow"
)

status.pack(pady = 10)

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