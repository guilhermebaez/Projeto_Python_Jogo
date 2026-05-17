
<img width="263" height="160" alt="image" src="https://github.com/user-attachments/assets/4c00308c-bb7a-4c79-a455-419c4a1c706f" />															

**Jogo de Descobrir Palavra**

**Nome:** Guilherme Baez Machado

**RA:** 26002725

**1 - Projeto**

-Consiste em um jogo de adivinhação de palavras

-O Sistema sorteia uma palavra em uma lista é definida

-O jogador tenta adivinhar a palavra escolhida pelo sistema

-O input do jogador será apenas letras

**2 - Funcionamento**

-Tela própria do aplicativo (sem usar terminal) usando Tkinter

--------------------------------

Funções Usadas:

Função - Objetivo

Tk() - janela principal

Label()	- textos

Button() - botões

Entry()	- input

Toplevel() - popup

pack() - posicionamento

config() - atualizar interface

after() - delay

withdraw() - esconder janela

deiconify() - mostrar janela

mainloop() - manter app aberto

get() - ler input

delete() - limpar input

quit() - fechar app

--------------------------------

-A tela deve ser estilizada e agradável visualmente

-TEMA: Países e Cidades

-Elementos da tela:

	|-Título do projeto (Estilizado em asterisco ASCII)
	
	|-Tema do jogo (Estilizado em asterisco ASCII)
	
	|-Palavra: _ _ _ _ _ (Mostrador de Letras estilo forca)
	
	|-Dica: (Baseada na palavra escolhida pelo sistema)
	
	|-Letras Usadas: (Letras escolhidas pelo player)
	
	|-Tentativas (O player receberá um número de tentativas variável, dependendo da palavra que o sistema selecionar --> Sistema de dificuldade)
	
	|-Acertos: (Quantas palavras o jogador acertou)
	
	|-Input: (Aqui é onde o player escreve a letra)

<img width="803" height="628" alt="image" src="https://github.com/user-attachments/assets/4f99bc3d-be55-44ab-a7a6-128f84529a74" />
	
-Após o envio da letra, o sistema deve validar o carácter e atualizar o estado do jogo: Verifica se a letra pertence a palavra, atualiza a exibição da palavra, registra a letra como utilizada (não poderá mais ser usada), incrementa o número de tentativas.

-O processo irá se repetir até o jogador acertar a palavra;

-Após acertar:

|-Mensagem de acerto;

|-Nova Rodada

-Caso o player não acerte a palavra, um HUD de derrota irá aparecer, avisando o jogador que ele perdeu e perguntar se quer jogar novamente ou não.

<img width="499" height="426" alt="image" src="https://github.com/user-attachments/assets/2bf58c14-d6db-48eb-a510-6852b2f72e3e" />

-O jogo terá um sistema de pontos baseado na quantidade de palavras que o player acertou, guardando o high-score de cada um que jogar o jogo, salvando no arquivo TXT de nomes dos jogadores;

**3 - Arquivos**

**-Arquivo 1:**

	Contém todas as palavras e suas respectivas dicas.

**-Arquivo 2:**

	Atualizado ao final de cada partida, contendo:
	- Nome do jogador
	- Data da partida
	- Pontuação final
	- Número de tentativas
	- Palavra secreta
	
**4 - Controle do projeto**

-O projeto será feito em Python, utilizando o VSCode;

-O controle do projeto será feito via GitHub, contendo as versões comitadas e o release final;

-O código será comentado, explicando seu funcionamento;

**5 - Estrutura de dados**

-Dicionário (dict): Irá armazenar as palavras e suas respectivas dicas

-Lista (list): Será utilizada para armazenar as letras já inseridas pelo jogador

-String (str): Representará a palavra sorteada para exibir a palavra aos poucos (conforme as letras sejam acertadas)

**6 - Tratamento de Erro**

-O sistema deverá validar todas as entradas do usuário antes de processá-las.

-Caso o jogador não insira nenhum valor, a entrada será ignorada.

-O sistema aceitará apenas uma letra por vez. Caso contrário, a entrada será rejeitada.

-Entradas que não sejam letras (como números ou símbolos) não serão aceitas.

-Caso o jogador insira uma letra já utilizada anteriormente, o sistema deverá ignorar a entrada e não contabilizar como tentativa.

-O sistema deverá evitar falhas durante a execução, garantindo que entradas inesperadas não interrompam o funcionamento do jogo.

**7 - Visão Empreendedora**

-Público-Alvo:

-O jogo é voltado para estudantes e jogadores casuais que desejam aprender e se divertir.

-Problemas que o jogo resolve:

-Auxilia no aprendizado de geografia (países e cidades).

-Estimula o raciocínio lógico e a memória.

-Pode ser utilizado como ferramenta educacional em pré-escolas.

-Aplicações:

-Uso educacional

-Uso recreativo

-Treinamento cognitivo

-Inovação:

-O uso de interface gráfica com ASCII torna o jogo visualmente diferenciado.

-O sistema pode ser expandido com novos temas e modos de jogo.
