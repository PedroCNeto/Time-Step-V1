import pygame
from pygame import mixer
import random
from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, KEYDOWN, K_x, K_z
from pygame.locals import *
from pygame.time import Clock

#DANDO INICIO AO PYGAME
mixer.init()
pygame.init()

#PALETA DE CORES
cores = {
    "preto" : pygame.Color(0,0,0),
    "azul" : pygame.Color(0,0,255),
    "verde" : pygame.Color(0,255,0),
    "amarelo" : pygame.Color(255,0,255),
    "roxo" : pygame.Color(128,0,128),
    "vermelho" : pygame.Color(255,0,0),
    "branco" : pygame.Color(255,255,255),
    }       

#CRIANDO AS DIMENSÕES DA RESOLUÇÃO
class Window:
    __width = 0 #largura
    __height = 0 #altura
    __color = pygame.Color(0, 0, 0) #cor

    def __init__(self, largura, altura, color): #construtor
        self.__width = largura
        self.__height = altura
        self.__color = color

    def dim(self): #retorna tamanho da tela
        return (self.__width, self.__height)

    def cor(self): #retorna a cor da janela
        return self.__color
windowresolution = Window(1024, 768, cores["preto"])
janeladogame = pygame.display.set_mode(windowresolution.dim())
pygame.display.set_caption("Time Step")

#GUARDANDO AS INFORMAÇÕES DA QUANTIDADE DE PIXELS
x0, y0 = (0, 0) #PONTO 0 (ESQUERDA EM CIMA)
x1, y1 = windowresolution.dim() #LADO CONTRARIO (DIREITA EM BAIXO)

#DEFININDO OS FRAMES POR SEGUNDO (FPS)
clock = pygame.time.Clock() 
clock.tick(30) #DEFININDO OS FRAMES (30)
fps = clock.tick(30) #CRIANDO UMA VARIAVEL PARA O FPS

#VARIAVEL QUE DIZ SE O JOGO ESTA RODANDO
running = True





#DADOS DOS PERSONAGENS, INIMIGOS E NPCS

#DADOS DOS PERSONAGENS CONTROLAVEIS
class personagens():
    class henry: #DADOS DO PERSONAGEM HENRY
        maxhp = 100
        hp = 100
        forca = 0
        precisao = 0
        carisma = 0
        res = 0
        agility = 0
        pontosliberados = 20
    class jonh: #DADOS DO PERSONAGEM JOHN
        maxhp = 100
        hp = 100
        forca = 0
        precisao = 0
        carisma = 0
        res = 0
        agility = 0
        pontosliberados = 20
    class yuri: #DADOS DO PERSONAGEM YURI
        maxhp = 100
        hp = 100
        forca = 0
        precisao = 0
        carisma = 0
        res = 0
        agility = 0
        pontosliberados = 20

#FUNÇÃO DE TESTE
def statsupdated():#FUNÇÃO PARA DIZER SE ALGUM DOS TESTE ESTÁ FUNCIONANDO
    print("atualizado")

#LISTA DOS PERSONAGENS
personagensvivos = []
inimigosvivos = []

#DADOS DOS INIMIGOS
class inimigos():
    class homemdascavernas1:
        maxhp = 90
        hp = 90
        forca = 10
        precisao = 1
        carisma = 2
        res = 5
        agility = 4
    class homemdascavernas2:
        maxhp = 90
        hp = 90
        forca = 10
        precisao = 2
        carisma = 2
        res = 5
        agility = 6
    class homemdascavernas3:
        maxhp = 90
        hp = 90
        forca = 10
        precisao = 1
        carisma = 2
        res = 5
        agility = 5


          







#ALGUMAS FONTES
fonts1 = pygame.font.SysFont('Bahnschrift', 60)
fonts2 = pygame.font.SysFont('Bahnschrift', 20)
fonts3 = pygame.font.SysFont('Bahnschrift', 35)

#DEFININDO AS CLASSES E FUNÇÕES QUE SERÃO USADAS PARA FACILITAR A CRIAÇÃO DE CERTOS OBJETOS DE CLIQUE E HUD
class barradevida(): #CRIA A BARRA DE VIDA TANTO A PARTE VERMELHA TANTO A VERDE(QUE VARIA COM BASE NA VIDA PERDIDA)
    def __init__(self, x, y, hp, maxhp):
        self.x = x
        self.y = y
        self.hp = hp
        self.maxhp = maxhp
    
    def montagembarradevida(self, hp):
        #atualizada a % da vida
        self.hp = hp
        #valor da vida da parte verda que vai variar
        divisordevida = self.hp / self.maxhp
        pygame.draw.rect(janeladogame, cores["vermelho"], (self.x, self.y, 125, 20))
        pygame.draw.rect(janeladogame, cores["verde"], (self.x, self.y, 125 * divisordevida, 20))
def desenhar_texto(texto, fonte, cor, x, y): #DESENHO O TEXTO NA TELA
    imagemtexto = fonte.render(texto, True, cor)
    janeladogame.blit(imagemtexto, (x, y))
class botoes(): #CRIA OS BOTOES NA TELA
    
    #MONTA RETANGULOS QUE PODEM TER FUNÇÕES
    def __init__(self, cor, x, y , largura, altura, funcao):
        self.cor = cor
        self.x = x
        self.y = y 
        self.largura = largura
        self.altura = altura
        self.funcao = funcao
           
    #MONTA UM BOTAO VISIVEL E SOLIDO
    def montagemdefabrica(self, win):
        pygame.draw.rect(win, self.cor, (self.x, self.y, self.largura, self.altura), 0)

    #MONTA UM BOTÃO INVISIVEL
    def montandobotaoinvisivel(self, win):
        pygame.draw.rect(win, self.cor,(self.x, self.y, self.largura, self.altura), -1)

    #FUNÇÃO QUE É UTILIZADA PARA UTILIZAR OS BOTOES
    def clique(self, pos, funcao):

        if pos[0] > self.x and pos[0] < self.x + self.largura:
            if pos[1] > self.y and pos[1] < self.y + self.altura:
                funcao()
                return True
            else:
                return False  
def AIdosBots():#"INTELIGENCIA ARTIFICIAL"  
#FUNCAO DA ESQUIVA
    henryprecisamaluco = personagens.henry.precisao / 2
    yuriprecisamaluco = personagens.yuri.precisao / 2
    johnprecisamaluco = personagens.jonh.precisao / 2
    henryarredondado = round(henryprecisamaluco)
    yuriarredondado = round(yuriprecisamaluco)
    johnarredondado = round(johnprecisamaluco) 
    numeros = list(range(1, 20))
    porcetagemdeesquivvahenry = list(range(1, henryarredondado))
    porcetagemdeesquivvayuri = list(range(1, yuriarredondado))
    porcetagemdeesquivvajohn = list(range(1, johnarredondado))
    numeroescolhido = random.choice(numeros)

#DEFESA DOS PERSONAGENS 
    defesahenry = personagens.henry.res+50
    defesayuri = personagens.yuri.res+50
    defesajohn = personagens.jonh.res+50
#DANO DOS PERSONAGENS
    #DANO DO BOT   
    danocaverna1cima = inimigos.homemdascavernas1.forca*50
    danocaverna2cima = inimigos.homemdascavernas2.forca*50
    danocaverna3cima = inimigos.homemdascavernas3.forca*50

    #DANO TOTAL CAUSADO PELO BOT HENRY
    danototalHcaverna1= danocaverna1cima/defesahenry
    danototalHcaverna2 = danocaverna2cima/defesahenry
    danototalHcaverna3 = danocaverna3cima/defesahenry

    #DANO TOTAL CAUSADO PELO BOT JOHN
    danototalJcaverna1= danocaverna1cima/defesajohn
    danototalJcaverna2 = danocaverna2cima/defesajohn
    danototalJcaverna3 = danocaverna3cima/defesajohn

    #DANO TOTAL CAUSADO PELO BOT YURI
    danototalYcaverna1= danocaverna1cima/defesayuri
    danototalYcaverna2 = danocaverna2cima/defesayuri
    danototalYcaverna3 = danocaverna3cima/defesayuri
