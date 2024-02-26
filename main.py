import pyautogui as bot
from time import sleep
from os import system
import webbrowser

def seg2():
    while True:
        posicao = bot.locateOnScreen('follow.png', confidence=0.7,) 
        
        if posicao is not None:
            x, y = bot.center(posicao)  
            bot.click(x, y)
            sleep(2)
            seg3()
        else:
            x, y = 885, 554
            bot.moveTo(x, y)
            for _ in range(5):
                bot.scroll(50)
                sleep(2)
            seg2()

def seg3():
    while True:
        posicao = bot.locateOnScreen('follow.png', confidence=0.7,) 
        
        if posicao is not None:
            x, y = bot.center(posicao) 
            bot.click(x, y)
            sleep(2)
            seg2()
        else:
            x, y = 885, 554
            bot.moveTo(x, y)
            for _ in range(5):
                bot.scroll(50)
                sleep(2)
            seg2()

def seg1():
    urlperf = input("digite a url do perfil: ")
    webbrowser.open(urlperf + "following/")
    sleep(5)
    seg2()
    
def questionmensage():
    urlperfmensage = input("Digite o perfil que deseja enviar mensagem: ")
    quantmsg = int(input("Digite a quantidade de mensagens que deseja enviar: "))
    mensage = input("Qual mensagem você deseja enviar? ")   
    webbrowser.open("https://www.instagram.com/" + urlperfmensage)
    sleep(5)
    posicao = bot.locateOnScreen('msg.png', confidence=0.9,) 
    posicao2 = bot.locateOnScreen('follow.png', confidence=0.9,)

    if posicao:
        x, y = bot.center(posicao)  
        bot.click(x, y)
        sleep(5)
        for _ in range(quantmsg):
            bot.write(mensage, interval=0.2)
            bot.press('enter')
            sleep(1)
    else:
        xy = bot.center(posicao2)  
        bot.click(xy)
        sleep(3)
        x, y = bot.center(posicao)  
        bot.click(x, y)
        sleep(5)
        for _ in range(quantmsg):
            bot.write(mensage, interval=0.2)
            bot.press('enter')
            sleep(1)

def comentario():
    linkfoto = input("cole a url da foto que deseja comentar: ")
    qntdcomentario = int(input("digite a quantidade de comentários: "))
    msgcomentario = input("digite oque deseja comentar: ")
    webbrowser.open(linkfoto)
    sleep(5)
    posicao = bot.locateOnScreen('comentario.png', confidence=0.9,)
    if posicao:
        x, y = bot.center(posicao)  
        bot.click(x, y)
        sleep(5)
        for _ in range(qntdcomentario):
            bot.write(msgcomentario, interval=0.5)
            bot.press('enter')
            sleep(3)


def menu():
    print('''
    [1] - spam de seguidores
    [2] - spam de comentarios
    [3] - spam de mensagem 
    [4] - sair do sistemas
    ''')
    op = int(input(":"))
    if op == 1:
        system("cls")
        seg1()
    elif op == 2:
        system("cls")
        comentario()
    elif op == 3:
        system("cls")
        questionmensage()
    elif op == 4:
        exit
    else:
        print("opção invalida!")
        system("cls")
        menu()

def load():
    print("Iniciando o aplicativo aguarde...")
    sleep(2)
    system("cls")
    print("#")
    sleep(1)
    system("cls")
    print("##")
    sleep(1)
    system("cls")
    print("###")
    sleep(1)
    system("cls")
    print("####")
    sleep(1)
    system("cls")
    print("#####")
    sleep(1)
    system("cls")
    menu()
menu()

