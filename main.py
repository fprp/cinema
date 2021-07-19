from datetime import datetime
from random import choice
import csv
import sys

arq1 = open("./src/login/usuarios.txt", "r")
arquivo1 = arq1.readlines()
arq2 = open("./src/cartaz/elementos.txt", "r")
arquivo2 = arq2.readlines()

def tirarbarraEne(string):
    """Essa função retorna uma string sem o \n"""
    sembarran = ""
    for i in string:
        if(i != '\n'):
            sembarran += i
    return sembarran

usu = {}
conta = 0
tamanho = len(arquivo1)//3

def keyidenti():
    """Essa função retorna uma senha de identificação única para uma sessão"""
    caracters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    senha = ''

    for char in range(5):
            senha += choice(caracters)
    return  senha

while(conta < tamanho):
    usu[tirarbarraEne(arquivo1[3*conta])] = (tirarbarraEne(arquivo1[3*conta+1]),tirarbarraEne(arquivo1[3*conta+2]))
    conta+=1
ele = {}
conta = 0
tamanho = len(arquivo2)//8

while(conta < tamanho):
    ele[conta] =(tirarbarraEne(arquivo2[8*conta]),tirarbarraEne(arquivo2[8*conta+1]),tirarbarraEne(arquivo2[8*conta+2]),
                 tirarbarraEne(arquivo2[8*conta+3]), tirarbarraEne(arquivo2[8*conta+4]), tirarbarraEne(arquivo2[8*conta+5]),tirarbarraEne(arquivo2[8*conta+6]),
                 tirarbarraEne(arquivo2[8*conta+7]))
    conta+=1
    
def escolher_opcao3():
    """Essa função retorna uma opção dentre 1,2 e 3"""
    
    opcao = int(input("Escolha uma opção acima: "))

    while(opcao != 1 and opcao != 2 and opcao != 3):
        print("Opcao incorreta, por favor, escolher 1, 2 ou 3")
        opcao = int(input("Escolha uma opção: "))
        
    return opcao
    
def escolher_opcao():
    """Essa função retorna uma opcao dentre 1 e 2"""
    opcao = int(input("Escolha uma opção acima: "))

    while(opcao != 1 and opcao != 2):
        print("Opcao incorreta, por favor, escolher 1 ou 2")
        opcao = int(input("Escolha uma opção: "))
        
    return opcao

def escolher_opcao2():
    """Essa função retorna uma opção entre 1 e 10"""
    opcao = int(input("Escolha uma opção acima: "))

    while(opcao < 1 or opcao > 10):
        print("Opcao incorreta, por favor, escolher enter 1 e 7")
        opcao = int(input("Escolha uma opção: "))
        
    return opcao

def pegar_hora():
    """Essa função pega a data e hora atuais"""
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
    return data_e_hora_em_texto

def escrever_log(usuario,option):
    """Essa função escreve no arquivo de LOG todas as execuções do programa"""
    hora = pegar_hora()
    arq3 = open("./public/log.txt", "a")                   
    arq3.write("Quem Executou: " + usuario)
    arq3.write("\n")
    arq3.write("Quando Executou: " + hora)
    arq3.write("\n")
    if(option == 1):
        arq3.write("O que executou: Criação de nova sessão")
        arq3.write("\n")
    elif(option == 2):
        arq3.write("O que executou: Atualização de sessão")
        arq3.write("\n")
    elif(option == 3):
        arq3.write("O que executou: Vizualização de sessões")
        arq3.write("\n")
    elif(option == 4):
        arq3.write("O que executou: Busca de sessões")
        arq3.write("\n")
    elif(option == 5):
        arq3.write("O que executou: Remoção de sessão")
        arq3.write("\n")
    elif(option == 6):
        arq3.write("O que executou: Ordenação de sessões")
        arq3.write("\n")
    elif(option == 7):
        arq3.write("O que executou: Geração de planilha")
        arq3.write("\n")
    elif(option == 8):
        arq3.write("O que executou: Geração de relatório")
        arq3.write("\n")
    elif(option == 9):
        arq3.write("O que executou: Mudança de nível de acesso")
        arq3.write("\n")  
    elif(option == 10):
        arq3.write("O que executou: Logout")
        arq3.write("\n")  
        
    arq3.write("\n")

