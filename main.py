from pprint import pprint
import banco
import pandas as pd

class Node:
    def __init__(self, livro, autor, serie, biblioteca, quantidade, reading, nome, pilha, fila):
        self.livro = livro
        self.autor = autor
        self.serie = serie
        self.biblioteca = biblioteca
        self.quantidade = quantidade
        self.reading = reading
        self.nome = str(nome)
        self.pilha = pilha
        self.fila = fila
        self.next = None

class LinkedList_livros:
    def __init__(self):
        self.tamanho = 0
        self.head = None

    def append(self, livro, autor, serie, biblioteca, quantidade, reading, nome):
        new_node = Node(livro, autor, serie, biblioteca, quantidade, reading, nome, stack(), queue())

        if not self.head:
            self.head = new_node
            return
    
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        self.tamanho = self.tamanho + 1

    # Procurar um livro na lista por título
    def search(self, title, autor, serie):
        current_node = self.head
        while current_node:
            if current_node.livro == title and current_node.autor == autor and current_node.serie == serie:
                return current_node
            current_node = current_node.next
        return None

    # Procurar por índice
    def find(self, index):
        pointer = self.head
        i = 0
        while(pointer):
            if i == index:
                return pointer.data
            pointer = pointer.next
            i += 1
        print("O índice está fora do alcance da lista.")

    # Remover um livro da lista por título
    def remove(self, title):
        if self.head is None:
            print("A lista está vazia.")
            return
        if self.head.livro == title:
            self.head = self.head.next
            self.tamanho -= 1
            return
        pointer = self.head
        while pointer.next:
            if pointer.next.livro == title:
                pointer.next = pointer.next.next
                self.tamanho -= 1
                return
            pointer = pointer.next

    def print_list(self):
        pointer = self.head
        while pointer:
            print("Livro:", pointer.livro)
            print("Autor:", pointer.autor)
            print("Série:", pointer.serie)
            print("Biblioteca:", pointer.biblioteca)
            print("Quantidade:", pointer.quantidade)
            print("Reading:", pointer.reading)
            print("--------------------\n")
            pointer = pointer.next

    def merge_sort(self, critério_primario, critério_secundario):
        if self.head is None or self.head.next is None:
            return

        meio = self._encontrar_meio()
        esquerda = LinkedList_livros()
        direita = LinkedList_livros()
        esquerda.head = self.head
        direita.head = meio.next
        meio.next = None

        esquerda.merge_sort(critério_primario, critério_secundario)
        direita.merge_sort(critério_primario, critério_secundario)

        self.head = self._merge(esquerda.head, direita.head, critério_primario, critério_secundario)

    def _encontrar_meio(self):
        if self.head is None:
            return None

        lento = self.head
        rapido = self.head

        while rapido.next and rapido.next.next:
            lento = lento.next
            rapido = rapido.next.next

        return lento

    def _merge(self, esquerda, direita, critério_primario, critério_secundario):
        resultado = None

        if esquerda is None:
            return direita
        if direita is None:
            return esquerda

        if critério_primario == "Nome":
            if esquerda.livro < direita.livro:
                resultado = esquerda
                resultado.next = self._merge(esquerda.next, direita, critério_primario, critério_secundario)
            elif esquerda.livro > direita.livro:
                resultado = direita
                resultado.next = self._merge(esquerda, direita.next, critério_primario, critério_secundario)
            else:
                if critério_secundario == "Nome":
                    if esquerda.livro < direita.livro:
                        resultado = esquerda
                        resultado.next = self._merge(esquerda.next, direita, critério_primario, critério_secundario)
                    else:
                        resultado = direita
                        resultado.next = self._merge(esquerda, direita.next, critério_primario, critério_secundario)
                elif critério_secundario == "Ano":
                    if esquerda.ano < direita.ano:
                        resultado = esquerda
                        resultado.next = self._merge(esquerda.next, direita, critério_primario, critério_secundario)
                    elif esquerda.ano > direita.ano:
                        resultado = direita
                        resultado.next = self._merge(esquerda, direita.next, critério_primario, critério_secundario)
                elif critério_secundario == "Autor":
                    if esquerda.autor < direita.autor:
                        resultado = esquerda
                        resultado.next = self._merge(esquerda.next, direita, critério_primario, critério_secundario)
                    elif esquerda.autor > direita.autor:
                        resultado = direita
                        resultado.next = self._merge(esquerda, direita.next, critério_primario, critério_secundario)
                elif critério_secundario == "Serie":
                    if int(esquerda.serie) < int(direita.serie):
                        resultado = esquerda
                        resultado.next = self._merge(esquerda.next, direita, critério_primario, critério_secundario)
                    else:
                        resultado = direita
                        resultado.next = self._merge(esquerda, direita.next, critério_primario, critério_secundario)
        elif critério_primario == "Autor":
            if esquerda.autor < direita.autor:
                resultado = esquerda
                resultado.next = self._merge(esquerda.next, direita, critério_primario, critério_secundario)
            elif esquerda.autor > direita.autor:
                resultado = direita
                resultado.next = self._merge(esquerda, direita.next, critério_primario, critério_secundario)
            else:
                if critério_secundario == "Nome":
                    if esquerda.livro < direita.livro:
                        resultado = esquerda
                        resultado.next = self._merge(esquerda.next, direita, critério_primario, critério_secundario)
                    else:
                        resultado = direita
                        resultado.next = self._merge(esquerda, direita.next, critério_primario, critério_secundario)
                elif critério_secundario == "Ano":
                    if esquerda.ano < direita.ano:
                        resultado = esquerda
                        resultado.next = self._merge(esquerda.next, direita, critério_primario, critério_secundario)
                    elif esquerda.ano > direita.ano:
                        resultado = direita
                        resultado.next = self._merge(esquerda, direita.next, critério_primario, critério_secundario)
                elif critério_secundario == "Autor":
                    if esquerda.autor < direita.autor:
                        resultado = esquerda
                        resultado.next = self._merge(esquerda.next, direita, critério_primario, critério_secundario)
                    elif esquerda.autor > direita.autor:
                        resultado = direita
                        resultado.next = self._merge(esquerda, direita.next, critério_primario, critério_secundario)
                elif critério_secundario == "Serie":
                    if int(esquerda.serie) < int(direita.serie):
                        resultado = esquerda
                        resultado.next = self._merge(esquerda.next, direita, critério_primario, critério_secundario)
                    else:
                        resultado = direita
                        resultado.next = self._merge(esquerda, direita.next, critério_primario, critério_secundario)

        return resultado
    
    def search_all_by_author(self, author):
        results = LinkedList_livros()
        current = self.head

        while current:
            if current.autor == author:
                results.append(current.livro, current.autor, current.serie, current.biblioteca, current.quantidade, current.reading, current.nome)
            current = current.next

        return results

    def search_all_by_title(self, title):
        results = LinkedList_livros()
        current = self.head

        while current:
            if current.livro == title:
                results.append(current.livro, current.autor, current.serie, current.biblioteca, current.quantidade, current.reading, current.nome)
            current = current.next

        return results