#FUNCAO DO ATAQUE    
    qtsvivos = len(personagensvivos)
    if qtsvivos >= 1:
        if ordemdecrescente[0] == "Caverna1":
            escolhido = random.choice(personagensvivos)
            if escolhido == "John":
                if personagens.jonh.hp > 0:
                    if numeroescolhido not in porcetagemdeesquivvajohn:
                        personagens.jonh.hp = personagens.jonh.hp - danototalJcaverna1
                    if numeroescolhido in porcetagemdeesquivvajohn:
                        print("John desviou!")
                
            if escolhido == "Henry":
                if personagens.henry.hp > 0: 
                    if numeroescolhido not in porcetagemdeesquivvahenry:
                        personagens.henry.hp = personagens.henry.hp - danototalHcaverna1
                    if numeroescolhido in porcetagemdeesquivvahenry:
                        print("Henry desviou!")
                        
            
            if escolhido == "Yuri":
                if personagens.yuri.hp > 0:    
                    if numeroescolhido not in porcetagemdeesquivvayuri:
                        personagens.yuri.hp = personagens.yuri.hp - danototalYcaverna1                    
                    if numeroescolhido in porcetagemdeesquivvayuri:
                        print("Yuri Desviou")
        
        if ordemdecrescente[0] == "Caverna2":
            escolhido = random.choice(personagensvivos)
            
            if escolhido == "John":
                if personagens.jonh.hp > 0:
                    if numeroescolhido not in porcetagemdeesquivvajohn:
                        personagens.jonh.hp = personagens.jonh.hp - danototalJcaverna2
                    if numeroescolhido in porcetagemdeesquivvajohn:
                        print("John desviou!")
            
            if escolhido == "Henry":
                if personagens.henry.hp > 0:   
                    if numeroescolhido not in porcetagemdeesquivvahenry:
                        personagens.henry.hp = personagens.henry.hp - danototalHcaverna2
                    if numeroescolhido in porcetagemdeesquivvahenry:
                        print("Henry desviou")
            
            if escolhido == "Yuri":
                if personagens.yuri.hp > 0:    
                    if numeroescolhido not in porcetagemdeesquivvayuri:
                        personagens.yuri.hp = personagens.yuri.hp - danototalYcaverna2                   
                    if numeroescolhido in porcetagemdeesquivvayuri:
                        print("Yuri Desviou")
        
        if ordemdecrescente[0] == "Caverna3":
            escolhido = random.choice(personagensvivos)
            
            if escolhido == "John":
                if personagens.jonh.hp > 0:
                    if numeroescolhido not in porcetagemdeesquivvajohn:
                        personagens.jonh.hp = personagens.jonh.hp - danototalJcaverna3
                    if numeroescolhido in porcetagemdeesquivvajohn:
                        print("John desviou!")
            
            if escolhido == "Henry":
                if personagens.henry.hp > 0:   
                    if numeroescolhido not in porcetagemdeesquivvahenry:
                        personagens.henry.hp = personagens.henry.hp - danototalHcaverna3
                    if numeroescolhido in porcetagemdeesquivvahenry:
                        print("Henry desviou")
            
            if escolhido == "Yuri":
                if personagens.yuri.hp > 0:    
                    if numeroescolhido not in porcetagemdeesquivvayuri:
                        personagens.yuri.hp = personagens.yuri.hp - danototalYcaverna3                    
                    if numeroescolhido in porcetagemdeesquivvayuri:
                        print("Yuri Desviou")

#TESTE PARA VER SE TODOS OS PERSONAGENS ESTÃO MORTOS, SE ESTIVEM O JOGO VOLTA REINICIA
def mortinhodasilva():        
    qtsvivos = len(personagensvivos)
    if personagens.henry.hp <= 0:
        if "Henry" in personagensvivos:
            personagensvivos.remove("Henry")
        if "Henry" in ordemdecrescente:
            ordemdecrescente.remove("Henry")
    if personagens.jonh.hp <= 0:
        if "John" in personagensvivos:
            personagensvivos.remove("John")
        if "John" in ordemdecrescente:
            ordemdecrescente.remove("John") 
    if personagens.yuri.hp <= 0:
        if "Yuri" in personagensvivos:
            personagensvivos.remove("Yuri")
        if "Yuri" in ordemdecrescente:
            ordemdecrescente.remove("Yuri")
    if inimigos.homemdascavernas1.hp <= 0:
        if "Caverna1" in inimigosvivos:
            inimigosvivos.remove("Caverna1")
        if "Caverna1" in ordemdecrescente:
            ordemdecrescente.remove("Caverna1")
    if inimigos.homemdascavernas2.hp <= 0:
        if "Caverna2" in inimigosvivos:
            inimigosvivos.remove("Caverna2")
        if "Caverna2" in ordemdecrescente:
            ordemdecrescente.remove("Caverna2")
    if inimigos.homemdascavernas3.hp <= 0:
        if "Caverna3" in inimigosvivos:
            inimigosvivos.remove("Caverna3")
        if "Caverna3" in ordemdecrescente:
            ordemdecrescente.remove("Caverna3")                

