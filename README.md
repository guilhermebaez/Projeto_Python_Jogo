Jogo de Descobrir Palavras
Nome: Guilherme Baez Machado
RA: 26002725

1 - Projeto
-Consiste em um jogo de adivinhação de palavras
-O Sistema sorteia uma palavra em uma lista é definida
-O jogador tenta adivinhar a palavra escolhida pelo sistema
-O input do jogador será apenas letras

2 - Funcionamento
-Tela própria do aplicativo (sem usar terminal) usando Tkinter
-A tela deve ser estilizada e agradável visualmente
-TEMA: Países e Cidades
-Elementos da tela:
	|-Título do projeto (Estilizado em asterisco ASCII)
	|-Tema do jogo (Estilizado em asterisco ASCII)
	|-Palavra: _ _ _ _ _ (Mostrador de Letras estilo forca)
	|-Dica: (Baseada na palavra escolhida pelo sistema)
	|-Letras Usadas: (Letras escolhidas pelo player)
	|-Tentativas (Quantas vezes o jogador deu input)
	|-Acertos: (Quantas palavras o jogador acertou)
	|-Input: (Aqui é onde o player escreve a letra)
-Após o envio da letra, o sistema deve validar o carácter e atualizar o estado do jogo: Verifica se a letra pertence a palavra, atualiza a exibição da palavra, registra a letra como utilizada (não poderá mais ser usada), incrementa o número de tentativas.
-O processo irá se repetir até o jogador acertar a palavra;
-Após acertar, um outro HUD irá aparecer contendo: 
|-Mensagem de acerto;
|-Quer continuar?; 
(Sim: Reinicia com uma nova palavra)
(Não: Fecha o sistema e gera um arquivo TXT)

3 - Arquivos
-Arquivo 1 - Contém todas as palavras e suas dicas
-Arquivo 2 - Atualizado após o fim do jogo, contém o nome do jogador, a data que jogou, sua pontuação e quantidade de tentativas
	
4 - Controle do projeto
-O projeto será feito em Python, utilizando o VSCode;
-O controle do projeto será feito via GitHub, contendo as versões comitadas e o release final;
-O código será comentado, explicando seu funcionamento;

5 - Estrutura de dados
-Dicionário (dict): Irá armazenar as palavras e suas respectivas dicas
-Lista (list): Será utilizada para armazenar as letras já inseridas pelo jogador
-String (str): Representará a palavra sorteada para exibir a palavra aos poucos (conforme as letras sejam acertadas)

6 - Tratamento de Erro
-O sistema deverá validar todas as entradas do usuário antes de processá-las.
-Caso o jogador não insira nenhum valor, a entrada será ignorada.
-O sistema aceitará apenas uma letra por vez. Caso contrário, a entrada será rejeitada.
-Entradas que não sejam letras (como números ou símbolos) não serão aceitas.
-Caso o jogador insira uma letra já utilizada anteriormente, o sistema deverá ignorar a entrada e não contabilizar como tentativa.
-O sistema deverá evitar falhas durante a execução, garantindo que entradas inesperadas não interrompam o funcionamento do jogo.

