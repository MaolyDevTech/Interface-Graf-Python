# Projeto de Interface Gráfica com Python

Este projeto tem como objetivo criar uma interface gráfica em Python usando a biblioteca PySimpleGUI. O foco principal é criar uma interface de login simples onde os usuários podem inserir um nome de usuário e senha. Se as credenciais de login forem corretas, uma mensagem de boas-vindas será exibida.

# As Is:


![image](https://github.com/MaolyDevTech/Interface-Graf-Python/assets/144358009/c23e7366-3e72-4f58-9b60-caf1b6af892e)      

# To Be:

![image](https://github.com/MaolyDevTech/Interface-Graf-Python/assets/144358009/8ebaa548-6b00-4d44-a518-ff56725bbefe)


## Configurando o Ambiente de Desenvolvimento

Para começar a trabalhar neste projeto, siga as etapas a seguir:

1. **Criação de Ambiente Virtual**: É recomendável isolar as dependências do projeto em um ambiente virtual. Para criar o ambiente virtual, execute o seguinte comando:

   ```
   python -m venv interface
   ```

2. **Ativação do Ambiente Virtual (Windows)**: Ative o ambiente virtual com o seguinte comando:

   ```
   .\interface\Scripts\activate
   ```

   Consulte a documentação apropriada para outras plataformas.

3. **Instalação da Biblioteca PySimpleGUI**: Instale a biblioteca PySimpleGUI no ambiente virtual com o comando a seguir:

   ```
   pip install PySimpleGUI
   ```

## Estrutura do Projeto


1. **Importando a Biblioteca e Definindo o Tema**:

   - Primeiro, o código importa a biblioteca PySimpleGUI com um alias "sg" para tornar mais fácil usá-la.
   - Em seguida, define o tema da interface como "DarkPurple6". O tema é responsável pelo estilo visual da janela.

2. **Definindo o Layout da Interface**:

   - O layout é a estrutura da interface que os usuários veem. Aqui está o que está acontecendo:
   - Um campo de entrada de "Usuário" é criado com um espaço para inserir texto. O campo é identificado por 'usuario'.
   - Um campo de entrada de "Senha" é criado com um espaço para inserir texto, mas os caracteres inseridos são mascarados por asteriscos (senha). O campo é identificado por 'senha'.
   - Uma caixa de seleção chamada 'Salvar o Login?' é incluída, que permite que você marque ou desmarque.
   - Um botão "Entrar" é criado que os usuários podem clicar.

3. **Criando a Janela**:

   - A janela é onde todos os elementos da interface são exibidos. A função `sg.Window()` é usada para criar uma janela chamada 'Login com Python' com base no layout que definimos anteriormente.

4. **Lendo os Eventos**:

   - Agora, o código entra em um loop que continuamente lê os eventos da janela e os valores dos elementos da interface.
   - Ele verifica se o evento de fechamento da janela ocorreu (`sg.WINDOW_CLOSED`) e, se isso acontecer, o loop é encerrado, o que fecha a janela.
   - Em seguida, ele verifica se o botão "Entrar" foi pressionado e se as credenciais de usuário ('maoly') e senha ('123456') estão corretas.
   - Se as credenciais estiverem corretas, ele exibe uma mensagem de boas-vindas na tela com a frase 'Bem-vindo à Interface Gráfica com Python da Maoly!'.

Esse é um programa de interface gráfica simples que permite aos usuários inserir um nome de usuário e uma senha. Se as credenciais estiverem corretas, ele exibe uma mensagem de boas-vindas. É uma aplicação básica de interface gráfica, comum em aplicativos de login.


## Executando o Projeto

Para executar o projeto, certifique-se de que o ambiente virtual está ativado e que você está no diretório onde o código está localizado. Em seguida, execute o código Python fornecido.

O "unpacking" em Python é uma técnica que permite atribuir valores de uma estrutura de dados, como uma tupla ou lista, a várias variáveis em uma única linha. No contexto deste projeto, a linha `eventos, valores = janela.read()` faz uso do "unpacking" para atribuir os valores da tupla retornada por `janela.read()` às variáveis `eventos` e `valores`.

Agora você tem um projeto simples de interface gráfica com Python usando a biblioteca PySimpleGUI. Este projeto pode servir como base para o desenvolvimento de interfaces mais complexas e personalizadas de acordo com suas necessidades.