def escrever_arquivo():
    """Essa função salva os dados das sessões no arquivo quando o usuário faz o logout"""
    contador = 0
    quantidade = len(ele)
    arq1 = open("./src/login/usuarios.txt", "w")
    arq2 = open("./src/cartaz/elementos.txt", "w")
    while(contador<quantidade):
        arq2.write(ele[contador][0])
        arq2.write("\n")
        arq2.write(ele[contador][1])
        arq2.write("\n")
        arq2.write(ele[contador][2])
        arq2.write("\n")
        arq2.write(ele[contador][3])
        arq2.write("\n")
        arq2.write(ele[contador][4])
        arq2.write("\n")
        arq2.write(ele[contador][5])
        arq2.write("\n")
        arq2.write(ele[contador][6])
        arq2.write("\n")
        arq2.write(ele[contador][7])
        arq2.write("\n")
        contador += 1
        
    for i in usu:
        arq1.write(i)
        arq1.write("\n")
        for j in usu[i]:
            arq1.write(j)
            arq1.write("\n")
            
def menu_principal():
    """Esssa função mostra para o usuário as opções disponíveis, faz login, cadastra novo usuário ou encerra o sistema"""
    print("\nPopcorn Recife: Filmes em cartaz em Recife!\n")
    print("1 - Login")
    print("2 - Cadastrar Novo Usuario")
    print("3 - Sair")
    opcao = escolher_opcao3()
        
    if(opcao == 1):
        usuario = tela_login()
        menu_login(usuario)
    elif(opcao == 2):
        tela_cadastrar_usuario()
        menu_principal()
    else:
        print("\n-----------------------------------------------------------------------")
        print("Obrigado por utilizar o meu sistema, volte logo!.")
        print("-----------------------------------------------------------------------")
        escrever_arquivo()
        arq1.close()
        arq2.close()
        sys.exit()
    
def tela_login():
    """Essa função efetua o login ou mostra mensagem de erro caso não consiga efetuar"""
    control = -1
    while(control < 0):
        usuario = input("Qual o seu nome de usuario?: ")
        if(usuario in usu):  
            senha = input("Qual a sua senha: ")
            if(usu[usuario][0] == senha):
                return usuario
            else:
                print("Senha incorreta.")
        else:
            print("\n-----------------------------------------------------------------------")
            print("Usuario não encontrado, por favor, cadastre-se ou tente novamente.")
            print("-----------------------------------------------------------------------")
            menu_principal()
                
def tela_cadastrar_usuario():
    """Essa função cadastra novos usuários"""
    control = -1
    while(control < 0):
        usuario = input("Qual é o seu nome de usuario? ")
        if(usuario in usu):
            print("Nome de usuario ja existe, por favor, escolha outro.")
        else:
            control = 1
    
    senha = input("E sua senha? ")
    usu[tirarbarraEne(usuario)] = (tirarbarraEne(senha),"2")
    print("\n-----------------------------------------------------------------------")
    print("Usuario cadastrado com sucesso!")
    print("-----------------------------------------------------------------------")

def tela_cadastra_sessao(usuario):
    """Essa função cadastra novas sessões"""
    nomedofilme = input("Qual o nome do filme? ")
    numerodasala = input("Qual o número da sala? ")
    tipodefilme = input("O filme é em 2D ou 3D? ")
    datadofilme = input("A sessão é em que dia?[DD/MM/YYYY] ")
    horadofilme = input("A sessão começa de que horas?[HH:MM] ")
    keyunica = keyidenti()
    criacaodasessao = pegar_hora()
    campoupd = pegar_hora()
    quantidade = len (ele)
    ele[quantidade] = (tirarbarraEne(nomedofilme),tirarbarraEne(numerodasala),tirarbarraEne(tipodefilme),tirarbarraEne(datadofilme),tirarbarraEne(horadofilme),
                       tirarbarraEne(keyunica), tirarbarraEne(criacaodasessao),tirarbarraEne(campoupd))
    escrever_log(usuario,1)
    
    print("\n-----------------------------------------------------------------------")
    print("Sessão cadastrada com sucesso!")
    print("-----------------------------------------------------------------------")
    
