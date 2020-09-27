#Entrega 22/09

# Tamanho definido da lista (constante).
tamanhoLista = 4

#Estrutura:

# ______________________________________ Área de definição do classe (registro).
class Pessoa:  # Nome da classe (registro).
    nome = ''  # Atributos nome e matrícula.
    matricula = 0


class Lista:  # Nome da classe (registro).
    alunos = [Pessoa()] * tamanhoLista  # Vetor de alunos de tamanhoLista (constante).
    numeroElementos = 0  # Número de elementos ocupados na lista.


# _____________________________________________________________________________#

#Funções

# Cria Lista
def criaLista():
    lista = Lista() #inicializa lista
    print("Lista criada")
    return lista
    
#Recebe os dados a serem informados pelo aluno
def entradaDados():
    aluno = Pessoa() #inicializa aluno
    aluno.nome = input("Nome:")  #solicita que seja informado nome do aluno
    aluno.matricula = input("Matrícula:") #solicita que seja informado a matricula do aluno
    return aluno

#Inclui elemento no final da lista

def incluiFimLista(lista):
    #validar se lista está cheia
    if lista.numeroElementos != len(lista.alunos):
            # inclui um novo elemento ao final da lista válida.
            lista.alunos[lista.numeroElementos] = entradaDados()
            print("Aluno adicionado no final da lista")
            lista.numeroElementos += 1  #contabiliza aluno adicionado
    else:
        print("Lista cheia")

    return lista


#Inclui elemento no início da lista (pos = 0)
def incluiInicioLista(lista):
    #validar se lista está cheia
    if lista.numeroElementos != len(lista.alunos):
      pos = 0  #posição inicial da lista
      
        # abre espaço para inserir o novo elemento
      for i in range(len(lista.alunos) - 1, pos - 1, -1): # percorre a lista até o final
            lista.alunos[i] = lista.alunos[i - 1] # deslocando elementos para a direita
      lista.alunos[pos] = entradaDados()  #informações digitadas pelo usuário serão inseridas na posição 0 da lista
      lista.numeroElementos += 1 #contabiliza aluno adicionado
      
    else:
        print("Lista cheia")

    return lista

# -> Exclui por nome da lista

def excluiNomeLista(lista):
    #valida se lista possui elementos a serem excluídos
    if lista.numeroElementos >= 1:
        nExcluir = input("Informe o nome que deseja excluir\n")
        for i in range (lista.numeroElementos-1): #percorre até o final da lista
            if nExcluir == lista.alunos[i].nome: # valida se nome a ser excluído é igual ao que consta na lista
                lista.alunos[i] = 0 # se condição acima for true então é atribuído a posição i o valor 0
        print("Aluno excluído com sucesso")
        lista.numeroElementos -= 1  #desconta o aluno excluído  
    else:
        print("a lista está vazia")
    return lista

#-> Exclui por matrícula da lista

def excluiMatLista(lista):
    #valida se lista possui elementos a serem excluídos
    if lista.numeroElementos >= 1:
        matExcluir = input("Informe o numero da matricula que deseja excluir\n")
        for i in range (lista.numeroElementos-1): #percorre até o final da lista
            if matExcluir == lista.alunos[i].matricula: # valida se nome a ser excluído é igual ao que consta na lista
                lista.alunos[i] = 0 # se condição acima for true então é atribuído a posição i o valor 0
        lista.numeroElementos -= 1 #desconta o aluno excluído
        print("Aluno excluído com sucesso")               
    else:
        print("a lista está vazia")
    return lista

#-> Imprime lista (relatório de toda lista)

def imprimeLista(lista):
    # Imprime elementos válidos da lista.
    for i in range (lista.numeroElementos): 
       print("[{}] Nome: {}".format(i, lista.alunos[i].nome), end="\t")
       print("Matricula: {}".format(lista.alunos[i].matricula))

    print("[{} elemento(s) ocupado(s) de {}]".format(lista.numeroElementos, tamanhoLista))

# -> Consulta elemento na lista por valor ou indíce de referencia indicado pelo usuario

def consultarLista(lista):
    consulta = input("Digite a matrícula que deseja consultar:\n ")  # cria uma variavel para a matricula q deseja buscar

    if lista.numeroElementos > 1:  # verifica se a lista não esta vazia
        for i in range(lista.numeroElementos-1):  # varre a lista procurando a matricula desejada
            if consulta == lista.alunos[i].matricula:  # no momento em que encontrar a matricula printa
                print("Nome:", lista.alunos[i].nome)
            else:  # caso não haja nenhum registro igual ao consultado
                print("Não há nenhum aluno cadastrado com esse matrícula. Tente Novamente.")

    else:  # caso a lista esteja vazia
        print("")
        print("")
        print("Desculpe, a lista está vazia!")

    return lista

# -> Ordena lista por valor indicado pelo usuario

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

#Editar elemento da lista (nome|matrícula)

def alterarElemento(lista):
    alterar = int(input("Digite qual item da lista deseja modificar: "))  # guarda na variavel o indice a ser alterado

    if alterar > lista.numeroElementos:  # confere se o valor digitado existe
        print("A lista não possui tantos cadastros.")
    else:
        lista.alunos[
            alterar] = entradaDados()  # sobrescreve o elemento presente na posição escolhida por um novo registro
    print("Registro alterado com sucesso!")

    return lista

def Menu():
    
    while True:
        print()
        print()
        print("[__Gerenciamento de Listas__]")
        print(" 1: Criar lista")
        print(" 2: Incluir elemento no fim da lista")
        print(" 3: Incluir elemento no início da lista")
        print(" 4: Imprimir lista")
        print(" 5: Excluir por nome da lista")
        print(" 6: Excluir por matrícula da lista")
        print(" 7: Consultar elemento da lista")
        print(" 8: Ordenar lista")
        print(" 9: Alterar nome da lista")
        print(" 10: Sair")
        
        # Valida entrada de dados para opção aceitar apenas o menu.
        while True:
            op = int(input("Opção: "))
            if op >= 1 and op <= 9:
                break
        print()
        if op == 1:
            lista = criaLista()
        elif op == 2:
            lista = incluiFimLista(lista)
        elif op == 3:
            lista = incluiInicioLista(lista)
        elif op == 4:
            lista = imprimeLista(lista)
        elif op == 5:
            lista = excluiNomeLista(lista)
        elif op == 6:
            lista = excluiMatLista(lista)
        elif op == 7:
            lista = consultarLista(lista)
        elif op == 8:
            lista = ordenarLista(lista)
        elif op == 9:
            lista = alterarElemento(lista)
        else:
            print()
            print("[Obrigada!]")
            break

Menu()
                
         
         