def vitoria():
    pygame.mixer.music.stop()
    teladevitoria = True
    while teladevitoria:
        
        clock.tick(30)
        janeladogame.fill((cores["preto"]))
        creditos = pygame.image.load('imagens/creditos.png')
        janeladogame.blit(creditos,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    pygame.quit()
def derrota():
    pygame.mixer.music.stop()
    teladederrota = True
    while teladederrota:

        clock.tick(30)
        janeladogame.fill((cores["preto"]))
        perdemo = pygame.image.load("imagens/perdemo.png")
        janeladogame.blit(perdemo,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    gameplay()
def teclas():
    creditos_running = True
    while creditos_running:
        clock.tick(30)
        janeladogame.fill((cores["preto"]))
        teclas1 = pygame.image.load("imagens/MENUteclas.png")
        teclas1 = pygame.transform.scale(teclas1,(1024,768))
        janeladogame.blit(teclas1,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == pygame.QUIT:
                creditos_running = False
                pygame.quit()


#BARRA DE VIDA DOS ALIADOS
bdvjohn = barradevida(180, 325, personagens.jonh.hp, personagens.jonh.maxhp)
bdvyuri = barradevida(280, 225, personagens.yuri.hp, personagens.yuri.maxhp)
bdvhenry = barradevida(280, 425, personagens.jonh.hp, personagens.jonh.maxhp)

#BARRA DE VIDA DOS INIMIGOS
bdvcaverna1 = barradevida(700, 425, inimigos.homemdascavernas1.hp, inimigos.homemdascavernas1.maxhp)
bdvcaverna2 = barradevida(600, 325, inimigos.homemdascavernas2.hp, inimigos.homemdascavernas2.maxhp)
bdvcaverna3 = barradevida(700, 225, inimigos.homemdascavernas3.hp, inimigos.homemdascavernas3.maxhp)


#FUNÇÃO DO AUDIO
ooflist = []
def audio():  
    mortosound = mixer.Sound('audio/morto.wav')    

#SOM DE MORTE
    if inimigos.homemdascavernas1.hp <= 0:
        if 4 in ooflist:
            mortosound.play()            
            ooflist.remove(4)
    if inimigos.homemdascavernas2.hp <= 0:
        if 5 in ooflist:
            mortosound.play()            
            ooflist.remove(5)
    if inimigos.homemdascavernas3.hp <= 0:
        if 6 in ooflist:
            mortosound.play()            
            ooflist.remove(6)
    if personagens.yuri.hp <= 0:
        if 3 in ooflist:
            mortosound.play()
            ooflist.remove(3)
    if personagens.jonh.hp <= 0:
        if 2 in ooflist:
            mortosound.play()
            ooflist.remove(2)
    if personagens.henry.hp <= 0:
        if 1 in ooflist:
            mortosound.play()
            ooflist.remove(1)   
    

#MUSICA MENU
def musicamenu():
    pygame.mixer.music.load('audio/menusong.wav')
    pygame.mixer.music.play(-1)

musicamenu()



#FUNÇÕES QUE VÃO SER OS MENUS/GAMEPLAY
def cutscene():
    scenes = [pygame.image.load("imagens/cutscenes/cutscene00.png"),pygame.image.load("imagens/cutscenes/cutscene01.png"),pygame.image.load("imagens/cutscenes/cutscene02.png"),pygame.image.load("imagens/cutscenes/cutscene03.png"),pygame.image.load("imagens/cutscenes/cutscene04.png"),pygame.image.load("imagens/cutscenes/cutscene05.png"),pygame.image.load("imagens/cutscenes/cutscene06.png"),pygame.image.load("imagens/cutscenes/cutscene07.png"),pygame.image.load("imagens/cutscenes/cutscene08.png"),pygame.image.load("imagens/cutscenes/cutscene09.png"),pygame.image.load("imagens/cutscenes/cutscene10.png"),pygame.image.load("imagens/cutscenes/cutscene11.png")]
    cutscenerunning =  True
    while cutscenerunning:
        quantasfaltam = len(scenes)       
        janeladogame.fill((0,0,0))
        cutatual = scenes[0]
        cutatual = pygame.transform.scale(cutatual,(1024,768))
        janeladogame.blit(cutatual,(0,0))
        if quantasfaltam > 1:
            desenhar_texto("Aperte Z para continuar...", fonts3, cores["preto"],500,40)
        if quantasfaltam == 1:
            desenhar_texto("Aperte Z para começar a batalha...", fonts2, cores["preto"],350,450)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cutscenerunning = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_z:
                    if quantasfaltam > 1:
                        del scenes[0]
                    if quantasfaltam == 1:
                        gameplay()
                        cutscenerunning = False

def main_menu():
    main_menu_running = True
    teclaatual = 0

    #INTRODUÇÃO DO LOOP
    while main_menu_running:
        janeladogame.fill((cores["preto"]))
        clock.tick(30)
    
    #TEXTOS E IMAGENS   
        imgplayselecionada = pygame.image.load('imagens/fundo/MENUstartselec.png')
        imgsairselecionada = pygame.image.load('imagens/fundo/MENUsairselec.png')
        imgteclassselecionada = pygame.image.load('imagens/fundo/MENUteclasselec.png')
        planodefundomenu = pygame.image.load('imagens/fundo/MENUstart.png')
        planodefundomenu = pygame.transform.scale(planodefundomenu,(1024,768))
        imgplayselecionada = pygame.transform.scale(imgplayselecionada,(296,100))
        imgsairselecionada = pygame.transform.scale(imgsairselecionada,(296,100))
        imgteclassselecionada = pygame.transform.scale(imgteclassselecionada,(296,100))
        
        janeladogame.blit(planodefundomenu,(0,0))

        if teclaatual == 0:
            janeladogame.blit(imgplayselecionada,(364, 288))
        if teclaatual == 1:
            janeladogame.blit(imgteclassselecionada,(364, 440))
        if teclaatual == 2:
            janeladogame.blit(imgsairselecionada,(364,592))


        
        pygame.display.update()
    
    #EVENTOS 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu_running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    teclaatual = teclaatual +1
                    if teclaatual > 2:
                        teclaatual = teclaatual - 1
                if event.key == K_UP:
                    teclaatual = teclaatual - 1
                    if teclaatual < 0:
                        teclaatual = teclaatual + 1
                if teclaatual == 0:
                    if event.key == K_z:
                        main_menu_running = False
                        caracterbuild()
                if teclaatual == 2:
                    if event.key == K_z:
                        main_menu_running = False
                        pygame.quit()
                if teclaatual == 1:
                    if event.key == K_z:
                        main_menu_running = False
                        teclas()
def caracterbuild(): 
     
    caracterbuilding = True
    janeladogame.fill((0,0,0))
    pygame.display.update()
    
    
    primeiralinha = 28
    segundalinha = 208
    terceiralinha = 396
    quartalinha = 588
    quintalinha = 776
    sextalinha = 948
    ys = 352
    
    movimentohorizontal = 1   


    




    while caracterbuilding:        
        
#versao numero dos atributos
        henryforca = int(personagens.henry.forca)
        henryres = int(personagens.henry.res)
        henrycar = int(personagens.henry.carisma)
        henryagi = int(personagens.henry.agility)
        henrypres = int(personagens.henry.precisao)
        
        johnforca = int(personagens.jonh.forca)
        johnres = int(personagens.jonh.res)
        johncar = int(personagens.jonh.carisma)
        johnagi = int(personagens.jonh.agility)
        johnpres = int(personagens.jonh.precisao)

        yuriforca = int(personagens.yuri.forca)
        yurires = int(personagens.yuri.res)
        yuricar = int(personagens.yuri.carisma)
        yuriagi = int(personagens.yuri.agility)
        yuripres = int(personagens.yuri.precisao)

        henrypontos = int(personagens.henry.pontosliberados)
        johnpontos = int(personagens.jonh.pontosliberados)
        yuripontos = int(personagens.yuri.pontosliberados)
        
        
#Display        
        pos = pygame.mouse.get_pos()
        parasairdatelademontagem = personagens.yuri.pontosliberados + personagens.jonh.pontosliberados + personagens.henry.pontosliberados
        pygame.display.update()        
#DESENHO DOS BOTOES    
        botoesfoto = pygame.image.load('imagens/saveselector.png')
        botoesfoto = pygame.transform.scale(botoesfoto,(1024,768))

        if movimentohorizontal == 1:
            xs = primeiralinha
        if movimentohorizontal == 2:
            xs = segundalinha
        if movimentohorizontal == 3:
            xs = terceiralinha
        if movimentohorizontal == 4:
            xs = quartalinha
        if movimentohorizontal == 5:
            xs = quintalinha
        if movimentohorizontal == 6:
            xs = sextalinha

        diminuir = [28, 776, 396]
        aumentar = [208, 588, 948]
        if xs in diminuir:
            botaomarcardos = pygame.image.load("imagens/-.png")
            botaomarcardos = pygame.transform.scale(botaomarcardos,(48,48))
        if xs in aumentar:
            botaomarcardos = pygame.image.load('imagens/+.png')
            botaomarcardos = pygame.transform.scale(botaomarcardos,(48,48))

        janeladogame.fill((0,0,0))
        if parasairdatelademontagem == 0:
            desenhar_texto("Aperte Enter para continuar", fonts1, cores["branco"], 300, 0)
        janeladogame.blit(botoesfoto,(0,0))
        janeladogame.blit(botaomarcardos,(xs,ys))   
        desenhar_texto(f'FORÇA:{henryforca}', fonts2, cores["preto"], 100, 360)   
        desenhar_texto(f'FORÇA:{johnforca}', fonts2, cores["preto"], 480, 360)            
        desenhar_texto(f'FORÇA:{yuriforca}', fonts2, cores["preto"], 840, 360)    
        desenhar_texto(f'PRECISÃO:{henrypres}', fonts2, cores["preto"],90, 432)
        desenhar_texto(f'PRECISÃO:{johnpres}', fonts2, cores["preto"],460, 432)   
        desenhar_texto(f'PRECISÃO:{yuripres}', fonts2, cores["preto"],830, 432)     
        desenhar_texto(f'CARISMA:{henrycar}', fonts2, cores["preto"],90, 500)
        desenhar_texto(f'CARISMA:{johncar}', fonts2, cores["preto"],460, 500)   
        desenhar_texto(f'CARISMA:{yuricar}', fonts2, cores["preto"],830, 500) 
        desenhar_texto(f'DEFESA:{henryres}', fonts2, cores["preto"],90, 570)
        desenhar_texto(f'DEFESA:{johnres}', fonts2, cores["preto"],470, 570)   
        desenhar_texto(f'DEFESA:{yurires}', fonts2, cores["preto"],840, 570) 
        desenhar_texto(f'AGILIDADE:{henryagi}', fonts2, cores["preto"],80, 640)
        desenhar_texto(f'AGILIDADE:{johnagi}', fonts2, cores["preto"],460, 640)   
        desenhar_texto(f'AGILIDADE:{yuriagi}', fonts2, cores["preto"],830, 640) 
        desenhar_texto(f'PONTOS LIBERADOS:{henrypontos}', fonts2, cores["preto"], 60, 290)      
        desenhar_texto(f'PONTOS LIBERADOS:{johnpontos}', fonts2, cores["preto"], 420, 290)  
        desenhar_texto(f'PONTOS LIBERADOS:{yuripontos}', fonts2, cores["preto"], 780, 290)    
        if parasairdatelademontagem == 0:
            desenhar_texto(f'APERTER "ENTER" PARA INICIAR O JOGO', fonts3, cores["vermelho"], 180, 720)



#EVENTOS DO MENU DE CUSTOMIZAÇÃO
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                caracterbuilding = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ys = ys + 68
                    if ys > 668:
                        ys = ys - 68
                if event.key == pygame.K_UP:
                    ys = ys - 68
                    if ys < 352:
                        ys = ys + 68
                if event.key == pygame.K_RIGHT:
                    movimentohorizontal = movimentohorizontal + 1
                    if movimentohorizontal > 6:
                        movimentohorizontal = movimentohorizontal -1
                if event.key == pygame.K_LEFT:
                    movimentohorizontal = movimentohorizontal - 1
                    if movimentohorizontal < 1:
                        movimentohorizontal = movimentohorizontal + 1
                if event.key == pygame.K_ESCAPE:
                    caracterbuilding = False
                    main_menu()
                if parasairdatelademontagem == 0:
                    if event.key == pygame.K_RETURN:
                        caracterbuilding = False
                        pygame.mixer.music.stop()
                        cutscene()

    #USO DA CONSTRUCAO DE PERSONAGENS
            #HENRY CONSTRUCTION    
                if event.key == pygame.K_z:
                    if xs == primeiralinha:
                        if ys == 352:
                            if personagens.henry.forca > 0:
                                personagens.henry.forca-=1
                                personagens.henry.pontosliberados+=1
                                print("henry")
                    if xs == primeiralinha:
                        if ys == 420:
                            if personagens.henry.precisao > 0:
                                personagens.henry.precisao-=1                           
                                personagens.henry.pontosliberados+=1
                    if xs == primeiralinha:
                        if ys == 488:
                            if personagens.henry.carisma > 0:  
                                personagens.henry.carisma-=1
                                personagens.henry.pontosliberados+=1
                    if xs == primeiralinha:
                        if ys == 556:
                            if personagens.henry.res > 0:
                                personagens.henry.res-=1
                                personagens.henry.pontosliberados+=1
                    if xs == primeiralinha:
                        if ys == 624:
                            if personagens.henry.agility > 0:
                                personagens.henry.agility-=1
                                personagens.henry.pontosliberados+=1
                    if xs == segundalinha:
                        if ys == 352:
                            if personagens.henry.pontosliberados > 0:
                                personagens.henry.forca+=1
                                personagens.henry.pontosliberados-=1
                    if xs == segundalinha:
                        if ys == 420:    
                            if personagens.henry.pontosliberados > 0:
                                personagens.henry.precisao+=1  
                                personagens.henry.pontosliberados-=1                         
                    if xs == segundalinha:
                        if ys == 488:
                            if personagens.henry.pontosliberados > 0:  
                                personagens.henry.carisma+=1
                                personagens.henry.pontosliberados-=1
                    if xs == segundalinha:
                        if ys == 556:    
                            if personagens.henry.pontosliberados > 0:
                                personagens.henry.res+=1
                                personagens.henry.pontosliberados-=1
                    if xs == segundalinha:
                        if ys == 624:    
                            if personagens.henry.pontosliberados > 0:
                                personagens.henry.agility+=1
                                personagens.henry.pontosliberados-=1    
                                print(personagens.henry.agility)
            #JOHN CONSTRUCTION
                    if xs == terceiralinha:
                        if ys == 352:
                            if personagens.jonh.forca > 0:
                                personagens.jonh.forca-=1
                                personagens.jonh.pontosliberados+=1
                                print("john")
                    if xs == terceiralinha:
                        if ys == 420:    
                            if personagens.jonh.precisao > 0:
                                personagens.jonh.precisao-=1                           
                                personagens.jonh.pontosliberados+=1
                    if xs == terceiralinha:
                        if ys == 488:                     
                            if personagens.jonh.carisma > 0:  
                                personagens.jonh.carisma-=1
                                personagens.jonh.pontosliberados+=1
                    if xs == terceiralinha:
                        if ys == 556:                     
                            if personagens.jonh.res > 0:
                                personagens.jonh.res-=1
                                personagens.jonh.pontosliberados+=1
                    if xs == terceiralinha:
                        if ys == 624:                     
                            if personagens.jonh.agility > 0:
                                personagens.jonh.agility-=1
                                personagens.jonh.pontosliberados+=1
                    if xs == quartalinha:
                        if ys == 352:                     
                            if personagens.jonh.pontosliberados > 0:
                                personagens.jonh.forca+=1
                                personagens.jonh.pontosliberados-=1
                    if xs == quartalinha:
                        if ys == 420:                     
                            if personagens.jonh.pontosliberados > 0:
                                personagens.jonh.precisao+=1
                                personagens.jonh.pontosliberados-=1                           
                    if xs == quartalinha:
                        if ys == 488:                     
                            if personagens.jonh.pontosliberados > 0:  
                                personagens.jonh.carisma+=1
                                personagens.jonh.pontosliberados-=1
                    if xs == quartalinha:
                        if ys == 556:                     
                            if personagens.jonh.pontosliberados > 0:
                                personagens.jonh.res+=1
                                personagens.jonh.pontosliberados-=1
                    if xs == quartalinha:
                        if ys == 624:                     
                            if personagens.jonh.pontosliberados > 0:
                                personagens.jonh.agility+=1
                                personagens.jonh.pontosliberados-=1
                                print(personagens.jonh.agility)
            #YURI CONSTRUCTION
                    if xs == quintalinha:
                        if ys == 352: 
                            if personagens.yuri.forca > 0:
                                personagens.yuri.forca-=1
                                personagens.yuri.pontosliberados+=1
                                print("yuri")
                    if xs == quintalinha:
                        if ys == 420:
                            if personagens.yuri.precisao > 0:
                                personagens.yuri.precisao-=1
                                personagens.yuri.pontosliberados+=1                           
                    if xs == quintalinha:
                        if ys == 488:                        
                            if personagens.yuri.carisma > 0:  
                                personagens.yuri.carisma-=1
                                personagens.yuri.pontosliberados+=1
                    if xs == quintalinha:
                        if ys == 556:                            
                            if personagens.yuri.res > 0:
                                personagens.yuri.res-=1
                                personagens.yuri.pontosliberados+=1
                    if xs == quintalinha:
                        if ys == 624:
                            if personagens.yuri.agility > 0:
                                personagens.yuri.agility-=1
                                personagens.yuri.pontosliberados+=1
                    if xs == sextalinha:
                        if ys == 352:
                            if personagens.yuri.pontosliberados>0:
                                personagens.yuri.forca+=1
                                personagens.yuri.pontosliberados-=1
                    if xs == sextalinha:
                        if ys == 420:
                            if personagens.yuri.pontosliberados>0:
                                personagens.yuri.precisao+=1
                                personagens.yuri.pontosliberados-=1                          
                    if xs == sextalinha:
                        if ys == 488:
                            if personagens.yuri.pontosliberados>0:  
                                personagens.yuri.carisma+=1
                                personagens.yuri.pontosliberados-=1
                    if xs == sextalinha:
                        if ys == 556:
                            if personagens.yuri.pontosliberados>0:
                                personagens.yuri.res+=1
                                personagens.yuri.pontosliberados-=1
                    if xs == sextalinha:
                        if ys == 624:
                            if personagens.yuri.pontosliberados > 0:
                                personagens.yuri.agility+=1
                                personagens.yuri.pontosliberados-=1
                                print(personagens.yuri.agility) 

#LISTA ORDENADA
ordemdecrescente = []
primeiralista = []


def gameplay():
    henrydefendendo = 0
    johndefendendo = 0
    yuridefendendo = 0
    marcadorx = 0
    marcadory = 0
    sinalizadorspritecount = 0
    planodefundocounter = 0
    spritescount = 0
    derrotacount = 0

#SONS
    tirosound1 = mixer.Sound('audio/tiro1.wav')
    tirosound2 = mixer.Sound('audio/tiro2.wav')
    tirosound3 = mixer.Sound('audio/tiro3.wav')

    escudosound = mixer.Sound('audio/escudo.wav')

    pocaosound = mixer.Sound('audio/pocao.wav')

    bonk = mixer.Sound('audio/bonk.wav')
#MUSICA
    pygame.mixer.music.load('audio/battlesong1.wav')
    pygame.mixer.music.play(-1)

#DANO DOS PROTAGONISTAS
    
    #DEFESAS
    defesacaverna = 55
    
    #DANO DO HENRY 
    danohenrycima = personagens.henry.forca * 50
    #DANO JOHN
    danojohncima = personagens.jonh.forca * 50
    #DANO YURI
    danoyuricima = personagens.yuri.forca * 50
            
    #DANO CAUSADO PELOS PERSONAGENS PRINCIPAIS
    danototalhenry = danohenrycima/defesacaverna
    danototaljohn = danojohncima/defesacaverna
    danototalyuri = danoyuricima/defesacaverna
#DICIONARIO 
    ordem = {
        "Caverna1": (inimigos.homemdascavernas1.agility),
        "Caverna2":(inimigos.homemdascavernas2.agility),
        "Caverna3":(inimigos.homemdascavernas3.agility),
        "Henry": (personagens.henry.agility),
        "John": (personagens.jonh.agility),
        "Yuri": (personagens.yuri.agility)
    }
#ORDENA
    quantidadedeespeciais = 1
    ordemdecrescente.clear()
    primeiralista.clear()
    for i in sorted(ordem, key = ordem.get, reverse=True):
        primeiralista.append(i)  
    pygame.display.update()
#ATUALIZA A VIDA DOS PERSONAGENS CASO O JOGO SEJA REINICIADO(SE TODOS FICA COM A VIDA >= 0)   
    ordemdecrescente.clear()
    ordemdecrescente.extend(primeiralista)
    personagensvivos.append("Yuri")
    personagensvivos.append("John")
    personagensvivos.append("Henry")
    inimigosvivos.append('Caverna1')
    inimigosvivos.append('Caverna2')
    inimigosvivos.append('Caverna3')
    personagens.henry.hp = 100
    personagens.jonh.hp = 100
    personagens.yuri.hp = 100
    inimigos.homemdascavernas1.hp = 90
    inimigos.homemdascavernas2.hp = 90
    inimigos.homemdascavernas3.hp = 90
    ooflist.clear()
    ooflist.append(1)
    ooflist.append(2)
    ooflist.append(3)
    ooflist.append(4)
    ooflist.append(5)
    ooflist.append(6)
#CONFIGURAÇÕES DURANTE A GAMEPLAY
    gameplay_running = True
    mx2 = 730
    my2 = 425
    x2 = 20
    y2 = 610
    ix = 100
    iy = 130
    pocoes = 3
    cura = 25
    count = 0
    atacar = 0
    selecionando = True
    selecionandoitens = False
    selecionandoalvo = False
#DADOS DOS SPRITES
    yuriatacando = False
    henryatacando = False
    johnatacando = False
    
    
    
    planodefundo = [pygame.image.load("imagens/fundo/planodefundo0.png"),pygame.image.load("imagens/fundo/planodefundo1.png"),pygame.image.load("imagens/fundo/planodefundo2.png"),pygame.image.load("imagens/fundo/planodefundo3.png"),]
    sinalizador = [pygame.image.load("imagens/sinalizador/sinalizador-1.png"), pygame.image.load("imagens/sinalizador/sinalizador-2.png")]


#ANIMAÇOES DO HENRY
    henryidle = [pygame.image.load("imagens/henry/henryidle0.png"),pygame.image.load("imagens/henry/henryidle0.png"),pygame.image.load("imagens/henry/henryidle0.png"),pygame.image.load("imagens/henry/henryidle0.png"),pygame.image.load("imagens/henry/henryidle1.png"),pygame.image.load("imagens/henry/henryidle1.png"),pygame.image.load("imagens/henry/henryidle1.png"),pygame.image.load("imagens/henry/henryidle1.png")]
    henryatackani = [pygame.image.load('imagens/henry/Hatack0.png'),pygame.image.load('imagens/henry/Hatack1.png'),pygame.image.load('imagens/henry/Hatack2.png'),pygame.image.load('imagens/henry/Hatack3.png'),pygame.image.load('imagens/henry/Hatack4.png'),pygame.image.load('imagens/henry/Hatack5.png'),pygame.image.load('imagens/henry/Hatack6.png'),pygame.image.load('imagens/henry/Hatack7.png')]
    henrydesmaiado = [pygame.image.load('imagens/henry/henrycaido0.png'),pygame.image.load('imagens/henry/henrycaido0.png'),pygame.image.load('imagens/henry/henrycaido1.png'),pygame.image.load('imagens/henry/henrycaido1.png'),pygame.image.load('imagens/henry/henrycaido2.png'),pygame.image.load('imagens/henry/henrycaido2.png'),pygame.image.load('imagens/henry/henrycaido3.png'),pygame.image.load('imagens/henry/henrycaido3.png')]
    henrydefesa = [pygame.image.load('imagens/henry/henrydefendendo0.png'),pygame.image.load('imagens/henry/henrydefendendo0.png'),pygame.image.load('imagens/henry/henrydefendendo0.png'),pygame.image.load('imagens/henry/henrydefendendo0.png'),pygame.image.load('imagens/henry/henrydefendendo1.png'),pygame.image.load('imagens/henry/henrydefendendo1.png'),pygame.image.load('imagens/henry/henrydefendendo1.png'),pygame.image.load('imagens/henry/henrydefendendo1.png')]
    henryatual = henryidle
#ANIMAÇOES DO JOHN
    johnidle = [pygame.image.load("imagens/john/johnidle0.png"),pygame.image.load("imagens/john/johnidle0.png"),pygame.image.load("imagens/john/johnidle0.png"),pygame.image.load("imagens/john/johnidle0.png"),pygame.image.load("imagens/john/johnidle1.png"),pygame.image.load("imagens/john/johnidle1.png"),pygame.image.load("imagens/john/johnidle1.png"),pygame.image.load("imagens/john/johnidle1.png")]
    johnatackani = [pygame.image.load('imagens/john/Jatack0.png'),pygame.image.load('imagens/john/Jatack1.png'),pygame.image.load('imagens/john/Jatack2.png'),pygame.image.load('imagens/john/Jatack3.png'),pygame.image.load('imagens/john/Jatack4.png'),pygame.image.load('imagens/john/Jatack5.png'),pygame.image.load('imagens/john/Jatack6.png'),pygame.image.load('imagens/john/Jatack7.png')]
    johndesmaiado = [pygame.image.load('imagens/john/johncaido0.png'),pygame.image.load('imagens/john/johncaido0.png'),pygame.image.load('imagens/john/johncaido1.png'),pygame.image.load('imagens/john/johncaido1.png'),pygame.image.load('imagens/john/johncaido2.png'),pygame.image.load('imagens/john/johncaido2.png'),pygame.image.load('imagens/john/johncaido3.png'),pygame.image.load('imagens/john/johncaido3.png')]
    johndefesa = [pygame.image.load('imagens/john/johndefendendo0.png'),pygame.image.load('imagens/john/johndefendendo0.png'),pygame.image.load('imagens/john/johndefendendo0.png'),pygame.image.load('imagens/john/johndefendendo0.png'),pygame.image.load('imagens/john/johndefendendo1.png'),pygame.image.load('imagens/john/johndefendendo1.png'),pygame.image.load('imagens/john/johndefendendo1.png'),pygame.image.load('imagens/john/johndefendendo1.png')]
    johnatual = johnidle
#ANIMAÇOES DO YURI
    yuriidle = [pygame.image.load("imagens/yuri/yuriidle0.png"),pygame.image.load("imagens/yuri/yuriidle0.png"),pygame.image.load("imagens/yuri/yuriidle0.png"),pygame.image.load("imagens/yuri/yuriidle0.png"),pygame.image.load("imagens/yuri/yuriidle1.png"),pygame.image.load("imagens/yuri/yuriidle1.png"),pygame.image.load("imagens/yuri/yuriidle1.png"),pygame.image.load("imagens/yuri/yuriidle1.png")]
    yuriatackani = [pygame.image.load('imagens/yuri/Yatack0.png'),pygame.image.load('imagens/yuri/Yatack1.png'),pygame.image.load('imagens/yuri/Yatack2.png'),pygame.image.load('imagens/yuri/Yatack3.png'),pygame.image.load('imagens/yuri/Yatack4.png'),pygame.image.load('imagens/yuri/Yatack5.png'),pygame.image.load('imagens/yuri/Yatack6.png'),pygame.image.load('imagens/yuri/Yatack7.png')]
    yuridesmaiado = [pygame.image.load('imagens/yuri/yuricaido0.png'),pygame.image.load('imagens/yuri/yuricaido0.png'),pygame.image.load('imagens/yuri/yuricaido1.png'),pygame.image.load('imagens/yuri/yuricaido1.png'),pygame.image.load('imagens/yuri/yuricaido2.png'),pygame.image.load('imagens/yuri/yuricaido2.png'),pygame.image.load('imagens/yuri/yuricaido3.png'),pygame.image.load('imagens/yuri/yuricaido3.png')]
    yuridefesa = [pygame.image.load('imagens/yuri/yuridefendendo0.png'),pygame.image.load('imagens/yuri/yuridefendendo0.png'),pygame.image.load('imagens/yuri/yuridefendendo0.png'),pygame.image.load('imagens/yuri/yuridefendendo0.png'),pygame.image.load('imagens/yuri/yuridefendendo1.png'),pygame.image.load('imagens/yuri/yuridefendendo1.png'),pygame.image.load('imagens/yuri/yuridefendendo1.png'),pygame.image.load('imagens/yuri/yuridefendendo1.png')]
    yuriatual = yuriidle

#ANIMACOES HDC 1
    hdc1idle = [pygame.image.load("imagens/caverna1/hcidle0.png"),pygame.image.load("imagens/caverna1/hcidle0.png"),pygame.image.load("imagens/caverna1/hcidle0.png"),pygame.image.load("imagens/caverna1/hcidle0.png"),pygame.image.load("imagens/caverna1/hcidle1.png"),pygame.image.load("imagens/caverna1/hcidle1.png"),pygame.image.load("imagens/caverna1/hcidle1.png"),pygame.image.load("imagens/caverna1/hcidle1.png")]
    hdc1atack = [pygame.image.load("imagens/caverna1/hc1a0.png"),pygame.image.load("imagens/caverna1/hc1a0.png"),pygame.image.load("imagens/caverna1/hc1a1.png"),pygame.image.load("imagens/caverna1/hc1a1.png"),pygame.image.load("imagens/caverna1/hc1a1.png"),pygame.image.load("imagens/caverna1/hc1a1.png"),pygame.image.load("imagens/caverna1/hc1a2.png"),pygame.image.load("imagens/caverna1/hc1a2.png")]
    hdc1morto = [pygame.image.load("imagens/caverna1/hc1morto0.png"),pygame.image.load("imagens/caverna1/hc1morto0.png")]
    hdc1atual = hdc1idle
#ANIMACOES HDC 2
    hdc2idle = [pygame.image.load("imagens/caverna2/hc2idle0.png"),pygame.image.load("imagens/caverna2/hc2idle0.png"),pygame.image.load("imagens/caverna2/hc2idle0.png"),pygame.image.load("imagens/caverna2/hc2idle0.png"),pygame.image.load("imagens/caverna2/hc2idle1.png"),pygame.image.load("imagens/caverna2/hc2idle1.png"),pygame.image.load("imagens/caverna2/hc2idle1.png"),pygame.image.load("imagens/caverna2/hc2idle1.png")]
    hdc2atack = [pygame.image.load("imagens/caverna2/hc2a0.png"),pygame.image.load("imagens/caverna2/hc2a0.png"),pygame.image.load("imagens/caverna2/hc2a1.png"),pygame.image.load("imagens/caverna2/hc2a1.png"),pygame.image.load("imagens/caverna2/hc2a1.png"),pygame.image.load("imagens/caverna2/hc2a1.png"),pygame.image.load("imagens/caverna2/hc2a2.png"),pygame.image.load("imagens/caverna2/hc2a2.png")]
    hdc2morto = [pygame.image.load("imagens/caverna2/hc2morto0.png"),pygame.image.load("imagens/caverna2/hc2morto0.png")]
    hdc2atual = hdc2idle
#ANIMACOES HDC 3
    hdc3idle = [pygame.image.load("imagens/caverna3/hc3idle0.png"),pygame.image.load("imagens/caverna3/hc3idle0.png"),pygame.image.load("imagens/caverna3/hc3idle0.png"),pygame.image.load("imagens/caverna3/hc3idle0.png"),pygame.image.load("imagens/caverna3/hc3idle1.png"),pygame.image.load("imagens/caverna3/hc3idle1.png"),pygame.image.load("imagens/caverna3/hc3idle1.png"),pygame.image.load("imagens/caverna3/hc3idle1.png")]
    hdc3atack = [pygame.image.load("imagens/caverna3/hc3a0.png"),pygame.image.load("imagens/caverna3/hc3a0.png"),pygame.image.load("imagens/caverna3/hc3a1.png"),pygame.image.load("imagens/caverna3/hc3a1.png"),pygame.image.load("imagens/caverna3/hc3a1.png"),pygame.image.load("imagens/caverna3/hc3a1.png"),pygame.image.load("imagens/caverna3/hc3a2.png"),pygame.image.load("imagens/caverna3/hc3a2.png")]
    hdc3morto = [pygame.image.load("imagens/caverna3/hc3morto0.png"),pygame.image.load("imagens/caverna3/hc3morto0.png")]
    hdc3atual = hdc3idle
#LOOP DA GAMEPLAY
    while gameplay_running:


        
        qtsvivos = len(personagensvivos)
        if len(inimigosvivos) == 0:
            if count == 60:
                vitoria()
                gameplay_running = False
        if qtsvivos == 0:
            derrotacount+=1
            if derrotacount == 60:
                derrota()
                gameplay_running = False
        mortinhodasilva()
        audio()
        paraoespecial = personagens.henry.hp + personagens.jonh.hp + personagens.yuri.hp
        if henrydefendendo == 3:
            personagens.henry.res = personagens.henry.res / 2
            henrydefendendo = 1
        if henrydefendendo == 2:
            if ordemdecrescente[0] == "Henry":
                henrydefendendo = 3
            if personagens.henry.hp <= 0:
                henrydefendendo = 1
                personagens.henry.res = personagens.henry.res / 2
        
        if yuridefendendo == 3:
            personagens.yuri.res = personagens.yuri.res / 2
            yuridefendendo = 1
        if yuridefendendo == 2:
            if ordemdecrescente[0] == "Yuri":
                yuridefendendo = 3
            if personagens.yuri.hp <= 0:
                yuridefendendo = 1
                personagens.yuri.res = personagens.yuri.res / 2
        
        if johndefendendo == 3:
            personagens.jonh.res = personagens.jonh.res / 2
            johndefendendo = 1
        if johndefendendo == 2:
            if ordemdecrescente[0] == "John":
                johndefendendo = 3
            if personagens.jonh.hp <= 0:
                johndefendendo = 1
                personagens.jonh.res = personagens.jonh.res /2
        
        pygame.display.update()
        primeiro_a_atacar = ordemdecrescente[0]
        clock.tick(30) 
        count += 1
        janeladogame.fill((cores["preto"]))
#CONFIG DO MARCADOR DE QUE VAI ATACAR
        if primeiro_a_atacar == "Henry":
            marcadorx = 320
            marcadory = 400
        if primeiro_a_atacar == "John":
            marcadorx = 220
            marcadory = 300
        if primeiro_a_atacar == "Yuri":
            marcadorx = 320
            marcadory = 200
        if primeiro_a_atacar == "Caverna1":
            marcadorx = 730
            marcadory = 400
        if primeiro_a_atacar == "Caverna2":
            marcadorx = 630
            marcadory = 300
        if primeiro_a_atacar == "Caverna3":
            marcadorx = 730
            marcadory = 200


#SPRITES E MENU DA GAMEPLAY
        
        if iy == 130:
            marcadoritens = pygame.image.load('imagens/seta.png')    
        else:
            marcadoritens = pygame.image.load('imagens/cura.png')
        
        
        marcadoritens = pygame.transform.scale(marcadoritens,(50,50))
        marcadorhit = pygame.image.load('imagens/mira.png')
        marcadorhit = pygame.transform.scale(marcadorhit,(50,50))
        
        
        
        pocaosprite = pygame.image.load("imagens/pocao1.png")
        pocaosprite = pygame.transform.scale(pocaosprite,(70,70))
        barraitens = pygame.image.load("imagens/barrapocao.png")
        barraitens = pygame.transform.scale(barraitens,(100,480))
        
        
        
        background = pygame.transform.scale(planodefundo[0],(1024,768))


#ANIMACOES
        if henryatacando == True:
            henryatual = henryatackani
        if personagens.henry.hp <= 0:
            henryatual = henrydesmaiado
        if henrydefendendo == 2:
            henryatual = henrydefesa
        if henryatacando == False:
            if henrydefendendo != 2:
                if personagens.henry.hp > 0:
                    henryatual = henryidle
        
        if johnatacando == True:
            johnatual = johnatackani
        if personagens.jonh.hp <= 0:
            johnatual = johndesmaiado
        if johndefendendo == 2:
            johnatual = johndefesa
        if johnatacando == False:
            if johndefendendo != 2:
                if personagens.jonh.hp > 0:
                    johnatual = johnidle

        if yuriatacando == True:
            yuriatual = yuriatackani
        if personagens.yuri.hp <= 0:
            yuriatual = yuridesmaiado
        if yuridefendendo == 2:
            yuriatual = yuridefesa
        if yuriatacando == False:
            if yuridefendendo != 2:
                if personagens.yuri.hp > 0:
                    yuriatual = yuriidle


        if inimigos.homemdascavernas1.hp <= 0:
            hdc1atual = hdc1morto
        if inimigos.homemdascavernas2.hp <= 0:
            hdc2atual = hdc2morto
        if inimigos.homemdascavernas3.hp <= 0:
            hdc3atual = hdc3morto

        
  
        
#DESIGN DOS MENUS E O FUNDO       
        planodefundocounter = planodefundocounter + 1
        if planodefundocounter == 20:
            fundoremovido = planodefundo.pop(0)
            planodefundo.append(fundoremovido)
            planodefundocounter = 0
        janeladogame.blit(background,(0,0))
        
        atacarselecionado = pygame.image.load('imagens/atacarmenuselecionado.png')
        defenderselecionado = pygame.image.load('imagens/defendermenuselecionado.png')
        itensselecionado = pygame.image.load('imagens/itensmenuselecionado.png')



        
        if x2 == 20:
            if y2 == 610:
                botaomarcador = atacarselecionado
            if y2 == 686:
                botaomarcador = itensselecionado
        if x2 == 236:
            if y2 == 610:
                botaomarcador = defenderselecionado
            if y2 == 686:
                botaomarcador = especialselecionado
        
        


        botaomarcador = pygame.transform.scale(botaomarcador,(196,64))
        




        if paraoespecial < 100:
            if quantidadedeespeciais > 0:   
                barragameplay = pygame.image.load('imagens/barramenubraba.png')
                especialselecionado = pygame.image.load('imagens/especialmenuselecionado.png')
                botaomarcador = pygame.transform.scale(botaomarcador,(196,64))


        if paraoespecial > 100:
            barragameplay = pygame.image.load('imagens/barramenubraba1.png')
            especialselecionado = pygame.image.load('imagens/especialmenuselecionado1.png')
            
        if quantidadedeespeciais <= 0:
            barragameplay = pygame.image.load('imagens/barramenubraba1.png')
            especialselecionado = pygame.image.load('imagens/especialmenuselecionado1.png')


        barragameplay = pygame.transform.scale(barragameplay,(452,180))
        janeladogame.blit(barragameplay,(0,590))   
        
        henryanim = henryatual[0]
        henryanim = pygame.transform.scale(henryanim,(100,100))
        
        johnanim = johnatual[0]
        johnanim = pygame.transform.scale(johnanim,(100,100))
        
        yurianim = yuriatual[0]
        yurianim = pygame.transform.scale(yurianim,(100,100))

        hdc1anim = hdc1atual[0]
        hdc1anim = pygame.transform.scale(hdc1anim,(100,100))

        hdc2anim = hdc2atual[0]
        hdc2anim = pygame.transform.scale(hdc2anim,(100,100))

        hdc3anim = hdc3atual[0]
        hdc3anim = pygame.transform.scale(hdc3anim,(100,100))

        janeladogame.blit(henryanim,(300,450))
        janeladogame.blit(johnanim,(200,350))
        janeladogame.blit(yurianim,(300,250))
        janeladogame.blit(hdc1anim,(700,450))
        janeladogame.blit(hdc2anim,(600,350))
        janeladogame.blit(hdc3anim,(700,250))

        
        bdvhenry.montagembarradevida(personagens.henry.hp)
        bdvjohn.montagembarradevida(personagens.jonh.hp)
        bdvyuri.montagembarradevida(personagens.yuri.hp)
        bdvcaverna1.montagembarradevida(inimigos.homemdascavernas1.hp)
        bdvcaverna2.montagembarradevida(inimigos.homemdascavernas2.hp)
        bdvcaverna3.montagembarradevida(inimigos.homemdascavernas3.hp)
        
        borda = pygame.image.load('imagens/borda.png')
        janeladogame.blit(borda,(180, 325))
        janeladogame.blit(borda,(280, 225))
        janeladogame.blit(borda,(280, 425))
        janeladogame.blit(borda,(700,225))
        janeladogame.blit(borda,(700,425))
        janeladogame.blit(borda,(600,325))

        
        
        
        if selecionando == True:
            janeladogame.blit(botaomarcador,(x2,y2))
        if selecionandoalvo == True:
            janeladogame.blit(marcadorhit,(mx2,my2))
        if selecionandoitens == True:
            janeladogame.blit(barraitens,(0,100))
            janeladogame.blit(pocaosprite,(15,120))
            janeladogame.blit(marcadoritens,(ix,iy))
            desenhar_texto(f'{pocoes}', fonts2, cores["preto"],45, 160)
#THE TRUE SPRITES MONSTROS
        janeladogame.blit(sinalizador[0],(marcadorx,marcadory))
        sinalizadorspritecount+=1
        if sinalizadorspritecount == 10:
            sprinteremovido = sinalizador.pop(0)
            sinalizador.append(sprinteremovido)
            sinalizadorspritecount = 0
        spritescount+=1
        if spritescount == 5:
            spritescount = 0            
            
            henryremovido = henryatual.pop(0)
            henryatual.append(henryremovido)
            
            johnremovido = johnatual.pop(0)
            johnatual.append(johnremovido)

            yuriremovido = yuriatual.pop(0)
            yuriatual.append(yuriremovido)

            hdc1removido = hdc1atual.pop(0)
            hdc1atual.append(hdc1removido)

            hdc2removido = hdc2atual.pop(0)
            hdc2atual.append(hdc2removido)

            hdc3removido = hdc3atual.pop(0)
            hdc3atual.append(hdc3removido)
        


#CONFIG DO ATAQUE DO INIMIGO   
        if primeiro_a_atacar == ('Caverna1'):
            hdc1atual = hdc1atack
            selecionando = False
            if count == 25:
                bonk.play()
            if count == 40:
                AIdosBots()
                ultimoatacante = ordemdecrescente.pop(0)
                ordemdecrescente.append(ultimoatacante)
                count = 0
                hdc1atual = hdc1idle
                selecionando = True
        if primeiro_a_atacar == ('Caverna2'):
            hdc2atual = hdc2atack
            selecionando = False
            if count == 25:
                bonk.play()
            if count == 40:
                AIdosBots() 
                ultimoatacante = ordemdecrescente.pop(0)
                ordemdecrescente.append(ultimoatacante)
                count = 0
                hdc2atual = hdc2idle
                selecionando = True
        if primeiro_a_atacar == ('Caverna3'):
            hdc3atual = hdc3atack
            selecionando = False
            if count == 25:
                bonk.play()
            if count == 40:
                AIdosBots() 
                ultimoatacante = ordemdecrescente.pop(0)
                ordemdecrescente.append(ultimoatacante)
                count = 0
                hdc3atual = hdc3idle
                selecionando = True
#EVENTOS DA GAMEPLAY
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_z:
                    print(ordemdecrescente)
                if selecionando == True:
                    if event.key == K_DOWN:
                        y2 = y2 + 76
                        if y2 > 690:
                            y2 = y2 - 76
                    if event.key == K_UP:
                        y2 = y2 - 76
                        if y2 < 610:
                            y2 = y2 + 76
                    if event.key == K_LEFT:
                        x2 = x2 - 216
                        if x2 < 20:
                            x2 = x2 + 216
                    if event.key == K_RIGHT:
                        x2 = x2 + 216
                        if x2 > 240:
                            x2 = x2 - 216
                    if event.key == K_ESCAPE:
                        gameplay_running = False
                        pygame.mixer.music.stop()
                        musicamenu()
                        main_menu()

                    
                
                    if event.key == K_z:
                        if x2 == 20:
                            if y2 == 610:
                                selecionandoalvo = True
                                selecionando = False
                                count = 0
                            if y2 == 686:
                                count = 0
                                selecionandoitens = True
                                selecionando =False
       
#PROGRAMANDO DEFESA  
                        if x2 == 236:
                            if y2 == 610:
                                if primeiro_a_atacar in personagensvivos:        
                                    if primeiro_a_atacar == "Yuri":
                                        if count >= 5:
                                            yuridefendendo = 1
                                            if yuridefendendo == 1:
                                                personagens.yuri.res = personagens.yuri.res * 2 
                                                escudosound.play()
                                                yuridefendendo = 2                                              
                                                print(personagens.yuri.res)
                                                ultimoatacante = ordemdecrescente.pop(0)          
                                                if personagens.yuri.hp > 0:
                                                    ordemdecrescente.append(ultimoatacante)  
                                                count = 0                               

                                    if primeiro_a_atacar == "Henry":  
                                        if count >= 5:
                                            henrydefendendo = 1
                                            if henrydefendendo == 1:
                                                personagens.henry.res = personagens.henry.res * 2
                                                escudosound.play()                                                
                                                henrydefendendo = 2                                                
                                                print(personagens.henry.res)
                                                ultimoatacante = ordemdecrescente.pop(0)
                                                if personagens.henry.hp > 0:
                                                    ordemdecrescente.append(ultimoatacante)                                              
                                                count = 0
                                    
                                    if primeiro_a_atacar == "John":
                                        if count >= 5:
                                            johndefendendo = 1
                                            if johndefendendo == 1:    
                                                personagens.jonh.res = personagens.jonh.res * 2
                                                escudosound.play()                                                
                                                johndefendendo = 2
                                                print(personagens.jonh.res)
                                                ultimoatacante = ordemdecrescente.pop(0)
                                                if personagens.jonh.hp > 0:
                                                    ordemdecrescente.append(ultimoatacante)                                                                                  
                                                count = 0
                                    

#CONFIGURANDO O "ESPECIAL"
                            if y2 == 686:
                                if paraoespecial < 100:
                                    if quantidadedeespeciais > 0:
                                        ultimoatacante = ordemdecrescente.pop(0)
                                        ordemdecrescente.append(ultimoatacante)                                              
                                        if count > 5:
                                            inimigos.homemdascavernas1.hp = inimigos.homemdascavernas1.hp - 40
                                            inimigos.homemdascavernas2.hp = inimigos.homemdascavernas2.hp - 40
                                            inimigos.homemdascavernas3.hp = inimigos.homemdascavernas3.hp - 40
                                            quantidadedeespeciais = quantidadedeespeciais - 1
                                            count = 0


#SAIR DO EVENTO DA BARRA DE ITENS
                if selecionandoitens == True:
                    if event.key == K_x:
                        selecionandoitens = False
                        selecionando = True
                        ix = 100
                        iy = 130
#FAZER O TECLADO SE MOVER ENTRE OS INIMIGOS
                if selecionandoalvo == True:
                    if event.key == K_UP:
                        my2 = my2 - 100
                        if my2 < 225:
                            my2 = my2 + 100
                    if event.key == K_DOWN:
                        my2 = my2 + 100
                        if my2 > 425:
                            my2 = my2 - 100
                    if my2 == 325:
                        mx2 = 630
                    if my2 != 325:
                        mx2 = 730
                    if event.key == K_x:
                        my2 = 425
                        selecionandoalvo = False
                        selecionando = True

#SITUACAO DE VITORIA E GAMEOVER                   
                    if primeiro_a_atacar == "Henry":
                        if personagens.henry.hp <= 0:
                            ordemdecrescente.remove("Henry")
                    if primeiro_a_atacar == "John":
                        if personagens.jonh.hp <= 0:
                            ordemdecrescente.remove("John")
                    if primeiro_a_atacar == "Yuri":
                        if personagens.yuri.hp <= 0:
                            ordemdecrescente.remove("Yuri")
                    if primeiro_a_atacar == "Caverna1":
                        if inimigos.homemdascavernas1.hp <= 0:
                            ordemdecrescente.remove("Caverna1")
                    if primeiro_a_atacar == "Caverna2":
                        if inimigos.homemdascavernas2.hp <= 0:
                            ordemdecrescente.remove("Caverna2")
                    if primeiro_a_atacar == "Caverna3":
                        if inimigos.homemdascavernas3.hp <= 0:
                            ordemdecrescente.remove("Caverna3")
#ATAQUE DOS ALIADOS                                           
                    if primeiro_a_atacar in personagensvivos:   
                        if primeiro_a_atacar == "Henry":
                            if count >= 5:    
                                if event.key == K_z:
                                    henryatacando = True
                                    count = 0


                        if primeiro_a_atacar == "John":
                            if count >= 5:    
                                if event.key == K_z:
                                    johnatacando = True
                                    count = 0
                                

                        if primeiro_a_atacar == "Yuri":
                            if count >= 5:    
                                if event.key == K_z:
                                    yuriatacando = True
                                    count = 0
#CONFIGURANDO OS ITENS(POCAO)             
                if selecionandoitens == True:
                    if count >= 5:
                        if iy == 130:
                            if event.key == K_z:
                                count = 0
                                ix = 320
                                iy = 450
                    if count >= 5:
                        if iy != 130:  
                            if event.key == K_DOWN:
                                iy = iy + 100
                                if iy > 450:
                                    iy = iy - 100
                            if event.key == K_UP:
                                iy = iy - 100
                                if iy < 250:
                                    iy = iy + 100
                            if iy == 350:
                                ix = 220
                            if iy != 350:
                                ix = 320
                            if count > 5:
                                if iy == 450:
                                    if event.key == K_z:
                                        if pocoes > 0:
                                            if personagens.henry.hp < 100:
                                                if personagens.henry.hp > 0:   
                                                    pocaosound.play()
                                                    pocoes = pocoes - 1
                                                    personagens.henry.hp = personagens.henry.hp + cura
                                                    ultimoatacante = ordemdecrescente.pop(0)
                                                    ordemdecrescente.append(ultimoatacante)
                                                    selecionando = True
                                                    selecionandoitens = False
                                                    count = 0
                                                    iy = 130
                                                    ix = 100
                                                    if personagens.henry.hp > 100:
                                                        personagens.henry.hp = 100                                            
                                        else:
                                            print("Acabou suas poções")
                                if iy == 350:
                                    if event.key == K_z:
                                        if pocoes > 0:
                                            if personagens.jonh.hp < 100:    
                                                if personagens.jonh.hp > 0:    
                                                    pocaosound.play()
                                                    pocoes = pocoes - 1
                                                    personagens.jonh.hp = personagens.jonh.hp + cura
                                                    ultimoatacante = ordemdecrescente.pop(0)
                                                    ordemdecrescente.append(ultimoatacante)                                    
                                                    selecionando = True
                                                    selecionandoitens = False   
                                                    count = 0
                                                    iy = 130
                                                    ix = 100                                                   
                                                    if personagens.jonh.hp > 100:
                                                        personagens.jonh.hp = 100                           
                                        else:
                                            print("Acabou suas poções")
                                if iy == 250:
                                    if event.key == K_z:
                                        if pocoes > 0:
                                            if personagens.yuri.hp < 100:
                                                if personagens.yuri.hp > 0:
                                                    pocaosound.play()                                                    
                                                    pocoes = pocoes - 1
                                                    personagens.yuri.hp = personagens.yuri.hp + cura
                                                    ultimoatacante = ordemdecrescente.pop(0)
                                                    ordemdecrescente.append(ultimoatacante)                                    
                                                    selecionando = True
                                                    selecionandoitens = False       
                                                    iy = 130
                                                    ix = 100                                                   
                                                    if personagens.yuri.hp > 100:
                                                        personagens.yuri.hp = 100
                                            count = 0                             
                                        else:
                                            print("Acabou suas poções")
#TIMING DOS ATAQUES                       
        if henryatacando == True:  
                if my2 == 425:  
                    if inimigos.homemdascavernas1.hp > 0:   
                        selecionandoalvo = False
                        if count == 5:
                            tirosound1.play()
                        if count == 40:
                            inimigos.homemdascavernas1.hp = inimigos.homemdascavernas1.hp - danototalhenry
                            ultimoatacante = ordemdecrescente.pop(0)
                            ordemdecrescente.append(ultimoatacante)
                            count = 0
                            henryatacando = False
                            selecionando = True
                    else:
                        print("Esse inimigo já está morto!")
                        henryatacando = False
                        selecionando = True
                        selecionandoalvo = False  
                if my2 == 325:  
                    if inimigos.homemdascavernas2.hp > 0:   
                        selecionandoalvo = False                        
                        if count == 5:
                            tirosound1.play()
                        if count == 40:
                            inimigos.homemdascavernas2.hp = inimigos.homemdascavernas2.hp - danototalhenry
                            ultimoatacante = ordemdecrescente.pop(0)
                            ordemdecrescente.append(ultimoatacante)
                            count = 0
                            henryatacando = False
                            selecionando = True
                    else:
                        print("Esse inimigo já está morto!") 
                        henryatacando = False
                        selecionando = True
                        selecionandoalvo = False                        
                if my2 == 225:  
                    if inimigos.homemdascavernas3.hp > 0:   
                        selecionandoalvo = False                        
                        if count == 5:
                            tirosound1.play()
                        if count == 40:
                            inimigos.homemdascavernas3.hp = inimigos.homemdascavernas3.hp - danototalhenry
                            ultimoatacante = ordemdecrescente.pop(0)
                            ordemdecrescente.append(ultimoatacante)
                            count = 0
                            henryatacando = False
                            selecionando = True
                    else:
                        print("Esse inimigo já está morto!")
                        henryatacando = False
                        selecionando = True
                        selecionandoalvo = False
        
        if johnatacando == True:
            if my2 == 425:  
                if inimigos.homemdascavernas1.hp > 0:   
                    selecionandoalvo = False     
                    if count == 5:
                        tirosound2.play()
                    if count == 40:
                        inimigos.homemdascavernas1.hp = inimigos.homemdascavernas1.hp - danototaljohn
                        ultimoatacante = ordemdecrescente.pop(0)
                        ordemdecrescente.append(ultimoatacante)
                        count = 0
                        johnatacando = False
                        selecionando = True
                else:
                    print("Esse inimigo já está morto!")
                    johnatacando = False
                    selecionando = True
                    selecionandoalvo = False                     
 
            if my2 == 325:  
                if inimigos.homemdascavernas2.hp > 0:   
                    selecionandoalvo = False
                    if count == 5:
                        tirosound2.play()
                    if count == 40:
                        inimigos.homemdascavernas2.hp = inimigos.homemdascavernas2.hp - danototaljohn
                        ultimoatacante = ordemdecrescente.pop(0)
                        ordemdecrescente.append(ultimoatacante)
                        count = 0
                        johnatacando = False
                        selecionando = True
                else:
                    print("Esse inimigo já está morto!")
                    johnatacando = False
                    selecionando = True
                    selecionandoalvo = False                    
            if my2 == 225:  
                if inimigos.homemdascavernas3.hp > 0: 
                    selecionandoalvo = False
                    if count == 5:
                        tirosound2.play()
                    if count == 40:
                        inimigos.homemdascavernas3.hp = inimigos.homemdascavernas3.hp - danototaljohn
                        ultimoatacante = ordemdecrescente.pop(0)
                        ordemdecrescente.append(ultimoatacante)
                        count = 0
                        johnatacando = False
                        selecionando = True
                else:
                    print("Esse inimigo já está morto!")
                    johnatacando = False
                    selecionando = True
                    selecionandoalvo = False
            
        if yuriatacando == True:
            if my2 == 425:  
                if inimigos.homemdascavernas1.hp > 0:   
                    selecionandoalvo = False
                    if count == 15:
                        tirosound3.play()
                    if count == 40:
                        inimigos.homemdascavernas1.hp = inimigos.homemdascavernas1.hp - danototalyuri
                        ultimoatacante = ordemdecrescente.pop(0)
                        ordemdecrescente.append(ultimoatacante)
                        count = 0
                        yuriatacando = False
                        selecionando = True
                else:
                    print("Esse inimigo já está morto!")
                    yuriatacando = False
                    selecionando = True
                    selecionandoalvo = False                    

            if my2 == 325:  
                if inimigos.homemdascavernas2.hp > 0:   
                    selecionandoalvo = False                    
                    if count == 15:
                        tirosound3.play()
                    if count == 40:
                        inimigos.homemdascavernas2.hp = inimigos.homemdascavernas2.hp - danototalyuri
                        ultimoatacante = ordemdecrescente.pop(0)
                        ordemdecrescente.append(ultimoatacante)
                        count = 0
                        yuriatacando = False
                        selecionando = True
                else:
                    print("Esse inimigo já está morto!")  
                    yuriatacando = False
                    selecionando = True
                    selecionandoalvo = False
            if my2 == 225:  
                if inimigos.homemdascavernas3.hp > 0:   
                    selecionandoalvo = False                                        
                    if count == 15:
                        tirosound3.play()
                    if count == 40:
                        inimigos.homemdascavernas3.hp = inimigos.homemdascavernas3.hp - danototalyuri
                        ultimoatacante = ordemdecrescente.pop(0)
                        ordemdecrescente.append(ultimoatacante)
                        count = 0
                        yuriatacando = False
                        selecionando = True
                else:
                    print("Esse inimigo já está morto!")
                    yuriatacando = False
                    selecionando = True
                    selecionandoalvo = False







while running:
    main_menu()




