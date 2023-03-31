from tkinter import *
from time import sleep
import time
from datetime import datetime
import random
janela = Tk()
janela.title("Atividade Tkinter")

escolha1= Label(janela, text="1 = Tabuada")
escolha1.grid(column=0, row=1)

escolha2= Label(janela, text="2 = Media")
escolha2.grid(column=0, row=2)

escolha3= Label(janela, text="3 = Salário anual")
escolha3.grid(column=0, row=3)

escolha4= Label(janela, text="4 = Ordem Crescente")
escolha4.grid(column=0, row=4)

escolha5= Label(janela, text="5 = Area de um triangulo")
escolha5.grid(column=0, row=5)

escolha6= Label(janela, text="6 = Converter C° em F°")
escolha6.grid(column=0, row=6)

escolha7= Label(janela, text="7 = Gasolina Consumida")
escolha7.grid(column=0, row=7)

escolha8= Label(janela, text="8 = Relogio Digital")
escolha8.grid(column=0, row=8)

escolha9= Label(janela, text="9 = Sortear Aluno (Em desenvolvimento)")
escolha9.grid(column=0, row=9)

escolha10= Label(janela, text="10 = Programa de Votação (Em desenvolvimento)")
escolha10.grid(column=0, row=10)

def enter():
    numero_escolhareal = numero_escolha.get()
    numero_escolhaint = int(numero_escolhareal)
    if numero_escolhaint == 1:
        def escolheu1():
            numero_tabuadaget= numero_tabuada.get()
            numero_tabuadafloat= int(numero_tabuadaget)
            contador = 0
            linha= 177
            for i in range(11):
                multi = numero_tabuadafloat*contador
                texto_tabuada = Label(janela, text= str(numero_tabuadafloat)+" X "+str(contador)+" = "+str(multi))
                texto_tabuada.grid(column=0, row=linha)
                contador += 1
                linha += 1
        info_tabuada= Label(janela, text="Digite o numero para a tabuada")
        info_tabuada.grid(column=0, row=14)
        numero_tabuada = Entry(janela)
        numero_tabuada.grid(column=0, row=15)
        botao_enter = Button(janela, text="Enter",command= escolheu1)
        botao_enter.grid (column=0, row=16)
    elif numero_escolhaint == 2:
        #nome
        info_media1= Label(janela, text="Digite o nome do aluno")
        info_media1.grid(column=0, row=14)
        nome_media = Entry(janela)
        nome_media.grid(column=0, row=15)
        #turma
        info_media2= Label(janela, text="Digite a turma do aluno")
        info_media2.grid(column=0, row=16)
        turma_media = Entry(janela)
        turma_media.grid(column=0, row=17)
        #nota 1
        info_media3= Label(janela, text="Digite a nota 1")
        info_media3.grid(column=0, row=18)
        nota1_media = Entry(janela)
        nota1_media.grid(column=0, row=19)
        #nota 2
        info_media4= Label(janela, text="Digite a nota 2")
        info_media4.grid(column=0, row=20)
        nota2_media = Entry(janela)
        nota2_media.grid(column=0, row=21)
        #nota 3
        info_media5= Label(janela, text="Digite a nota 3")
        info_media5.grid(column=0, row=22)
        nota3_media = Entry(janela)
        nota3_media.grid(column=0, row=23)
        #nota 4
        info_media6= Label(janela, text="Digite a nota 4")
        info_media6.grid(column=0, row=24)
        nota4_media = Entry(janela)
        nota4_media.grid(column=0, row=25)
       
       
        def escolheu2():          
            compara = 0
            melhor_nota = 0
            melhor_aluno= ""
            melhor_turma = ""
            melhornotalabel = Label(janela, text="Melhor nota até o momento é : "+str(melhor_nota)+", do aluno "+melhor_aluno+" da turma"+melhor_turma)
            melhornotalabel.grid(column=0, row=28)          
            nomeget= nome_media.get()
            turmaget= turma_media.get()
            nota1get = nota1_media.get()
            nota1float= float(nota1get)
            nota2get = nota2_media.get()
            nota2float= float(nota2get)
            nota3get = nota3_media.get()
            nota3float= float(nota3get)
            nota4get = nota4_media.get()
            nota4float= float(nota4get)
            media = (nota1float+nota2float+nota3float+nota4float)/4
            media = round(media,2)
            if media > compara:
                compara = media
                melhor_nota = media
                melhor_aluno = nomeget
                melhor_turma = turmaget
            if media >= 6:
                    medialabelaprov = Label(janela, text= nomeget+" foi aprovado, com a media de "+str(media)+", sendo as notas: "+str(nota1get)+","+str(nota2get)+","+str(nota3get)+","+str(nota4get))    
                    medialabelaprov.grid(column=0, row=27)
            elif media >= 4 and media < 6:
                    medialabelrec = Label(janela,text= nomeget+" esta de recuperação, com a media de "+str(media)+", sendo as notas: "+str(nota1get)+","+str(nota2get)+","+str(nota3get)+","+str(nota4get))
                    medialabelrec.grid(column=0, row=27)
            elif media < 4:
                    medialabelrepro = Label(janela,text= nomeget+" esta reprovado, com a media de "+str(media)+", sendo as notas: "+str(nota1get)+","+str(nota2get)+","+str(nota3get)+","+str(nota4get))
                    medialabelrepro.grid(column=0, row=27)
        #botão
        botao_enter1 = Button(janela, text="Enter",command= escolheu2)
        botao_enter1.grid (column=0, row=26)
    elif numero_escolhaint == 3:
       
        #Salario
        info_salario= Label(janela, text="Digite seu salario")
        info_salario.grid(column=0, row=14)
        salario_entry = Entry(janela)
        salario_entry.grid(column=0, row=15)
        #Desconto
        info_desc= Label(janela, text="Digite seu desconto mensal")
        info_desc.grid(column=0, row=16)
        desc_entry = Entry(janela)
        desc_entry.grid(column=0, row=17)
       
        def escolheu3():
            salarioget = salario_entry.get()
            salariofloat = float(salarioget)
            descget = desc_entry.get()
            descfloat = float(descget)
            full = (salariofloat*13)-(descfloat*13)
            info_salario2= Label(janela, text="Seu desconto foi R$"+str(descfloat*13))
            info_salario2.grid(column=0, row=18)
            info_salario3= Label(janela, text="Seu salario no final do ano será de R$"+str(full))
            info_salario3.grid(column=0, row=19)
        #botão
        botao_enter1 = Button(janela, text="Enter",command= escolheu3)
        botao_enter1.grid (column=0, row=20)
   
    elif numero_escolhaint == 4:
        #Numero 1
        numero1_info= Label(janela, text="Digite o numero 1")
        numero1_info.grid(column=0, row=14)
        numero1_entry = Entry(janela)
        numero1_entry.grid(column=0, row=15)
        #Numero 2
        numero2_info= Label(janela, text="Digite o numero 2")
        numero2_info.grid(column=0, row=16)
        numero2_entry = Entry(janela)
        numero2_entry.grid(column=0, row=17)
        #Numero 3
        numero3_info= Label(janela, text="Digite o numero 3")
        numero3_info.grid(column=0, row=18)
        numero3_entry = Entry(janela)
        numero3_entry.grid(column=0, row=19)
        #Numero 4
        numero4_info= Label(janela, text="Digite o numero 4")
        numero4_info.grid(column=0, row=20)
        numero4_entry = Entry(janela)
        numero4_entry.grid(column=0, row=21)
        #Numero 5
        numero5_info= Label(janela, text="Digite o numero 5")
        numero5_info.grid(column=0, row=22)
        numero5_entry = Entry(janela)
        numero5_entry.grid(column=0, row=23)        
        #Numero 6
        numero6_info= Label(janela, text="Digite o numero 6")
        numero6_info.grid(column=0, row=24)
        numero6_entry = Entry(janela)
        numero6_entry.grid(column=0, row=25)
        #Numero 7
        numero7_info= Label(janela, text="Digite o numero 7")
        numero7_info.grid(column=0, row=26)
        numero7_entry = Entry(janela)
        numero7_entry.grid(column=0, row=27)
        #Numero 8
        numero8_info= Label(janela, text="Digite o numero 8")
        numero8_info.grid(column=0, row=28)
        numero8_entry = Entry(janela)
        numero8_entry.grid(column=0, row=29)
        #Numero 9
        numero9_info= Label(janela, text="Digite o numero 9")
        numero9_info.grid(column=0, row=30)
        numero9_entry = Entry(janela)
        numero9_entry.grid(column=0, row=31)
        #Numero 10
        numero10_info= Label(janela, text="Digite o numero 10")
        numero10_info.grid(column=0, row=32)
        numero10_entry = Entry(janela)
        numero10_entry.grid(column=0, row=33)
        def escolheu4():
            numero1_float = float(numero1_entry.get())
            numero2_float = float(numero2_entry.get())
            numero3_float = float(numero3_entry.get())
            numero4_float = float(numero4_entry.get())
            numero5_float = float(numero5_entry.get())
            numero6_float = float(numero6_entry.get())
            numero7_float = float(numero7_entry.get())
            numero8_float = float(numero8_entry.get())
            numero9_float = float(numero9_entry.get())
            numero10_float = float(numero10_entry.get())

           
            numeros=[numero1_float,numero2_float,numero3_float,numero4_float,numero5_float,numero6_float,numero7_float,numero8_float,numero9_float,numero10_float]
            numeros.sort()
            ordem_crescente = Label(janela, text=numeros)
            ordem_crescente.grid(column=0, row=35)
        botao_enter1 = Button(janela, text="Enter",command= escolheu4)
        botao_enter1.grid (column=0, row=34)
   
    elif numero_escolhaint == 5:
        #Base
        base_info= Label(janela, text="Digite a base do seu triangulo")
        base_info.grid(column=0, row=14)
        base_entry = Entry(janela)
        base_entry.grid(column=0, row=15)
        #Altura
        altura_info= Label(janela, text="Digite a altura do seu triangulo")
        altura_info.grid(column=0, row=16)
        altura_entry = Entry(janela)
        altura_entry.grid(column=0, row=17)
        def escolheu5():
            base_float = float(base_entry.get())
            altura_float = float(altura_entry.get())
            area_triangulo = (base_float*altura_float)/2
            area_info= Label(janela, text="A area do seu triangulo é de: "+str(area_triangulo))
            area_info.grid(column=0, row=18)
        botao_enter1 = Button(janela, text="Enter",command= escolheu5)
        botao_enter1.grid (column=0, row=19)
   
    elif numero_escolhaint == 6:
        #Temp
        temp_info= Label(janela, text="Informe a temperatura em C° para transformar em F°")
        temp_info.grid(column=0, row=14)
        temp_entry = Entry(janela)
        temp_entry.grid(column=0, row=15)
       
        def escolheu6():
            temp_float = float(temp_entry.get())
            F= (9*temp_float+160)/5
            F_info= Label(janela, text="Sua temperatura em Fahrenheit é de: "+str(F))
            F_info.grid(column=0, row=16)
        botao_enter1 = Button(janela, text="Enter",command= escolheu6)
        botao_enter1.grid (column=0, row=17)
   
    elif numero_escolhaint == 7:
        #Tempo
        time_info= Label(janela, text="Informe o tempo da viagem em Horas")
        time_info.grid(column=0, row=14)
        time_entry = Entry(janela)
        time_entry.grid(column=0, row=15)
        #Velocidade
        speed_info= Label(janela, text="Informe a velocidade media da viagem em Kilometros")
        speed_info.grid(column=0, row=16)
        speed_entry = Entry(janela)
        speed_entry.grid(column=0, row=17)
        def escolheu7():
            time_float = float(time_entry.get())
            speed_float = float(speed_entry.get())
            dis = time_float*speed_float
            litros_utilizados = dis/12
            litros_utilizados = round(litros_utilizados,2)
            total_info= Label(janela, text="A quantidade de litros de gasolina ultizados nessa viagem sera de "+str(litros_utilizados)+" Litros, com a velocidade media de "+str(speed_float)+" , a distancia total foi de "+str(dis)+" Kilometros, com o tempo de "+str(time_float)+" hora(s)")
            total_info.grid(column=0, row=18)
        botao_enter1 = Button(janela, text="Enter",command= escolheu7)
        botao_enter1.grid (column=0, row=19)
   
    elif numero_escolhaint == 8:
        def escolheu8():
            data_e_hora_atuais = datetime.now()
            curr_time = time.localtime()
            curr_clock = time.strftime("%H:%M:%S", curr_time)
            data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y")
            #data
            data_info= Label(janela, text=data_e_hora_em_texto)
            data_info.grid(column=0, row=14)
            #Tempo
            hora_info= Label(janela, text=curr_clock)
            hora_info.grid(column=0, row=15)
        botao_enter1 = Button(janela, text="Clique para saber as horas exatas",command= escolheu8)
        botao_enter1.grid (column=0, row=19)

    #elif numero_escolhaint == 9:
    #  
    #   qntd_info= Label(janela, text="Informe a quantidade de alunos")
    #   qntd_info.grid(column=0, row=14)
    #   qntd_entry = Entry(janela)
    #   qntd_entry.grid(column=0, row=15)
    #   def escolheu9():
    #        nomes= []
    #        a= 0
    #        qntd_get= int(qntd_entry.get())
    #        while a < qntd_get:
    #            nome_info = Label(janela, text="Informe o nome do aluno")
    #            nome_info.grid (column=0, row=18+a*2)
    #            nome_entry = Entry(janela)
    #            nome_entry.grid(column=0, row=19+a*2)
    #            a +=1
    #        def sorteio():
    #            nomes.append(nome_entry)
    #            nome_escolhido= random.choice(nomes)
    #            resultado = Label(janela, text=nome_escolhido)
    #            resultado.grid (column=0, row=int(qntd_entry.get())+19+a)
    #        botao_enter2 = Button(janela, text="Sortear",command= sorteio)
    #        botao_enter2.grid (column=0, row=17)
    #   botao_enter1 = Button(janela, text="Enter",command= escolheu9)
    #   botao_enter1.grid (column=0, row=16)
    # (NÃO ESTA FUNCIONANDO)

    #elif numero_escolhaint == 10:
    #    def votacao_fun():
    #        Quantidade_info= Label(janela, text="Informe a quantidade de candidatos")
    #        Quantidade_info.grid(column=0, row=14)
    #        Quantidade = Entry(janela)
    #        Quantidade.grid(column=0, row=15)
    #       Candidatos= []
    #        Partido= []
    #       Votos= []
    #        def vai():
    #            for a in range(int(Quantidade.get())):
    #                Pessoas_info= Label(janela, text="Insira um nome")
    #                Pessoas_info.grid(column=0, row=16+a*2)
    #                Pessoas= Entry(janela)
    #                Pessoas.grid(column= 0, row=17+a*2)
    #                Candidatos.append(Pessoas)
    #                Numeros_info= Label(janela,text="Numero do partido")
    #                Numeros_info.grid(column=0,row=18+a*2)
    #                Numeros= Entry(janela)
    #                Partido.append(int(Numeros.get()))
    #            global dicionario
    #            dicionario = dict([("Candidatos",Candidatos), ("Partidos_Respectivos",Partido)])
    #            Quantidade_votos_info= Label(janela,text="Quantos votos serão?")
    #            Quantidade_votos_info.grid(column=0,row=19+a*2)
    #            Quantidade_votos = Entry(janela)
    #            Quantidade_votos.grid(column=0,row=20+a*2)
    #            for b in range(int(Quantidade_votos.get())):
    #                print(dicionario)
    #                Voto_info= Label(janela,text="Informe seu voto")
    #                Voto_info.grid(column=0,row=201+a*2)
    #                Voto = Entry(janela)
    #                Voto.grid(column=0,row=22+a*2)
    #                Votos.append(int(Voto.get()))
    #                def most_frequent(Votos):
    #                   for i in range(Quantidade):
    #                        if  max(set(Votos), key = Votos.count) == dicionario["Partidos_Respectivos"][i]:
    #                            info_resultado= Label(janela,text=dicionario["Candidatos"][i])
    #                            info_resultado.grid(column=0,row=23+a*2)
    #                            info_resultado2 = Label(janela,text="Foi eleito(a)")
    #                            info_resultado2.grid(column=0,row=24+a*2)
    #            botao_resultado= Button(janela,text="Clique para saber o resultado",command=most_frequent(Votos))
    #            botao_resultado.grid(column=0,row=25+a*2)
    #
    #        botao_enter1 = Button(janela, text="iniciar",command= vai)
    #        botao_enter1.grid (column=0, row=52)
    #        
    #    botao_enter1 = Button(janela, text="enter",command= votacao_fun)
    #    botao_enter1.grid (column=0, row=51)
    # (NÃO ESTA FUNCIONANDO)
       
                       


info_escolha= Label(janela, text="Escolha um numero de 0 a 10")
info_escolha.grid(column=0, row=11)
numero_escolha = Entry(janela)
numero_escolha.grid(column=0, row=12)
botao_enter = Button(janela, text="Enter",command= enter)
botao_enter.grid (column=0, row=13)


janela.mainloop()