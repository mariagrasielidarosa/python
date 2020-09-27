# Tamanho definido da lista (constante).
tamanhoLista = 4
lista = ''


# ______________________________________ Área de definição do classe (registro).
class Pessoa:  # Nome da classe (registro).
    nome = ''  # Atributos nome e matrícula.
    matricula = 0


class Lista:  # Nome da classe (registro).
    alunos = [Pessoa()] * tamanhoLista  # Vetor de alunos de tamanhoLista (constante).
    numeroElementos = 0  # Número de elementos ocupados na lista.


# _____________________________________________________________________________#


# ____________________________________________________________ Módulo criaLista.
# Objetivo: Cria lista com nº de elementos informado pelo usuário.
# Entrada.: Nenhuma.
# Saída...: Lista criada.
# _____________________________________________________________________________#
def criaLista():
    # Inicializa a lista.
    lista = Lista()
    print("Beleza, você criou uma lista!")
    return lista


# _________________________________________________________ Módulo imprimeLista.
# Objetivo: Imprime todos os elementos da lista em tela.
# Entrada.: Lista.
# Saída...: Em tela.
# _____________________________________________________________________________#
def imprimeLista(lista):
    print("[ ________ RELATÓRIO ________ ]")

    # Imprime elementos válidos da lista.
    for i in range(lista.numeroElementos):
        print("[{}] Nome: {}".format(i, lista.alunos[i].nome), end="\t")
        print("Matricula: {}".format(lista.alunos[i].matricula))

    print("[{} elemento(s) ocupado(s) de {}]".format(lista.numeroElementos, tamanhoLista))


# _________________________________________________________ Módulo entradaDados.
# Objetivo: Gera um novo elemento (registro) com os dados informados pelo usuário.
# Entrada.: Nenhuma.
# Saída...: Novo elemento (registro).
# _____________________________________________________________________________#
def entradaDados():
    aluno = Pessoa()
    aluno.nome = input("Informe o nome.....: ")
    aluno.matricula = int(input("Informe a matricula: "))

    return aluno


# _______________________________________________________ Módulo incluiFimLista.
# Objetivo: Inclui um novo elemento ao final da lista válida (após o último elemento com dados).
# Entrada.: Lista.
# Saída...: Lista modificada com um novo elemento no final.
# _____________________________________________________________________________#
def incluiFimLista(lista):  # append

    # Se lista não atingiu o tamanho máximo de elementos,
    if lista.numeroElementos != len(lista.alunos):
        # inclui um novo elemento ao final da lista válida.
        lista.alunos[lista.numeroElementos] = entradaDados()

        # Incrementa o número de elementos válidos da lista.
        lista.numeroElementos += 1
        print("Sucesso na inclusão... bata-palmas!")
    else:
        # Caso contrário, informa:
        print("Lista lotadinha... desculpe!")

    return lista


# _____________________________________________________ módulo incluiInicioLista.

def incluiInicioLista(lista):
    if lista.numeroElementos != len(lista.alunos):
        # lista.alunos[0] = entradaDados()
        pos = 0
        # abre espaço para inserir o novo elemento
        for i in range(len(lista.alunos) - 1, pos - 1, -1):
            lista.alunos[i] = lista.alunos[i - 1]
        lista.alunos[pos] = entradaDados()
        lista.numeroElementos += 1

        print("")
        print("")
        print("Incluído elemento no início da lista")
    else:
        print("")
        print("")
        print("Lista cheia")
    return lista


# ____________________________________________ Módulo Ordenar lista (BubbleSort)

def ordenarLista(lista):
    aux = 0

    if lista.numeroElementos > 1:  # verifica se a lista possui elementos suficientes para ordenar
        for i in range(
                lista.numeroElementos - 1):  # vai varrer a lista diversas vezes, até que o laço inferior organize todos os elementos
            for j in range(lista.numeroElementos - 1):  # -1 pois o ultimo elementos nao vai ter com quem comparar  - deslocamento para a esquerda
                if lista.alunos[j].matricula > lista.alunos[j + 1].matricula:  # compara o elemento com o próximo, se for maior, efetua a troca.
                    # python permite a troca direta entre elementos podendo usar:
                    # l(j), l(j-1) = l(j -1), l(j)
                    aux = lista.alunos[j]  # porém, pode-se utilizar variável auxilar também
                    lista.alunos[j] = lista.alunos[j + 1]
                    lista.alunos[j + 1] = aux
        print("")
        print("")
        print("Lista ordenada com sucesso")
    else:
        print("")
        print("")
        print("A lista está vazia ou possui apenas 1 elemento.")

    return lista