class No_usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.next = None

class LinkedList_usuarios:
    def __init__(self):
        self.head = None

    def append(self, nome, senha):
        new_node = No_usuario(nome, senha)

        if not self.head:
            self.head = new_node
            return
    
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

    # Procurar um usuario na lista
    def search(self, nome, senha):
        current_node = self.head
        while current_node:
            if current_node.nome == nome and current_node.senha == senha:
                return True
            current_node = current_node.next
        return None

    # Remover um usuario da lista por título
    def remove(self, nome, senha):
        if self.head is None:
            print("A lista está vazia.")
            return
        if self.head.nome == nome and self.head.senha == senha:
            self.head = self.head.next
            return
        pointer = self.head
        while pointer.next:
            if pointer.next.nome == nome and pointer.next.senha == senha:
                pointer.next = pointer.next.next
                return
            pointer = pointer.next

    def print_list(self):
        pointer = self.head
        while pointer:
            print("Usuário:", pointer.nome)
            print("Senha:", pointer.senha)
            print("--------------------\n")
            pointer = pointer.next

class no:
    def __init__(self, livro, autor, serie):
        self.livro = livro
        self.autor = autor
        self.serie = serie
        self.next = None

class stack:
    def __init__(self):
        self.topo = None
        self.size = 0
        
    def append(self, livro, autor, serie):

        novo_nodo = no(livro, autor, serie)
        novo_nodo.next = self.topo
        self.topo = novo_nodo
        self.size += 1

    def pop(self):

        if self.vazia() == True:
            return print("Está vazia.")
        
        self.topo = self.topo.next
        self.size -= 1


    def vazia(self):

        return self.size == 0

    def imprimir(self):

        atual = self.topo
        while atual:
            print(atual.livro, end=" -> ")
            atual = atual.next
        print("Fim")