def printar_filme(contador):
    """Essa função mostra os filmes em cartaz para o usuário"""
    print("\nNome do filme:", ele[contador][0])
    print("Número da sala:", ele[contador][1])
    print("2D ou 3D:", ele[contador][2])
    print("Dia do filme:", ele[contador][3])
    print("Hora do filme:", ele[contador][4])
    print("Key de identificação única:", ele[contador][5])
    print("Sessão disponibilizada em:", ele[contador][6])
    print("Última vez modificada em:", ele[contador][7])
    
def ver_sessoes_cadastradas(usuario):
    """Essa função auxilia para mostrar os filmes em cartaz"""
    quantidade = len(ele)
    contador = 0

    while (contador < quantidade):
        printar_filme(contador)
        contador += 1
    escrever_log(usuario,3)
        
def atualizar_sessao(usuario):
    """Essa função atualiza alguma sessão"""
    quantidade = len(ele)
    contador = 0

    while (contador < quantidade):
        print(contador + 1, end = '')
        printar_filme(contador)
        print("\n")
        contador += 1
        
    opcao= int(input("Qual sessão você deseja atualizar? "))
    print("O que você deseja alterar?")
    print("1 - Nome do filme")
    print("2 - Numero da sala")
    print("3 - 2D ou 3D")
    print("4 - Dia do filme")
    print("5 - Hora do filme")
    opcao2 = int(input())
    if(opcao2 == 1):
        nomedofilme = input("Qual é o novo nome do filme? ")
        data_e_hora_em_texto = pegar_hora()

        ele[opcao-1] = (tirarbarraEne(nomedofilme), ele[opcao-1][1],ele[opcao-1][2],ele[opcao-1][3],ele[opcao-1][4],
                        ele[opcao-1][5],ele[opcao-1][6],tirarbarraEne(data_e_hora_em_texto))
        print("\n-----------------------------------------------------------------------")
        print("Sessão atualizada com sucesso!")
        print("-----------------------------------------------------------------------")
    elif(opcao2 == 2):
        numerodasala = input("Qual é o novo numero da sala do filme?: ")
        data_e_hora_em_texto = pegar_hora()
        ele[opcao-1] = (ele[opcao-1][0],tirarbarraEne(numerodasala),ele[opcao-1][2],ele[opcao-1][3],ele[opcao-1][4],
                        ele[opcao-1][5],ele[opcao-1][6],tirarbarraEne(data_e_hora_em_texto))
        print("\n-----------------------------------------------------------------------")
        print("Sessão atualizada com sucesso!")
        print("-----------------------------------------------------------------------")
    elif(opcao2 == 3):
        doisdtresd = input("Qual o novo modo de exibição do filme? ")
        data_e_hora_em_texto = pegar_hora()
        ele[opcao-1] = (ele[opcao-1][0],ele[opcao-1][1],tirarbarraEne(doisdtresd),ele[opcao-1][3],ele[opcao-1][4],
                        ele[opcao-1][5],ele[opcao-1][6],tirarbarraEne(data_e_hora_em_texto))
        print("\n-----------------------------------------------------------------------")
        print("Sessão atualizada com sucesso!")
        print("-----------------------------------------------------------------------")
    elif(opcao2 == 4):
        diadofilme = input("Qual o novo dia do filme?[DD/MM/YYYY] ")
        data_e_hora_em_texto = pegar_hora()
        ele[opcao-1] = (ele[opcao-1][0],ele[opcao-1][1],ele[opcao-1][2],tirarbarraEne(diadofilme),ele[opcao-1][4],
                        ele[opcao-1][5],ele[opcao-1][6],tirarbarraEne(data_e_hora_em_texto))
        print("\n-----------------------------------------------------------------------")
        print("Sessão atualizada com sucesso!")
        print("-----------------------------------------------------------------------")
    elif(opcao2 == 5):
        horadofilme = input("Qual a nova hora do filme?[HH:MM] ")
        data_e_hora_em_texto = pegar_hora()
        ele[opcao-1] = (ele[opcao-1][0],ele[opcao-1][1],ele[opcao-1][2],ele[opcao-1][3],tirarbarraEne(horadofilme),
                        ele[opcao-1][5],ele[opcao-1][6],tirarbarraEne(data_e_hora_em_texto))
        print("\n-----------------------------------------------------------------------")
        print("Sessão atualizada com sucesso!")
        print("-----------------------------------------------------------------------")
        
    escrever_log(usuario,2)
