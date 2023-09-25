from pprint import pprint
import pandas as pd
import os

class Node:
    def __init__(self, livro, autor, serie, biblioteca, quantidade, reading, vezes_lidas, pilha, fila):
        self.livro = livro
        self.autor = autor
        self.serie = serie
        self.biblioteca = biblioteca
        self.quantidade = quantidade
        self.reading = reading
        self.vezes_lidas = vezes_lidas
        self.pilha = pilha
        self.fila = fila
        self.next = None

class LinkedList_livros:
    def __init__(self):
        self.tamanho = 0
        self.head = None

    def append(self, livro, autor, serie, biblioteca, quantidade, reading, vezes):
        new_node = Node(livro, autor, serie, biblioteca, quantidade, reading, vezes, stack(), queue())

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
    def remove(self, title, autor, serie):
        if self.head is None:
            print("A lista está vazia.")
            return
        if self.head.livro == title and self.head.autor == autor and self.head.serie == serie:
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
                results.append(current.livro, current.autor, current.serie, current.biblioteca, current.quantidade, current.reading, current.vezes_lidas)
            current = current.next

        return results

    def search_all_by_title(self, title):
        results = LinkedList_livros()
        current = self.head

        while current:
            if current.livro == title:
                results.append(current.livro, current.autor, current.serie, current.biblioteca, current.quantidade, current.reading, current.vezes_lidas)
            current = current.next

        return results

    def bubble_sort_books(self):
        if self.head is None or self.head.next is None:
            return

        sorted = False
        while not sorted:
            sorted = True
            current = self.head
            while current.next:
                if current.vezes_lidas < current.next.vezes_lidas:
                    current.vezes_lidas, current.next.vezes_lidas = current.next.vezes_lidas, current.vezes_lidas
                    current.livro, current.next.livro = current.next.livro, current.livro
                    current.autor, current.next.autor = current.next.autor, current.autor
                    current.serie, current.next.serie = current.next.serie, current.serie
                    current.biblioteca, current.next.biblioteca = current.next.biblioteca, current.biblioteca
                    current.quantidade, current.next.quantidade = current.next.quantidade, current.quantidade
                    current.reading, current.next.reading = current.next.reading, current.reading
                    sorted = False
                current = current.next

    def ranking_livros(self):
        self.bubble_sort_books()

class No_usuario:
    def __init__(self, nome, senha, livro, serie):
        self.nome = nome
        self.senha = senha
        self.livro = livro
        self.serie = serie
        self.next = None

class LinkedList_usuarios:
    def __init__(self):
        self.head = None

    def append(self, nome, senha, livro, serie):
        new_node = No_usuario(nome, senha, livro, serie)

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
                return current_node
            current_node = current_node.next
        return None
    
    def search_name(self, nome):
        current_node = self.head
        while current_node:
            if current_node.nome == nome:
                return current_node
            current_node = current_node.next
        return None
    
    # Procurar com quem está um livro
    def search_livro(self, livro, serie):
        current_node = self.head
        while current_node:
            if current_node.livro == livro and current_node.serie == serie:
                return current_node
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
        self.strin = None
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

    def string(self):
        self.strin = None
        atual = self.primeiro

        if self.primeiro is None:
            return None
        
        if atual.next is None:
            self.strin = atual.pessoa
            return 1
        
        self.strin = atual.pessoa
 
        flag = False

        while atual:
            if flag:
                self.strin += atual.pessoa
            if atual.next is None:
                pass
            else:
                self.strin += ';'
            atual = atual.next
            # pessoa += ','
            # pessoa +=  atual.pessoa
            flag = True
        return 1

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

# Obtém o diretório atual do script Python
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Define os nomes dos arquivos CSV
nome_arquivo_usuarios = "usuarios.csv"
nome_arquivo_livros = "tb_livros.csv"

# Constrói os caminhos relativos para os arquivos CSV
caminho_usuarios = os.path.join(diretorio_atual, nome_arquivo_usuarios)
caminho_livros = os.path.join(diretorio_atual, nome_arquivo_livros)

#caminho_usuarios = "C:\\Users\\willi\\OneDrive\\Documentos\\Willian\\Faculdade\\Métodos Computacionais\\Projeto\\usuarios.csv"
#caminho_livros = "C:\\Users\\willi\\OneDrive\\Documentos\\Willian\\Faculdade\\Métodos Computacionais\\Projeto\\tb_livros.csv"
visualizar = str()
nomes = str()
escolha = int(0)
lista_livros = LinkedList_livros()
lista_usuarios = LinkedList_usuarios()

