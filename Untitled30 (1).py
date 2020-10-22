#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def usuario():
    #Pede informações do úsuario
    nome = input("Digite seu nome:")
    email = input("Digite seu e-mail:")
    rg = input("Digite seu RG:")
    endereco = input("Digite seu endereço:")
    arquivo = open("cliente.txt", 'a' ) #abre um arquivo txt 
    arquivo.write(nome + "#" + email + "#" + rg + "#" + endereco + "\n") #armazena as informações
    arquivo.close()

def editarusuario():
    #recupera o usuario
    rg = input("Digite o seu RG:")
    
    #abre o arquivo com todos os usuarios
    arquivo = open("cliente.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #pede as informaçoes editadas do usuario
    nome = input("Digite novamente o seu nome:")
    email = input("Digite o seu email:")
    endereco = input("Digite o seu endereço:")
    
    #procura a localização da linha onde as informações foram escritas
    index = 0
    for s in lines:
        if rg in s:
            break
        index = index + 1
    
    #armazena as novas informações    
    s = nome + "#" + email + "#" + rg + "#" + endereco + "\n" #
    lines[index] = s
    
    #subscreve as informações antigas   
    arquivo = open("cliente.txt" , "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()
    
    

    
def recuperarusuario():
    #recupera o usuario pelo rg
    rg = input("Digite o seu RG:")
    
    #abre o arquivo com todos os usuarios
    arquivo = open("cliente.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #procura a linha especifica no arquivo 
    index = 0
    for s in lines:
        if rg in s:
            break
        index = index + 1
        
    #printa na tela as informações recuperadas
    recuperarusu = lines[index]
    listusuario = recuperarusu.split("#")
    print("rg:" + listusuario[0])
    print("nome:" + listusuario[1])
    print("email:" + listusuario[2])
    print("endereco:" + listusuario[3])
    
    arquivo = open("cliente.txt" , "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()
    
    
def removerusu():
    #remove o usuario pelo rg
    rg = input("Digite seu rg:")
    
    #abre o arquivo txt
    arquivo = open("cliente.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #procura a linha especifica dentro de um arquivo
    index = 0
    for s in lines:
        if rg in s:
             break
        index = index + 1

    del (lines[index])
    
    
    arquivo = open("cliente.txt", "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()
    
    
def cadastrodelivros():
    #classifica as informações dos livros
    nomedolivro = input("Digite o nome do livro:")
    editora = input("Digite a editora do livro:")
    genero = input("Digite o genero do livro:")
    preco = input("Digite o preço do livro:")
    #abre um arquivo txt para armazenar as informações
    arquivo = open("livros.txt", 'a' )
    arquivo.write(nomedolivro + "#" + editora + "#" + genero + "#" + preco + "\n")
    arquivo.close()

def editarlivro(): 
    #pede o nome do livro para editar as informações
    nomedolivro = input("Digite o nome do livro:")
    
    #abre o arquivo com todos os livros
    arquivo = open("livros.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #pede as informaçoes editadas dos livros
    editora = input("Digite a editora do livro:")
    genero = input("Digite o gênero do livro:")
    preco = input("Digite o preço do livro")
    
    #acha a localização especifica na lista
    index = 0
    for s in lines:
        if nomedolivro in s:
            break
        index = index + 1
    
    #guarda as informações e as separa por '#'    
    s = nomedolivro + "#" + editora + "#" + genero + "#" + preco + "\n"
    lines[index] = s
    
    #abre, subscreve, e fecha o arquivo
    arquivo = open("livros.txt" , "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()

def recuperarliv():
    #recupera as informações pelo nome do livro
    nomedolivro = input("Digite o nome do livro:")
    
    #abre o arquivo com todos os usuarios
    arquivo = open("livros.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #Procura as informações em uma linha especificada
    index = 0
    for s in lines:
        if nomedolivro in s:
            break
        index = index + 1
        
    #printa na tela as informações
    recuperarliv = lines[index]
    listliv = recuperarliv.split("#")
    print("nome do livro:" + listliv[0])
    print("editora:" + listliv[1])
    print("genero:" + listliv[2])
    print("Preço do livro:" + listliv[3])
   
    arquivo = open("livros.txt" , "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()
    
def removerlivro():
    #remove um livro da lista pelo noem dele
    nomedolivro = input("Digite o nome do livro:")
    
    arquivo = open("livros.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #procura o nome do livro na lista 
    index = 0
    
    for s in lines:
        if nomedolivro in s:
             break
        index = index + 1
    
    #deleta o livro da lista
    del (lines[index])
    
    
    arquivo = open("livros.txt", "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()
    
    
    
def cadastrodefuncio():
    #pede as informações dos funcionários
    nome = input("Digite o nome do funcionario:")
    rg = input("Digite o rg do funcionario:")
    cpf = input("Digite o cpf do funcionario:")
    cargahoraria = input("Digite a carga horaria do funcionario:")
    turno = input("Digite o turno em que o funcionario trabalha:")
    extras = input("Digite informações extras sobre o funcionario:")
    
    #Cria um arquivo com as informações dos funcionários
    arquivo = open("funcionarios.txt", 'a' )
    arquivo.write(nome + "#" + rg + "#" + cpf + "#" + cargahoraria  + "#" + turno + "#" + extras + "\n")
    arquivo.close()

def editarfuncio():
    #pede o RG do funcionário 
    rg = input("Digite o rg do funcionario:")
    
    #abre o arquivo com todos os usuarios
    arquivo = open("funcionarios.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #pede as informaçoes editadas do usuario
    nome = input("Digite o nome do funcionario:")
    cpf = input("Digite o cpf do funcionario:")
    cargahoraria = input("Digite a carga horaria do funcionario:")
    turno = input("Digite o turno em que o funcionario trabalha:")
    extras = input("Digite informações extras sobre o funcionario:")
    
    #procura as informações do funcionário pelo rg
    index = 0
    for s in lines:
        if rg in s:
            break
        index = index + 1
     
    #adiciona as informações no arquivo
    s = rg + "#" + nome + "#"  + cpf + "#" + cargahoraria + "#" + turno + "#" +  extras + "\n"
    lines[index] = s
    
    #abre,subscreve e encerra o arquivo com as informações dos funcionários
    arquivo = open("funcionarios.txt" , "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()

def recuperarfuncio():
    rg = input("Digite o rg do funcionario:")
    #abre o arquivo com todos os usuarios
    arquivo = open("funcionarios.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #procura na lista a linha especifica
    index = 0
    for s in lines:
        if rg in s:
            break
        index = index + 1
        
    #printa na tela as informaçoes do funcionario
    recuperarfunc = lines[index]
    listfun = recuperarfunc.split("#")
    print("Nome do funcionário:" + listfun[0])
    print("RG do funcionário:" + listfun[1])
    print("CPF do funcionário:" + listfun[2])
    print("carga horaria:" + listfun[3])
    print("Turno em que o funcionário trabalha:" + listfun[3])
    print("Informações adicionais do funcionário:")
   
    arquivo = open("livros.txt" , "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()
    
def removerfuncio():
    rg = input("Digite o rg do funcionario:")
    
    #abre o arquivo e lê as linhas
    arquivo = open("funcionarios.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #procura a linha especifica
    index = 0
    for s in lines:
        if rg in s:
             break
        index = index + 1
    
    #deleta a linha
    del (lines[index])
    
    #subscreve a informação
    arquivo = open("funcionarios.txt", "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()
    
    
def produtos():
    nome = input("Digite o nome de um produto que foi comprado esse mês: [Higiene/ Móveis/ produtos no geral]")
    valor1 = input("Digite o valor do produto:")
    compra = input("Digite a data de compra do produto:")
    arquivo = open("produtos.txt", 'a' )
    arquivo.write(nome + "#" + valor1 + "#" + compra + "\n")
    arquivo.close()

def editarprodutos():
    nome = input("Digite o nome do produto:")
    arquivo = open("produtos.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #pede as informaçoes editadas do usuario
    valor1 = input("Digite o valor do produto:")
    compra = input("Digite a data de compra do produto:")
    
    index = 0
    for s in lines:
        if nome in s:
            break
        index = index + 1
        
    s = nome + "#"  + valor1 +  "#" + compra + "\n"
    lines[index] = s
    
    arquivo = open("produtos.txt" , "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()

    #produto2 = input("Digite o nome de um produto que foi comprado esse mês: [Higiene/ Móveis/ produtos no geral]")
    #valor2 = input("Digite o valor do produto:")
    
def recuperarproduto():    
    nome = input("Digite o nome do produto:")
    #abre o arquivo com todos os produtos
    arquivo = open("produtos.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #acha o produto especificado pelo nome do produto
    index = 0
    for s in lines:
        if nome in s:
            break
        index = index + 1
        
    #printa na tela as informações perdidas
    recuperarprodutos = lines[index]
    listprod = recuperarprodutos.split("#")
    print("Produto:" + listprod[0])
    print("Valor do produto comprado:" + listprod[1])
    print("Data de compra do produto:" + listprod[2])

    arquivo = open("produtos.txt" , "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()
    

def removerprodu():
    nome = input("Digite o nome do produto:")
    
    #abre o arquivo com a lista de produtos
    arquivo = open("produtos.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #acha o produto pelo nome
    index = 0
    for s in lines:
        if nome in s:
             break
        index = index + 1
    
    #deleta o produto
    del (lines[index])
    
    #subscreve as informações
    arquivo = open("produtos.txt", "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()
    
    
    
def salario():
    #pede informações sobre o salario dos funcionários
    rg = input("Digite o rg do funcionário a ser pago:")
    valor = input("Digite o valor do salário a ser pago:")
    obs = input("Alguma observação a ressaltar?:")
    
    #abre o arquivo com as informações
    arquivo = open("salario.txt", "a")
    arquivo.write(rg + "#" + valor + "#" + obs + "\n")
    arquivo.close()
                    
def editarsala():
    #abre o arquivo e procura pelo rg especificado
    rg = input("Digite o rg do funcionário:")
    arquivo = open("salario.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #pede as informaçoes editadas sobre o salário
    valor = input("Digite o valor do salário a ser pago:")
    obs = input("Alguma observação a ressaltar?")
    
    #procura pela linha especificada
    index = 0
    for s in lines:
        if rg in s:
            break
        index = index + 1
    #armazena informações    
    s = rg + "#" + valor + "#" + obs + "\n"
    lines[index] = s
    
    arquivo = open("salario.txt" , "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()

def recuperarsala():
    #abre o arquivo 
    rg = input("Digite o rg do funcionário:")

    arquivo = open("salario.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
   
    #encontra a linha especificada pelo rg
    index = 0
    for s in lines:
        if rg in s:
            break
        index = index + 1
        
    #printa na tela as informações do salário
    recuperarsala = lines[index]
    listsala = recuperarsala.split("#")
    print("Rg do funcionário:" + listsala[0])
    print("Valor do salário:" + listsala[1])
    print("Observação a ser feita:" + listsala[2])
    
    arquivo = open("salario.txt" , "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()

    

    
def removersalario():
    rg = input("Digite o rg do funcionário:")
    
    arquivo = open("salario.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #procura a linha especifica
    index = 0
    for s in lines:
        if rg in s:
             break
        index = index + 1
    
    #remove o cadastro do salário especificado
    del (lines[index])
    
    
    arquivo = open("salario.txt", "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()
    
    
def contas():
    senha = input("Crie uma senha:")
    conta = input("Digite uma conta, despesa extra ou produto a ser pago:")
    valor1 = input("Digite o valor a ser pago:")
   
    #abre um arquivo com as informações 
    arquivo = open("contas.txt", "a")
    arquivo.write(senha + "#" + conta + "#" + valor1 + "\n")
    arquivo.close()
                    

            
def editarcontas():
    senha = input("Digite sua senha:")
    #abre o arquivo e lê as linhas
    arquivo = open("contas.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    #pede as informaçoes editadas do usuario
    conta = input("Digite uma conta, despesa extra ou produto a ser pago:")
    valor1 = input("Digite o valor a ser pago:")
    
    #procura a linha especifica
    index = 0
    for s in lines:
        if senha in s:
            break
        index = index + 1
        
    s = senha + "#" + conta + "#" + valor1 + "\n" #
    lines[index] = s
    
    #subscreve as informações antigas   
    arquivo = open("contas.txt" , "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()
    
        
        
    
        
def recuperacont():
    senha = input("Digite a sua senha:")
    arquivo = open("contas.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    index = 0
    for s in lines:
        if senha in s:
            break
        index = index + 1
        
    recuperarcont = lines[index]
    listcont = recuperarcont.split("#")
    print("senha:" + listcont[0])
    print("conta:" + listcont[1])
    print("valor a ser pago:" + listcont[2])
    
    
    arquivo = open("contas.txt" , "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()
    
  

    
def removercont():
    senha = input("Digite sua senha:")
    
    arquivo = open("contas.txt", "r")
    lines = arquivo.readlines()
    arquivo.close()
    
    index = 0
    
    for s in lines:
        if senha in s:
             break
        index = index + 1

    del (lines[index])
    
    
    arquivo = open("contas.txt", "w")
    for s in lines:
        arquivo.write(s)
    arquivo.close()



def calculadora():
    #uma mini calculadora
    n1 = int(input('digite um número:'))
    n2 = int(input('digite outro número:'))
    menu = 0
    while menu != 10:
        print('Qual opção você deseja?')
        menu = float(input(('''
        [1]-Somar
        [2]-Subtrair
        [3]-Multiplicar
        [4]-Dividir
        [5]-Ver qual dos números é maior
        [6]-Escolher novos números
        [7]-Sair do progama
        Digite uma das opções:''')))
        if menu == 1:
            soma = n1 + n2
            print('O resultado da soma entre os números {} e {} é de: {}'.format(n1, n2, soma))
        if menu == 2:
            subtracao = n1 - n2
            print('O resultado da subtração entre os números {} e {} é de : {}' .format(n1, n2, subtracao))
        if menu == 3:
            multi = n1 * n2
            print('O resultado da multiplicação entre os números {} e {} é de: {}'.format(n1, n2, multi))
        if menu == 4:
            divi = n1 / n2
            print("O resultado da divisão entre os números {} e {} é de : {} " .format(n1, n2, divi))
        if menu == 5:
            if n1 > n2:
                print('o numero {} é maior que o número {}' .format(n1, n2))
            elif n2 > n1:
                print('o numero {} é maior que o número {}' .format(n2, n1))
            elif n2 == n1:
                print('Os números são iguais')
        
        if menu == 6:
            n1 = int(input('digite um novo número:'))
            n2 = int(input('digite outro número:'))
        elif menu == 7:
            print('O programa foi finalizado')
    
def fibonacci():
    #sequencia de Fibonacci
    f = int(input("Quantos termos você quer mostrar?")) 
    n1 = 0 
    n2 = 1
    print('{} → {}' .format(n1, n2), end ='')
    cont = 3
    while cont <= f:
        n3 = n1 + n2
        print(' → {}' .format(n3), end = '')
        n1 = n2
        n2 = n3
        cont += 1
    print("\n""fim")
    
    
    


     
    
    


# In[85]:


while True:
    a = int(input("Digite o número correspondente a ação que você deseja: [1]-usuario, [2]-livros, [3]-funcionários, [4]-salários, [5]-produtos, [6]-contas, [7]-Jogos Matemáticos, [8]-sair]"))
    if a == 1:
        while (True):
            b = int(input("Qual funcão de usuarios você deseja administrar? [[1]- adicionar usuario, [2]-editar usuario, [3]-recuperar usuario, [4]-remover usuario, [5]-parar]"))
            if (b == 1):
                usuario()
            elif (b == 2):
                editarusuario()
            elif (b == 3):
                recuperarusuario()
            elif (b == 4):
                removerusu()
            elif (b == 5):
                break
    elif a == 2:
        while(True):
            c = int(input("Qual função dos livros você deseja admnistrar? [[1]-cadastrar livros, [2]-editar cadastro de livros, [3]-recuperar um cadastro, [4]-remover livros, [5]-sair]"))
            if (c == 1):
                cadastrodelivros()
            elif (c == 2):
                editarlivro()
            elif (c == 3):
                recuperarliv()
            elif (c == 4):
                removerlivro()
            elif (c == 5):
                break
    elif a == 3:
        while(True):
            e = int(input("Qual função de funcionários você deseja acessar? [[1]-cadastro de funcionário, [2]-editar cadastro, [3]-recuperar o cadastro, [4]-remover cadastro de um funcionário, [5]-Sair]"))
            if (e == 1):
                cadastrodefuncio()
            elif (e == 2):
                editarfuncio()
            elif (e == 3):
                recuperarfuncio()
            elif (e == 4):
                removerfuncio()
            elif (e == 5):
                break
                  
    elif a == 4:
        while(True):
            d = int(input("Qual função de salários você deseja acessar? [1-Salarios,2-editar salários, 3- recuperar informações sobre o salário, 4-remover a informação de um salário, 5-parar]"))
            if (d == 1):
                salario()
            elif (d == 2):
                editarsala()
            elif (d == 3):
                recuperarsala()
            elif (d == 4):
                removersala()
            elif (d == 5):
                break
    elif a == 5:
        while(True):
            f = int(input("Qual função de produtos você deseja acessar? [1-cadastro de produtos, 2-editar produtos, 3-recuperar cadastro de produtos, 4- remover cadastro de um produto, 5-parar]"))
            if (f == 1):
                produtos()
            elif (f == 2):
                editarprodutos()
            elif (f == 3):
                recuperarproduto()
            elif (f == 4):
                removerprodu()
            elif (f == 5):
                break
                  
    elif a == 6:
        while(True):
            g = int(input("Digite qual opção de contas você deseja acessar: [1-Cadastrar uma conta,despesa, ou produto a ser pago;2-editar o cadastro; recuperar o cadastro; 4-remover o cadastro;5-parar]"))
            if (g == 1):
                contas()
            elif (g == 2):
                editarcontas()
            elif (g == 3):
                recuperacont()
            elif (g == 4):
                removercont()
            elif (g == 5):
                break
    elif a == 7:
        while(True):
            z = int(input("Digite qual opçao de calculos você deseja entrar: [[1]-minicalculadora, [2]-Fibonacci, [3]-sair]"))
            if z == 1:
                calculadora()
            if z == 2:
                fibonacci()
            if z == 3:
                break
            
    elif a == 8:
        print("Progama finalizado")
        break
       



# In[ ]:



            


# In[ ]:



    


# In[ ]:





# In[ ]:





# In[ ]:





# In[88]:





# In[ ]:



    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




       


    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[87]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