def buscar_sessao(usuario):
    """Essa função busca alguma sessão de acordo com o paramentro indicado"""
    print("\nComo você deseja buscar a sessão? ")
    print("1 - Nome do filme")
    print("2 - Dia do filme")

    quantidade = len(ele)
    opcao = escolher_opcao()

    if(opcao == 1):
        filme = input("Qual filme deseja assistir?: ")
        contador = 0
        bool1 = False
        while(contador < quantidade):
            if(ele[contador][0] == filme):
                bool1 = True
                printar_filme(contador)
            contador += 1

        if(bool1 == False):
            print("\n-----------------------------------------------------------------------")
            print("Não foram encontrados nenhuma sessão para esse filme.")
            print("-----------------------------------------------------------------------")
 
    else:
        dia = input("Qual o dia para assistir o filme?[DD/MM/YYYY]")
        contador = 0
        bool2 = False
        while(contador < quantidade):
            if(ele[contador][3] == dia):
                bool2 = True
                printar_filme(contador)
            contador += 1

        if(bool2 == False):
            print("\n-----------------------------------------------------------------------")
            print("Não foram encontrados nenhuma sessão para esse dia.")
            print("-----------------------------------------------------------------------")
    escrever_log(usuario,4)
            
def permissao(usuario):
    """Essa função retorna se o usuário tem permissão para usar a funcionalidade do sistema"""
    if(usu[usuario][1] == '1'):
        return True
    else:
        return False    

def remover_sessao(usuario):
    """Essa função remove alguma sessão"""
    ver_sessoes_cadastradas(usuario)
    chave = input("Digite a Key de identificação única da sessão que deseja remover:")
    contador = 0
    quantidade = len(ele)
    excluiu = False
    while(contador < quantidade):
        if(chave == ele[contador][5]):
            ele.pop(contador)
            excluiu = True
            print("\n-----------------------------------------------------------------------")
            print("Sessão removida com sucesso!")
            print("-----------------------------------------------------------------------")
            contador += 1
            while(contador < quantidade): #shift nas key restantes 
                ele[contador - 1] = ele.pop(contador)
                contador += 1
        contador += 1
            
    if(excluiu == False):
        print("\n-----------------------------------------------------------------------")
        print("Não foi encontrado nenhuma sessão com essa key")
        print("-----------------------------------------------------------------------")
    escrever_log(usuario,5)
    
def ordenar_sessao(usuario):
    """Essa funcão ordena as sessões em ordem alfabetica"""
    quantidade = len(ele)
    contador = quantidade - 1
    contador2=0
    aux = {}
    while(contador>0):
        while(contador2 < contador):
            if (ele[contador2][0]>=ele[contador2+1][0]):
                aux = ele[contador2]
                ele[contador2]=ele[contador2+1]
                ele[contador2+1] = aux
            contador2 += 1
        contador -= 1
        
    print("\n-----------------------------------------------------------------------")
    print("Sessões ordenadas em ordem alfabética com sucesso!")
    print("-----------------------------------------------------------------------")
    escrever_log(usuario,6)
    
def gerar_planilha(usuario):
    """Essa função gera uma planilha com as informações das sessões"""
    contador = 0
    quantidade = len(ele)
    with open('./public/sessoes.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Nome do Filme', 'Número da sala', '2D/3D', 'Dia do Filme', 'Hora do Filme', 'Chave de Identificação', 'Dia da Disponibilização', 'Dia da Última Modificação'])
        while(contador<quantidade):
            writer.writerow(ele[contador])
            contador +=1
    print("\n-----------------------------------------------------------------------")
    print("Planilha criada com sucesso!")
    print("-----------------------------------------------------------------------")
    escrever_log(usuario,7)
    