# Carrega o arquivo CSV em um Dataframe do Pandas
tabela_usuarios_df = pd.read_csv(caminho_usuarios)
tabela_livros_df = pd.read_csv(caminho_livros)


# Loop para ler linha por linha
for indice, linha in tabela_usuarios_df.iterrows():
    # A variável 'linha' contém os valores da linha atual como uma série Pandas
    # Você pode acessar os valores das colunas pelo nome da coluna
    nome_usuario = linha['Nome']
    senha_usuario = linha['Senha']
    livro_usuario = linha['Livro']
    serie_usuario = linha['Serie']
    lista_usuarios.append(nome_usuario, senha_usuario, livro_usuario, serie_usuario)

for indice, linha in tabela_livros_df.iterrows():
    # A variável 'linha' contém os valores da linha atual como uma série Pandas
    # Você pode acessar os valores das colunas pelo nome da coluna
    livro = linha['livro']
    autor = linha['autor']
    serie = linha['serie']
    biblioteca = linha['biblioteca']
    quantidade = linha['quantidade']
    reading = linha['reading']
    vezes_lidas = linha['vezes_lidas']
    fila = str(linha['fila'])
    lista_livros.append(livro,autor,serie,biblioteca,quantidade,reading,vezes_lidas)

    # Atualiza a fila
    atualizacao = lista_livros.search(livro, autor, serie)

    if fila == "nan":
        pass
    else:
        nomes = fila.split(";")

        # Iterar sobre os nomes usando um loop for
        for nome in nomes:
            atualizacao.fila.append(nome)

    atualizacao.fila.string()


    permission = True

    # Acrescenta os exemplares na pilha
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

    visitante = input("Você é visitante: \n")

    if visitante == "Sim" or visitante == "sim":

        print("Vamos criar uma conta: \n")
        usuario_novo = input("Digite seu nome: \n")
        senha_nova = input("Digite uma senha: \n")
        
        lista_usuarios.append(usuario_novo, senha_nova, None, None)

        # Crie um dicionário com os valores para a nova linha
        nova_linha = {'Nome': usuario_novo, 'Senha': senha_nova}

        # Crie um novo DataFrame com a nova linha e concatene-o com o DataFrame existente
        novo_dataframe = pd.DataFrame([nova_linha])
        tabela_usuarios_df = pd.concat([tabela_usuarios_df, novo_dataframe], ignore_index=True)

        # Salve o DataFrame de volta no arquivo CSV
        tabela_usuarios_df.to_csv(caminho_usuarios, index=False)  # index=False evita a escrita do índice no arquivo

    print("Vamos entrar na sua conta: \n")

    usuario = input("Digite seu nome de usuário: \n")

    senha = input("Digite sua senha: \n")

    if (lista_usuarios.search(usuario, senha)):
        break
    
    print("Usuário e/ou senha inválidas\n")
first = 1

