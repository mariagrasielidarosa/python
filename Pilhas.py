# Tamanho definido da estrutura (constante).
tamanhoEstrutura = 3

# ______________________________________ Área de definição do classe (registro).
class Pessoa:  # Nome da classe (registro).
    nome = ''  # Atributos nome e matrícula.
    matricula = 0

class Pilha:   # Nome da classe (registro).
    alunos = [Pessoa()]*tamanhoEstrutura  # Vetor de alunos de tamanhoEstrutura (constante).
    numeroElementos = 0   # Número de elementos ocupados na estrutura.
# _____________________________________________________________________________#


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


# _____________________________________________________ Módulo imprimeEstrutura.
# Objetivo: Imprime todos os elementos da estrutura em tela.
# Entrada.: Estrutura.
# Saída...: Em tela.
# _____________________________________________________________________________#
def imprime(pilha):
  print("[ ________ RELATÓRIO ________ ]")
  
  # Imprime elementos válidos da estrutura.
  for i in range(pilha.numeroElementos):
    print("[{}] Nome: {}".format(i, pilha.alunos[i].nome), end = "\t")
    print("Matricula: {}".format(pilha.alunos[i].matricula))
  
  print("[{} elemento(s) ocupado(s) de {}]".format(pilha.numeroElementos, tamanhoEstrutura))


# ________________________________________________________ Módulo criaEstrutura.
# Objetivo: Cria estrutura com nº de elementos informado pelo usuário.
# Entrada.: Nenhuma.
# Saída...: Estrutura criada.
# _____________________________________________________________________________#
def cria():

  # Inicializa a estrutura.
  pilha = Pilha()
  print("Beleza, você criou uma estrutura!") 
  return pilha


# ____________________________________________________________ Módulo incluiFim.
# Objetivo: Inclui um novo elemento ao final da estrutura válida (após o último elemento com dados).
# Entrada.: Estrutura.
# Saída...: Estrutura modificada com um novo elemento no final.
# _____________________________________________________________________________#
def incluiFim(pilha):
  
  if pilha.numeroElementos == tamanhoEstrutura:
    print("Overflow!")
  else:
    pilha.alunos[pilha.numeroElementos] = entradaDados()
    pilha.numeroElementos += 1
    print("Deu certinho, empilhado!")
  #return pilha  
  

# ____________________________________________________________ Módulo excluiFim.
# Objetivo: Exclui um elemento do final da estrutura.
# Entrada.: Estrutura.
# Saída...: Estrutura modificada sem um elemento.
# _____________________________________________________________________________#
def excluiFim(pilha):
  print()
  

# _________________________________________________________________ Módulo menu.
# Objetivo: Apresenta o menu do programa.
# Entrada.: Nenhuma.
# Saída...: Nenhuma.
# _____________________________________________________________________________#
def menu():
  while True:
    print()
    print()
    print("[ ____ SISTEMA ACADÊMICO ____ ] ")
    print("1. Criar                        ")
    print("2. Inserir no fim (topo)     ")
    print("3. Exclui do fim (topo)         ")
    print("4. Imprimir                     ")
    print("5. Sair                         ")

    # Valida entrada de dados para opção aceitar apenas o menu.
    while True:
      opcaoMenu = input("Opção: ")
      if opcaoMenu >= '1' and opcaoMenu <= '5':
        break
    print()
    
    if opcaoMenu == '1':
      pilha = cria()
    elif opcaoMenu == '2':
      pilha = incluiFim(pilha)
    elif opcaoMenu == '3':
      pilha = excluiFim(pilha)
    elif opcaoMenu == '4':
      imprime(pilha)
    else:
      print()
      print("[ ____ Vou sentir saudades! Volte sempre! ____ ]")
      break


# __________________________________________________________ Início do programa.
menu()