# __________________________________________________ módulo excluiElementoLista.

def excluiElementoLista(lista):
     if lista.numeroElementos > 1:  # verifica se a lista não está vazia
        excluir = int(input("Digite o número da matricula que deseja excluir: "))  # lê a matricula que pretende excluir
        for i in range(lista.numeroElementos):  # varre a lista
            if excluir != lista.alunos[i].matricula:  # ao encontrar a matricula na lista:
                print("Essa matrícula não está cadastrada!")
            else:
                for j in range(i, lista.numeroElementos):
                    lista.alunos[j] = lista.alunos[j + 1]  # o elemento encontrado vai ser sobrescrito pelo seguinte, e assim sucessivamente até o final da lista + deslocamento para a direita
                    print("")
                    print("")
                    print("Dado excluído com sucesso.")


        else:                                                                                   
            print("")
            print("")
            print("A lista está vazia.")

            lista.numeroElementos -= 1
        return lista

# __________________________________________________ módulo excluiElementoLista.

def excluiNomeLista(lista):

    print("informe o nome que deseja excluir: ")

    nomeExcluir = input()

    for i in range(lista.numeroElementos):

        if nomeExcluir == lista.alunos[i].nome:
            print("{}", lista.alunos[i].matricula)
            print("Aluno excluido com sucesso.")

    lista.alunos[i] = 0
    lista.numeroElementos -= 1


    return lista



# ________________________________________________________ módulo consultarLista.

def consultarLista(lista):
    consulta = input("Digite a matrícula que deseja consultar: ")  # cria uma variavel para a matricula q deseja buscar

    if lista.numeroElementos > 1:  # verifica se a lista não esta vazia
        for i in range(lista.numeroElementos):  # varre a lista procurando a matricula desejada
            if consulta == lista.alunos[i].matricula:  # no momento em que encontrar a matricula printa
                print(lista.alunos[i].nome)
            else:  # caso não haja nenhum registro igual ao consultado
                print("Não há nenhum aluno cadastrado com esse matrícula. Tente Novamente.")

    else:  # caso a lista esteja vazia
        print("")
        print("")
        print("Desculpe, a lista está vazia!")

    return lista


# ______________________________________________________ método alterarElemento.
def alterarElemento(lista):
    alterar = int(input("Digite qual item da lista deseja modificar: "))  # guarda na variavel o indice a ser alterado

    if alterar > lista.numeroElementos:  # confere se o valor digitado existe
        print("A lista não possui tantos cadastros.")
    else:
        lista.alunos[
            alterar] = entradaDados()  # sobrescreve o elemento presente na posição escolhida por um novo registro
    print("Registro alterado com sucesso!")

    return lista


# _____________________________________________________________________________#
def menu():
    while True:
        print()
        print()
        print("[ ____ SISTEMA ACADÊMICO ____ ] ")
        print("1. Criar lista                  ")
        print("2. Inserir no fim da lista      ")
        print("3. Inserir no início da lista   ")
        print("4. Exclui elemento por matrícula")
        print("5. Exclui elemento por nome")
        print("6. Imprimir lista               ")
        print("7. Ordenar lista                ")
        print("8. Consultar por matrícula      ")
        print("9. Alterar elemento             ")
        print("10. Sair                         ")

        # Valida entrada de dados para opção aceitar apenas o menu.
        while True:
            opcaoMenu = input("Opção: ")
            if opcaoMenu >= '1' and opcaoMenu <= '8':
                break
        print()

        if opcaoMenu == '1':
            lista = criaLista()
        elif opcaoMenu == '2':
            lista = incluiFimLista(lista)
        elif opcaoMenu == '3':
            lista = incluiInicioLista(lista)
        elif opcaoMenu == '4':
            lista = excluiElementoLista(lista)
        elif opcaoMenu == '5':
            lista = excluiNomeLista(lista)
        elif opcaoMenu == '6':
            imprimeLista(lista)
        elif opcaoMenu == '7':
            lista = ordenarLista(lista)
        elif opcaoMenu == '8':
            lista = consultarLista(lista)
        elif opcaoMenu == '9':
            lista = alterarElemento(lista)
        else:
            print()
            print("[ ____ Ahhhh, que pena, você já vai... Volte sempre! ____ ]")
            break


# __________________________________________________________ Início do programa.
menu()