while(1):

    if first == 0:

        sair = input("Certeza que deseja sair? (Sim/Não) \n")

        if sair == "Sim" or sair == "sim":
            break

    ordenacao = input("Você deseja ordenar a lista? (Sim/Não) \n")

    if ordenacao == "Sim" or ordenacao == "sim":
        # Escolha o critério prioritário e secundário de ordenação
        critério_primario = input("Escolha o critério prioritário de ordenação (Nome, Autor): \n").capitalize()
        critério_secundario = input("Escolha o critério secundário de ordenação (Nome, Autor, Serie): \n").capitalize()

        lista_livros.merge_sort(critério_primario, critério_secundario)

        visualizar = input("Você deseja ver a lista ordenada? (Sim/Não) \n")

        if visualizar == "Sim" or visualizar == "sim":

            print("Lista Ordenada:\n")
            lista_livros.print_list()
    
    ranking = input("Você deseja ver o ranking dos mais lidos? (Sim/Não) \n")

    if ranking == "Sim" or ranking == "sim":
        lista_livros.ranking_livros()
        lista_livros.print_list()

    filtro = input("Você deseja usar um filto de busca? (Sim/Não) \n")

    if filtro == "Sim" or filtro == "sim":
        qual_filtro = input("Escolha um filtro: (Nome do livro, Autor) \n")

        if qual_filtro == "Nome do livro":

            nome_livro = input("Digite o nome do livro: \n")
            resultado = lista_livros.search_all_by_title(nome_livro)
            resultado.print_list()

        elif qual_filtro == "Autor":

            nome_autor = input("Digite o nome do autor: \n")
            resultado = lista_livros.search_all_by_author(nome_autor)
            resultado.print_list()
        
    if visualizar == "Não" or visualizar == "não" or ordenacao == "Não" or ordenacao == "não":

        ver = input("Você deseja ver a lista? (Sim/Não) \n")

        if ver == "Sim" or ver == "sim":

            print("Lista:\n")
            lista_livros.print_list()

    escolha = 0
    while (escolha != 5):
        escolha = int(input("\nPara devolver um livro digite 1. Para pegar um livro digite 2. Para adicionar um livro digite 3. Para remover um livro digite 4. Para sair digite 5: \n"))

        # Para devolver um livro
        if escolha == 1:

            nome_devolvido = input("Digite o nome do livro: ")
            autor_devolvido = input("Digite o nome do autor: ")
            serie_devolvida = int(input("Digite o número da série: "))

            livro = lista_livros.search(nome_devolvido, autor_devolvido, serie_devolvida)

            possibilidade = lista_usuarios.search_livro(nome_devolvido, serie_devolvida)

            if livro: # Se existe o Livro
                if possibilidade: # Se a pessoa tem o Livro
                    if possibilidade.nome == usuario: 
                        if livro.fila.primeiro is not None: # Se tem alguém na fila do Livro

                            current = livro.fila.primeiro
                            nome_achado = current.pessoa
                            no_usuario_na_fila = lista_usuarios.search_name(nome_achado)

                            if str(no_usuario_na_fila.livro) == "nan": # Se quem tá na fila não está lendo outro Livro

                                livro.vezes_lidas += 1
                                no_usuario_na_fila.livro = nome_devolvido
                                no_usuario_na_fila.serie = serie_devolvida
                                print(f"\nDê o livro para {nome_achado}.")
                                livro.fila.remove()
                                livro.fila.string()

                                possibilidade.livro = None
                                possibilidade.serie = None

                            else: 
                                livro.pilha.append(nome_devolvido, autor_devolvido, serie_devolvida)
                                livro.vezes_lidas += 1
                                livro.reading -= 1
                                possibilidade.livro = None
                                possibilidade.serie = None
                            
                        else:

                            livro.pilha.append(nome_devolvido, autor_devolvido, serie_devolvida)
                            livro.vezes_lidas += 1
                            livro.reading -= 1
                            possibilidade.livro = None
                            possibilidade.serie = None

                        print("Você pode devolver o livro.")

                    else:
                        print("\nVocê não pode devolver este livro, pois não o está lendo.")
            else:    
                print("\nLivro não encontrado no acervo. Digite-o novamente.")


        # Para pegar um livro
        elif escolha == 2:

            livro_procurado = input("Digite o nome do livro que você quer: ")
            autor_procurado = input("Digite o autor desse livro: ")
            serie_procurada = int(input("Digite a série dele: "))

            # Procura o livro
            no_achado = lista_livros.search(livro_procurado,autor_procurado,serie_procurada)
            
            if no_achado:

                # Entra na fila de espera
                if no_achado.pilha.size == 0:
                
                    no_achado.fila.append(usuario)
                    
                    # Concatena todas as pessoas que estão na fila
                    no_achado.fila.string()

                    # Procura com quem está o livro na fila dos usuários
                    possuidor = lista_usuarios.search_livro(livro_procurado, serie_procurada)

                    print("\nVocê está na fila de espera!")
                    print(f"O(os) livro(os) está(ão) com {possuidor.nome}.")
                    print(f"Tem-se um total de {no_achado.quantidade} livro(os) e {no_achado.reading} sendo lido(os).\n")

                # Pega o livro
                else:
                    print("\nVocê pode pegar o livro!\n")
                    print(f"O livro está na bilbioteca {no_achado.biblioteca}.")

                    # Retira um livro da pilha
                    no_achado.pilha.pop()
                    no_achado.reading += 1

                    no_usuario = lista_usuarios.search(usuario, senha)

                    # Atualiza o livro que a pessoa está lendo na lista dos usuários
                    no_usuario.livro = livro_procurado
                    no_usuario.serie = serie_procurada

            else:
                print("O livro não está no acervo.")

        # Colocar um novo livro na lista encadeada
        elif escolha == 3:

            livro_novo = input("Digite o nome do livro: ")
            autor_novo = input("Digite o nome do autor: ")
            serie_nova = int(input("Digite o número da série: "))
            biblioteca_nova = int(input("Qual a bilbioteca você deseja colocá-lo? Pais(1), filho(2), filha(3) "))

            # Vê se já existe o nó desse livro no acervo
            no_existe = lista_livros.search(livro_novo, autor_novo, serie_nova)

            # Se não existe ele acrescenta uma unidade de livro
            if no_existe is None:

                lista_livros.append(livro_novo, autor_novo, serie_nova, biblioteca_nova, 1, 0, 0)

            # Se existe, ele acrescenta a unidade atual mais 1
            else:
                
                no_existe.quantidade += 1

            print("\nO livro foi adicionado.\n")

        # Remover um livro da lista encadeada
        elif escolha == 4:

            livro_remover = input("Digite o nome do livro: ")
            autor_remover = input("Digite o nome do autor: ")
            serie_remover = int(input("Digite o número da série: "))

            no_remover = lista_livros.search(livro_remover, autor_remover, serie_remover)

            if no_remover:
                # Verifica se todos os exemplares estão sendo lidos
                if no_remover.quantidade - no_remover.reading > 0:
                    # Verifica se possui mais de um exemplar a ser lido
                    if no_remover.quantidade - no_remover.reading > 1:

                        print(f"O livro possui {no_remover.quantidade} exemplares.")
                        quantidade_remover = int(input("Digite quantos exemplares você quer remover: "))

                        # Retirar a quantidade digitada de exemplares da pilha
                        for i in range(quantidade_remover):

                            no_remover.pilha.pop()
                            no_remover.quantidade -= 1

                        print(f"{no_remover.quantidade} foram removidas.")

                        if no_remover.pilha.size == 0:

                            lista_livros.remove(livro_remover, autor_remover, serie_remover)
                            print("\nO Livro foi removido.")

                    # Se só tiver um exemplar a ser lido, ele remove o nó
                    else:
                        lista_livros.remove(livro_remover, autor_remover, serie_remover)
                        print("\nO Livro foi removido.")
                else:
                    print("Você não pode remover este livro, pois todos os exemplares estão sendo lidos.")
            else:

                print("O livro não foi encontrado.")

        first = 0

