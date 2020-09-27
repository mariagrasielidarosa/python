N = int(input()) #ler quantidade  de repetições de caracteres

for i in range(N): #executa de acordo com a quantidade informada
    c = input() #ler os caracteres informados
    diamante = 0 # variavel que irá contabilizar o número de diamantes
    menor = 0 #variavel que irá contabilizar a quantidade de caracter = <
    for j in range(len(c)): # percorre os caracteres informados
        if(c[j] == '<'): # valida se em cada caracter informado existe um que seja = ao '<'
            menor += 1 # soma + 1 sinal identificado
        if(c[j] == '>' and menor > 0): # valida se em cada caracter informado existe um que seja = ao '>' e se a quantidade de sinais = '<' é maior que 0
            diamante += 1 # se condição acima é válida contabiliza mais um diamante
            menor -= 1 # desconsidera um sinal < que foi comparado
    print(diamante) #informa a quantidade de diamantes identificados 
            