def relatorio(usuario):
    """Essa função gera um relatório"""
    contador = 0
    quantidade = len(ele)
    
    rela = open("./public/relatorio.txt", "w")
    while(contador < quantidade):
        rela.write("Nome do Filme: " + ele[contador][0])
        rela.write("\n")
        rela.write("Número da Sala:" + ele[contador][1])
        rela.write("\n")
        rela.write("2D ou 3D:"+ ele[contador][2])
        rela.write("\n")
        rela.write("Dia do Filme:" + ele[contador][3])
        rela.write("\n")
        rela.write("Hora do Filme:" + ele[contador][4])
        rela.write("\n")
        rela.write("Key de Identificação Única:" + ele[contador][5])
        rela.write("\n")
        rela.write("Sessão Disponibilizada Em:" + ele[contador][6])
        rela.write("\n")
        rela.write("Última Vez Modificada Em:" + ele[contador][7])
        rela.write("\n")
        rela.write("\n")
        contador += 1
    print("\n-----------------------------------------------------------------------")
    print("Relatório gerado com sucesso!")
    print("-----------------------------------------------------------------------")
    escrever_log(usuario, 8)
    rela.close()
def mudar_acesso(usuario):
    """Essa função muda o nível de acesso de algum usuário no sistem"""
    for i in usu:
        print(i)
    qual = input("Qual usuário você deseja alterar o nível de acesso? ")
    if(qual in usu):
        print("1 - Conceder mais acesso")
        print("2 - COnceder menos acesso")
        opitione = escolher_opcao()
        if(opitione == 1):
            usu[qual] = (usu[qual][0],"1")
        else:
            usu[qual] = (usu[qual][0],"2")
        print("\n-----------------------------------------------------------------------")
        print("Nível de acesso alterado com sucesso!")
        print("-----------------------------------------------------------------------")
    else:
        print("\n-----------------------------------------------------------------------")
        print("Usuário não encontrado.")
        print("-----------------------------------------------------------------------")
    escrever_log(usuario, 9)
def menu_login(usuario):
    #falta permitir mudar o nivel de acesso
    """Essa função corresponde com o menu principal após fazer o login"""
    print("\nBem vindo", usuario)
    print("O que você gostaria de fazer? ")
    print("1 - Cadastrar sessão") #Já tem
    print("2 - Atualizar sessão")#Já tem
    print("3 - Ver sessões") #Já tem
    print("4 - Buscar sessão") #Já tem
    print("5 - Remover sessão")#Já tem
    print("6 - Ordenar sessões")#Já tem
    print("7 - Download das sessões em planilha")#Já tem
    print("8 - Gerar Relatório")#Já tem
    print("9 - Mudar Nível de Acesso de Algum Usuário")
    print("10 - Logout") #Já tem
    
    opcao = escolher_opcao2()

    if(opcao == 10):
        print("\n-----------------------------------------------------------------------")
        print("Logout efetuado com sucesso")
        print("-----------------------------------------------------------------------")
        escrever_log(usuario,10)
        menu_principal()
    elif(opcao == 1):
        if(permissao(usuario) == True):
            tela_cadastra_sessao(usuario)
        else:
            print("\n-----------------------------------------------------------------------")
            print("usuario não tem permissao.")
            print("-----------------------------------------------------------------------")
    elif(opcao == 3):
        ver_sessoes_cadastradas(usuario)
    elif(opcao == 2):
        if(permissao(usuario) == True):
            atualizar_sessao(usuario)
        else:
            print("\n-----------------------------------------------------------------------")
            print("usuario não tem permissao.")
            print("-----------------------------------------------------------------------")
    elif(opcao == 4):
        buscar_sessao(usuario)
    elif(opcao == 5):
        if(permissao(usuario) == True):
            remover_sessao(usuario)
        else:
            print("\n-----------------------------------------------------------------------")
            print("usuario não tem permissao.")
            print("-----------------------------------------------------------------------")
    elif(opcao == 6):
        ordenar_sessao(usuario)
    elif(opcao == 7):
        gerar_planilha(usuario)
    elif(opcao == 8):
        relatorio(usuario)
    elif(opcao == 9):
        if(permissao(usuario) == True):
            mudar_acesso(usuario)
        else:
            print("\n-----------------------------------------------------------------------")
            print("usuario não tem permissao.")
            print("-----------------------------------------------------------------------")
    menu_login(usuario)

menu_principal()