# Definição da classe nó para a estrutura de dados fila
class no_queue:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.next = None

# Definição da classe fila
class queue:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def is_empty(self):
        return self.primeiro is None

    def append(self, pessoa):
        no_novo = no_queue(pessoa)
        if self.primeiro == None:
            self.primeiro = no_novo
            self.ultimo = no_novo
        else:
            self.ultimo.next = no_novo
            self.ultimo = no_novo

    def remove(self):
        if self.primeiro is None:
            print("A lista está vazia.")
            return
        self.primeiro = self.primeiro.next
        if self.primeiro is None:
            self.ultimo = None

    def imprimir(self):
        if self.primeiro is None:
            print("Fila vazia")
        else:
            atual = self.primeiro
            while atual:
                print(f"{atual.livro} ({atual.serie}) - {atual.pessoa}", end=" -> ")
                atual = atual.next
            print("Fim")

caminho_usuarios = "C:\\Users\\willi\\OneDrive\\Documentos\\Willian\\Faculdade\\Métodos Computacionais\\Projeto\\usuarios.csv"
caminho_livros = "C:\\Users\\willi\\OneDrive\\Documentos\\Willian\\Faculdade\\Métodos Computacionais\\Projeto\\tb_livros.csv"
visualizar = str()
lista_livros = LinkedList_livros()
lista_usuarios = LinkedList_usuarios()

# Carrega o arquivo CSV em um Dataframe do Pandas
tabela_usuarios_df = pd.read_csv(caminho_usuarios)
tabela_livros_df = pd.read_csv(caminho_livros)


# Loop para ler linha por linha
for indice, linha in tabela_usuarios_df.iterrows():
    # A variável 'linha' contém os valores da linha atual como uma série Pandas
    # Você pode acessar os valores das colunas pelo nome da coluna
    nome = linha['Nome']
    senha = linha['Senha']
    lista_usuarios.append(nome, senha)

for indice, linha in tabela_livros_df.iterrows():
    # A variável 'linha' contém os valores da linha atual como uma série Pandas
    # Você pode acessar os valores das colunas pelo nome da coluna
    livro = linha['livro']
    autor = linha['autor']
    serie = linha['serie']
    biblioteca = linha['biblioteca']
    quantidade = linha['quantidade']
    reading = linha['reading']
    nome = linha['nome']
    nome_fila = linha['fila']
    lista_livros.append(livro,autor,serie,biblioteca,quantidade,reading,nome)

    permission = True

    while 1:
        if permission:
            disponibilidade = quantidade-reading
            permission = False

        if disponibilidade > 0:
            node_livro = lista_livros.search(livro, autor, serie)

            node_livro.pilha.append(livro, autor, serie)
            disponibilidade = disponibilidade - 1
        else:
            break