# No final do código, depois de todas as operações, atualize os DataFrames
data_usuarios = []
data_livros = []

# Atualize a lista data_usuarios com os dados da lista de usuários
current_user = lista_usuarios.head
while current_user:
    data_usuarios.append({'Nome': current_user.nome, 'Senha': current_user.senha, 'Livro': current_user.livro, 'Serie': current_user.serie})
    current_user = current_user.next

# Atualize a lista data_livros com os dados da lista de livros
current_livro = lista_livros.head
while current_livro:
    # Se não tiver alguém na fila
    if current_livro.fila.primeiro is None:
        data_livros.append({'livro': current_livro.livro, 'autor': current_livro.autor, 'serie': current_livro.serie, 'biblioteca': current_livro.biblioteca, 'quantidade': current_livro.quantidade, 'reading': current_livro.reading, 'vezes_lidas': current_livro.vezes_lidas, 'fila': None})
        current_livro = current_livro.next
    # Se tiver alguém na fila
    else:
        data_livros.append({'livro': current_livro.livro, 'autor': current_livro.autor, 'serie': current_livro.serie, 'biblioteca': current_livro.biblioteca, 'quantidade': current_livro.quantidade, 'reading': current_livro.reading, 'vezes_lidas': current_livro.vezes_lidas, 'fila': current_livro.fila.strin})
        current_livro = current_livro.next

# Crie novos DataFrames com os dados atualizados
tabela_usuarios_df = pd.DataFrame(data_usuarios)
tabela_livros_df = pd.DataFrame(data_livros)

# Salve os novos DataFrames nos arquivos CSV, substituindo os antigos
tabela_usuarios_df.to_csv(caminho_usuarios, index=False)
tabela_livros_df.to_csv(caminho_livros, index=False)

# Encerre o programa