# Interação com o usuário
while 1:
    visitante = input("Você é visitante: ")

    if visitante == "Sim" or visitante == "sim":
        print("Vamos criar uma conta: ")
        usuario_novo = input("Digite seu nome: ")
        senha_nova = input("Digite uma senha: ")
        
        lista_usuarios.append(usuario_novo, senha_nova)

        # Crie um dicionário com os valores para a nova linha
        nova_linha = {'Nome': usuario_novo, 'Senha': senha_nova}

        # Crie um novo DataFrame com a nova linha e concatene-o com o DataFrame existente
        novo_dataframe = pd.DataFrame([nova_linha])
        tabela_usuarios_df = pd.concat([tabela_usuarios_df, novo_dataframe], ignore_index=True)

        # Salve o DataFrame de volta no arquivo CSV
        tabela_usuarios_df.to_csv(caminho_usuarios, index=False)  # index=False evita a escrita do índice no arquivo

    print("Vamos entrar na sua conta: ")

    usuario = input("Digite seu nome de usuário: ")

    senha = input("Digite sua senha: ")

    if (lista_usuarios.search(usuario, senha)):
        break
    
    print("Usuário e/ou senha inválidos")
first = 1

while(1):

    if first == 0:

        sair = input("Você deseja sair? (Sim/Não) ")

        if sair == "Sim" or sair == "sim":
            break

    ordenacao = input("Você deseja ordenar a lista? (Sim/Não) ")

    if ordenacao == "Sim" or ordenacao == "sim":
        # Escolha o critério prioritário e secundário de ordenação
        critério_primario = input("Escolha o critério prioritário de ordenação (Nome, Autor): ").capitalize()
        critério_secundario = input("Escolha o critério secundário de ordenação (Nome, Autor, Ano, Serie): ").capitalize()

        lista_livros.merge_sort(critério_primario, critério_secundario)

        visualizar = input("Você deseja ver a lista ordenada? (Sim/Não) ")

        if visualizar == "Sim" or visualizar == "sim":
            print("Lista Ordenada:")
            lista_livros.print_list()
        
    if visualizar == "Sim" or visualizar == "sim" or ordenacao == "Não" or ordenacao == "não":
        pass
    else:
        ver = input("Você deseja ver a lista? (Sim/Não) ")

        if ver == "Sim" or ver == "sim":
            print("Lista:")
            lista_livros.print_list()
    
    escolha = int(input("Para devolver um livro digite 1. Para pegar um livro digite 2. Para adicionar um livro digite 3. Para remover um livro digite 4: "))

    if escolha == 1:
        nome_devolvido = input("Digite o nome do livro: ")
        autor_devolvido = input("Digite o nome do autor: ")
        serie_devolvida = int(input("Digite o número da série: "))


        livro = lista_livros.search(nome_devolvido, autor_devolvido, serie_devolvida)
        livro.pilha.imprimir()

        if livro is not None:
            livro.pilha.append(nome_devolvido, autor_devolvido, serie_devolvida,)
        else:    
            print("\nLivro não encontrado no acervo. Digite-o novamente.")
            break
        livro.pilha.imprimir()

    elif escolha == 2:
        livro_procurado = input("Digite o nome do livro que você quer: ")
        autor_procurado = input("Digite o autor desse livro: ")
        serie_procurada = int(input("Digite a série dele: "))

        no_achado = lista_livros.search(livro_procurado,autor_procurado,serie_procurada)

        if no_achado.pilha.size == 0:
            no_achado.fila.append(usuario)
            print("Você está na fila de espera!")
            print(f"O(os) livro(os) está(ão) com {no_achado.nome}.")
            print(f"Tem-se um total de {no_achado.quantidade} livro(os) e {no_achado.reading} sendo lido(os)")
        else:
            print("Você pode pegar o livro!")

            # if no_achado.fila.primeiro.pessoa == usuario:

            no_achado.pilha.pop()
            if nome:
                nome = nome + ", "
            nome = nome + usuario
            # else:
            #     print(f"Você não pode pegar o livro ainda. {no_achado.fila.primeiro.pessoa} tem prioridade.")
    elif escolha == 3:
        livro_novo = input("Digite o nome do livro: ")
        autor_novo = input("Digite o nome do autor: ")
        serie_nova = int(input("Digite o número da série: "))
        biblioteca_nova = int(input("Qual a bilbioteca você deseja colocá-lo? Pais(1), filho(2), filha(3) "))

        existe = lista_livros.search(livro_novo, autor_novo, serie_nova)

        if existe is None:
            lista_livros.append(livro_novo, autor_novo, serie_nova, biblioteca_nova, 1, 0, None)

    lista_livros.print_list()
    first = 0