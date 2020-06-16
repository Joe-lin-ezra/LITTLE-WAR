import pygame
import time
import random
import glob
import json
import sqlite3
import numpy as np
from network import Network
import pygame_textinput
import Player  ##by Dan
import Constructer  ##by Dan
import Commander  ##by Dan
import os.path  # By Chin
import pygame.locals as pl  # By Chin
import DeCoder
import threading

# NewGame Page 系列 - By Chin
# import GUINewGamePage
import GUINewGamePageButtonClick
import GUINewGamePageMap
import GUINewGamePageTextBox
import GUIPausePage
import winOrLose
import select
import Player
import Army
import Headquarter
import Constructer  ##by Dan

##test  - Dan
pygame.init()
net = Network()

display_width = 1024
display_height = 768
gameDisplay = pygame.display.set_mode((display_width, display_height))

transComman = []  ##紀錄指令的地方
##test-Dan

Infantry_Self = pygame.image.load('../img/Infantry-self.png')
Infantry_Self = pygame.transform.scale(Infantry_Self, (40, 40))

Infantry_Enemy = pygame.image.load('../img/Infantry-enmy.png')
Infantry_Enemy = pygame.transform.scale(Infantry_Enemy, (40, 40))

HQ = pygame.image.load("../img/HQ.png")
HQ = pygame.transform.scale(HQ, (40, 40))

pygame.display.set_caption('Tanks')

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 000)

blue = (51, 102, 255)
light_blue = (102, 153, 255)

red = (200, 0, 0)
light_red = (255, 0, 0)

green = (0, 153, 51)
light_green = (51, 204, 51)

brown = (153, 102, 51)

gray = (102, 102, 102)
light_gray = (230, 230, 230)

orange = (255, 153, 0)
light_orange = (255, 204, 0)

navy =(0, 43, 128)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

FPS = 3


# map = open("map.json",'r')

def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])


def button(text, x, y, width, height, inactive_color, active_color, action=None, btncolor=black, enable=True):
    cur = pygame.mouse.get_pos()
    # print(cur)
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                click = None
                game_controls()

            if action == "play":
                click = None
                gameLoop()

            if action == "main":
                click = None
                game_intro()

            if action == "LoadingPage":
                click = None
                game_loading()

            if action == "Ranking":
                click = None
                game_rank()
            if action == "Home":
                if enable:
                    game_home()
                else:
                    pass
                click = None

            if action == "Setting":
                click = None
                game_setting()

            if action == "NewGame":
                # print("Comming Soon")
                click = None
                game_newgame()

            if action == "Browse":
                click = None
                return game_CreateGame(2)

            if action == "CreateGame":
                click = None
                game_CreateGame(1)

            if action == 'game_user':
                click = None
                game_user()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, btncolor, x, y, width, height)


def button_draw(Btn):  # Btn stands for button         Use for newgamepage (By Chin)
    # font = pygame.font.SysFont("comicsansms", 20)

    mouse = pygame.mouse.get_pos()

    if Btn['rect'].collidepoint(mouse):
        color = Btn['ac']
    else:
        color = Btn['ic']

    pygame.draw.rect(gameDisplay, color, Btn['rect'])

    image, rect = text_objects(Btn['msg'], black)
    rect.center = Btn['rect'].center
    gameDisplay.blit(image, rect)


def button_check(Btn):  # User for newgame Page (By Chin)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if Btn['rect'].collidepoint(mouse):
        if click[0] == 1 and Btn['action']:
            print(Btn['action'])
            Btn['action']()


def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(buttonx + (buttonwidth / 2)), int(buttony) + int(buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color, x_displace=0, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(x_displace / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)

def BTN( x, y, Wt,Wb,Ht,Hb, inactive_color, active_color,action=None,enable=True):
    cur = pygame.mouse.get_pos()
    print(cur)
    # print(cur[1])
    if Wb > cur[0] > Wt and Hb > cur[1] > Ht:
        click = pygame.mouse.get_pressed()
        gameDisplay.blit(active_color,(x,y))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                click = None
                game_controls()

            if action == "play":
                click = None
                gameLoop()

            if action == "main":
                click = None
                game_intro()

            if action == "LoadingPage":
                click = None
                game_loading()

            if action == "Ranking":
                click = None
                game_rank()

            if action == "Home":
                if enable:
                    game_home()
                else:
                    pass
                click = None

            if action == "Setting":
                click = None
                game_setting()

            if action == "NewGame":
                click = None
                game_newgame()

            if action == "Browse":
                click = None
                return game_CreateGame(2)

            if action == "CreateGame":
                click = None
                game_CreateGame(1)

            if action == 'game_user':
                click = None
                game_user()
    else:
       gameDisplay.blit(inactive_color,(x,y))


def game_user():
    run = True
    textinput = GUINewGamePageTextBox.TextInput()

    TextStyle = pygame.font.SysFont('Comic Sans MS', 28)

    MsgFontSize = medfont
    IDTitle = MsgFontSize.render("ID", True, black)
    NameTitle = MsgFontSize.render("Name", True, black)
    # text_box = TextBox(350, 50, 500, 100, callback=callback)

    MSG = smallfont.render("No Any Record", True, red)
    BrowseReply = pygame.Surface((300, 100))

    CreateBtn = pygame.image.load("../img/CreateAcBtn.png")
    CreateBtn = pygame.transform.scale(CreateBtn, (500, 500))

    CreateBtn2 = pygame.image.load("../img/CreateAcBtn2.png")
    CreateBtn2 = pygame.transform.scale(CreateBtn2, (500, 500))

    UseYourBtn = pygame.image.load("../img/UseYourBtn.png")
    UseYourBtn = pygame.transform.scale(UseYourBtn, (500, 500))

    UseYourBtn2 = pygame.image.load("../img/UseYourBtn2.png")
    UseYourBtn2 = pygame.transform.scale(UseYourBtn2, (500, 500))

    while run:
        # BrowseReply.fill(black)

        events = pygame.event.get()
        for event in events:
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(yellow)
        BTN(0, 120,100,410,290,450 ,CreateBtn, CreateBtn2, action="CreateGame")
        BTN(500, 120,600,910,290,450, UseYourBtn, UseYourBtn2, action="Browse")
        pygame.display.update()
        clock.tick(15)

def game_setting():
    run = True

    HomeBtn = pygame.image.load("../img/GoBackBtn.png")
    HomeBtn = pygame.transform.scale(HomeBtn, (70,70))

    HomeBtn2 = pygame.image.load("../img/GoBackBtn2.png")
    HomeBtn2 = pygame.transform.scale(HomeBtn2, (70,70))
    while run:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(yellow)
        Title = smallfont.render("Command : [ SET , ATK , MOVE ] [Nth Army] [Xposition] [Yposition]", True, green)
        gameDisplay.blit(Title, (80, 70))
        Title2 = smallfont.render("For example : set 0 1 0",True,green)
        gameDisplay.blit(Title2,(80,110))
        Title3 = smallfont.render("Army's type is showing on left hand side",True,green)
        gameDisplay.blit(Title3,(80,200))
        BTN(6,15,6,41,15,47, HomeBtn, HomeBtn2, action="Home")

        pygame.display.update()
        clock.tick(15)

def game_home():
    run = True

    NewGameBtn = pygame.image.load("../img/NewGameBtn.png")

    NewGameBtn2 = pygame.image.load("../img/NewGameBtn2.png")

    ControlBtn = pygame.image.load("../img/ControlBtn.png")

    ControlBtn2 = pygame.image.load("../img/ControlBtn2.png")

    RankBtn = pygame.image.load("../img/RankBtn.png")

    RankBtn2 = pygame.image.load("../img/RankBtn2.png")

    BackBtn = pygame.image.load("../img/BackBtn.png")

    BackBtn2 = pygame.image.load("../img/BackBtn2.png")


    while run:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(yellow)

        BTN(-100,-150,33,470,85,320, NewGameBtn, NewGameBtn2, action="NewGame")

        BTN(415, 230,570,1000,465,700, ControlBtn, ControlBtn2, action="Setting")

        BTN(415, -150,570,1000,85,320, BackBtn, BackBtn2, action="main")

        BTN(-100, 230, 33, 470, 465, 700, RankBtn, RankBtn2, action="Ranking")

        pygame.display.update()
        clock.tick(15)

def recieve():
    print('turn on second thread')
    global myTurn
    global take
    global enemyAction
    while True:
        enemyAction = net.recv()
        enemyAction = json.loads(enemyAction)
        if enemyAction['event'] == 3:
            take = 1
            enemyAction['event'] = 1

def game_newgame():
    global myTurn
    global enemyAction
    global take
    myTurn = False
    take = 0
    # 都是 TextBox 的東西 By Chin - Head#
    n = 0
    y = 0
    x = 0

    # open room By Paco
    a = net.send({'event': 1, 'player': place - 1})
    b = net.recv()  # get dic {'room': value, 'turn': value} turn = 1 is player1, = 2 player2
    rm = json.loads(b)
    room = rm['room']
    if rm['turn'] == 1:
        myTurn = True
    # open room By Paco

    textinput = GUINewGamePageTextBox.TextInput()  # 建立一個Textinput 的地方
    ResponseArea = pygame.Surface((600, 150))
    ResponseArea.fill(black)
    # 都是 TextBox 的東西 By Chin - Foot#

    # 呢邊是 Button 的東西 By Chin - Head #
    SendBtn = GUINewGamePageButtonClick.button(blue, 750, 590, 170, 120, "GO")  # color , x, y, width, height , text
    GOBtn = pygame.image.load("../img/GoBtn.png")
    GOBtn = pygame.transform.scale(GOBtn,(320,320))

    GOBtn2 = pygame.image.load("../img/GoBtn2.png")
    GOBtn2 = pygame.transform.scale(GOBtn2,(320,320))
    token = True  # 模仿回合的結束 用來不給玩家在不是自己的回合中輸入
    Pass = False  # Pause 專用
    # 呢邊是 Button 的東西 By Chin - Foot #
    # player conn server select By Paco
    net.send({'event': 7, 'room': room, 'player': place - 1})
    player = net.recv()  ##1在這邊要接收 server告訴本地適用哪的玩家
    player1 = Constructer.constructPlayer(player)
    player1.playerID = place - 1  ##server give us - By Dan
    player2 = Constructer.constructPlayer(player)
    player2.playerID = None  ##server give us - By Dan
    # player conn server select By Paco

    # server get map By Paco
    net.send({'event': 5, 'player': place - 1, 'room': room})
    mapInfor = net.recv()
    mapInfor = json.loads(mapInfor)
    map = Constructer.constructMap(mapInfor)
    # server get map By Paco

    if rm["turn"] == 1:
        player1.hq = Headquarter.Headquarter(hp=20, x=mapInfor["Player1_HQ"]["x"],
                                             y=mapInfor["Player1_HQ"]["y"])  ##建構玩家1物件
        player2.hq = Headquarter.Headquarter(hp=20, x=mapInfor["Player2_HQ"]["x"], y=mapInfor["Player2_HQ"]["y"])
    else:
        player2.hq = Headquarter.Headquarter(hp=20, x=mapInfor["Player2_HQ"]["x"],
                                             y=mapInfor["Player2_HQ"]["y"])  ##建構玩家2物件
        player1.hq = Headquarter.Headquarter(hp=20, x=mapInfor["Player1_HQ"]["x"], y=mapInfor["Player1_HQ"]["y"])

    head_font = smallfont  ##建立文字物件 by Dan  Changed : pygame.font.SysFont(None, 60) -> smallfont (By Chin)
    text_surface = head_font.render('illegal instruction', True, (255, 255, 255))  ##宣告文字物件的格式by Dan

    Sx = None  # Set up Army position x Default Value - By Chin
    Sy = None  # Set up Army position y Default Value - By Chin

    msg = smallfont  # 用於顯示不是目前玩家的回合
    MSGColor = red
    MSG = msg.render("Not Your Turn", True, MSGColor)

    threading.Thread(target=recieve).start()
    while True:
        gameDisplay.fill(yellow)
        message_to_screen("Game Start", black, 1000, -340, size='large')
        gameDisplay.blit(ResponseArea, (80, 580))
        SendBtn.draw(gameDisplay)
        BTN(680,490,740,940,600,700,GOBtn,GOBtn2)
        # Infantry id 編號是? - By Chin #
        Infantry = pygame.image.load("../img/Infantry-self.png")
        Infantry = pygame.transform.scale(Infantry, (50, 50))
        gameDisplay.blit(Infantry, (20, 80))
        message_to_screen("Infantry", navy, 280, -290, size="small")
        message_to_screen("> Move : 3 px", navy, 180, -230)
        message_to_screen("> ATK : 1 px  ", navy, 182, -190)

        # Mech id 編號是? - By Chin #
        Mech = pygame.image.load("../img/Mech-self.png")
        Mech = pygame.transform.scale(Mech, (50, 50))
        gameDisplay.blit(Mech, (20, 230))
        message_to_screen("Mech", navy, 280, -130)
        message_to_screen("> Move : 2 px", navy, 180, -90)
        message_to_screen("> ATK : 1 px ", navy, 178, -50)

        # Reco id 編號是? - By Chin #
        Reco = pygame.image.load("../img/Reco-self.png")
        Reco = pygame.transform.scale(Reco, (50, 50))
        gameDisplay.blit(Reco, (20, 380))
        message_to_screen("Reco", navy, 280, 30)
        message_to_screen("> Move : 2 px", navy, 180, 70)
        message_to_screen("> ATK : 1 px  ", navy, 180, 110)

        GUINewGamePageMap.Map(gameDisplay, map)
        DisplayArmy(player1, player2, Sx, Sy, rm['turn'])
        gameDisplay.blit(textinput.get_surface(), (90, 585))  # TextInput position By Chin

        events = pygame.event.get()
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if PauseBtn.isOver(pos):
                #     GUIPausePage.pause()
                if SendBtn.isOver(pos) and myTurn:
                    net.send({'event': 3, 'room': room, 'player': place - 1, 'action': transComman})
                    TorF = winOrLose.wOrL(player2)  ##判斷對方是否輸了
                    if TorF == True:
                        net.send({'event': 8, 'player': place - 1, 'name': name})
                        print("對方輸了")
                    else:
                        myTurn = False
                        print("下一回合")
                        print("TextBox Locked!")

                    # token = False                # 還未做出下一回合, 回恢權限 By Chin
            if event.type == pygame.MOUSEMOTION:
                if SendBtn.isOver(pos):
                    SendBtn.color = light_blue
                else:
                    SendBtn.color = blue

        if myTurn:
            if textinput.update(events):  # 輸入指令的地方 By Chin
                n += 1
                y = 30
                command = textinput.get_text()
                # print(command)  # 透過get_text() 取得輸入的資訊 By Chin
                TorF = Commander.inputCommand(player1, player2, rm['turn'], command, map,
                                              mapInfor)  ##呼叫commander來解析指令 by Dan
                if TorF == True:  ##如果回傳值是true 就要記錄下來 by Dan
                    transComman.append(command)
                else:  ##指令有問題
                    print("DFG : ", player1.army[0].x, player1.army[0].y)
                    ResponseArea.blit(text_surface, (10, 30 + (y * n)))  ##顯示文字物件 by Dan
        else:# 如不是玩家回合則顯示MSG - By Chin
            gameDisplay.blit(MSG, (750, 720))
            if take == 1:
                print(enemyAction)
                DeCoder.deCoder(enemyAction, (rm['turn'] + 1) % 2, map, player2, player1, mapInfor)
                DisplayArmy(player1, player2, 0, 0, rm['turn'])
                print(123)
                myTurn = True
                print(456)
                take = 0


        # if Sx and Sy:
        #     gameDisplay.blit(Infantry_Self, (Sx, Sy))
        #     # Sx = None
        #     # Sy = None

        # draw HQ position - By Chin
        # gameDisplay.blit(HQ, (200, 360))

        # draw Infantry - Start By Chin

        # Get PlayerID , Sx , Sy
        # Run DisplayArmy()
        # draw Infantry - End By Chin

        pygame.display.update()
        clock.tick(30)

def game_rank():
    run = True

    # Server Part By Paco - Head #
    rank_send = {'event': 4, 'player': place - 1, 'name': name}
    net.send(rank_send)
    rank_infor = net.recv()
    # print(rank_infor)
    # Server Part By Paco - Foot#

    HomeBtn = pygame.image.load("../img/homebtn.png")
    HomeBtn = pygame.transform.scale(HomeBtn, (350, 300))

    HomeBtn2 = pygame.image.load("../img/homebtn2.png")
    HomeBtn2 = pygame.transform.scale(HomeBtn2, (350, 300))

    while run:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(yellow)

        Rank_txt = medfont.render("Rank", True, black)
        gameDisplay.blit(Rank_txt, (95, 40))

        ID_txt = medfont.render("ID", True, black)
        gameDisplay.blit(ID_txt, (280, 40))

        Name_txt = medfont.render("Name", True, black)
        gameDisplay.blit(Name_txt, (500, 40))

        Win_txt = medfont.render("Win", True, black)
        gameDisplay.blit(Win_txt, (800, 40))

        rank = json.loads(rank_infor)  # player ID

        FirstR = rank["1"][0]
        FR = medfont.render(str(FirstR), True, black)
        gameDisplay.blit(FR, (95, 140))

        FirstI = rank["1"][1]
        FI = medfont.render(str(FirstI), True, black)
        gameDisplay.blit(FI, (280, 140))

        FirstN = rank["1"][2]
        FN = medfont.render(FirstN, True, black)
        gameDisplay.blit(FN, (500, 140))

        FirstW = rank["1"][3]
        FW = medfont.render(str(FirstW), True, black)
        gameDisplay.blit(FW, (800, 140))

        SecondR = rank["2"][0]
        SR = medfont.render(str(SecondR), True, black)
        gameDisplay.blit(SR, (95, 240))

        SecondI = rank["2"][1]
        SI = medfont.render(str(SecondI), True, black)
        gameDisplay.blit(SI, (280, 240))

        SecondN = rank['2'][2]
        SN = medfont.render(SecondN, True, black)
        gameDisplay.blit(SN, (500, 240))

        SecondW = rank['2'][3]
        SW = medfont.render(str(SecondW), True, black)
        gameDisplay.blit(SW, (800, 240))

        ThirdR = rank["3"][0]
        TR = medfont.render(str(ThirdR), True, black)
        gameDisplay.blit(TR, (95, 340))

        ThirdI = rank['3'][1]
        TI = medfont.render(str(ThirdI), True, black)
        gameDisplay.blit(TI, (280, 340))

        ThirdN = rank['3'][2]
        TN = medfont.render(ThirdN, True, black)
        gameDisplay.blit(TN, (500, 340))

        ThirdW = rank['3'][3]
        TW = medfont.render(str(ThirdW), True, black)
        gameDisplay.blit(TW, (800, 340))

        line = medfont.render('------------------------------------------', True, black)
        gameDisplay.blit(line, (70, 440))

        SelfR = rank["4"][0]
        SR = medfont.render(str(SelfR), True, black)
        gameDisplay.blit(SR, (95, 540))

        SelfI = rank['4'][1]
        SI = medfont.render(str(SelfI), True, black)
        gameDisplay.blit(SI, (280, 540))

        SelfN = rank['4'][2]
        SN = medfont.render(SelfN, True, black)
        gameDisplay.blit(SN, (500, 540))

        SelfW = rank['4'][3]
        SW = medfont.render(str(SelfW), True, black)
        gameDisplay.blit(SW, (800, 540))

        BTN(0, 550,70,290,653,750, HomeBtn, HomeBtn2, action="Home")

        pygame.display.update()
        clock.tick(15)

# Draw Army Function - By Chin
def DisplayArmy(Player1, Player2, Sx, Sy, turn):  # PlayerID Default is Player1 (Local Player)

    Sx = 200 + Player1.hq.x * 40-1
    Sy = 100 + Player1.hq.y * 40-1
    gameDisplay.blit(HQ, (Sx, Sy))
    Sx = 200 + Player2.hq.x * 40
    Sy = 100 + Player2.hq.y * 40
    gameDisplay.blit(HQ, (Sx, Sy))

    for i in range(len(Player1.army)):
        if Player1.army[i].x:
            Sx = 200 + Player1.army[i].x * 40
            Sy = 100 + Player1.army[i].y * 40
            if turn == 1:
                gameDisplay.blit(Infantry_Self, (Sx, Sy))
            else:
                gameDisplay.blit(Infantry_Enemy, (Sx, Sy))
            # if Player.army[i].type == 'Infantry' :
            #     if PlayerID == 1:
            #         gameDisplay.blit(Infantry_Self,(Sx,Sy))
            #     else:
            #         gameDisplay.blit(Infantry_Enemy,(Sx,Sy))
            # elif Player.army[i].type == 'Mech' :
            #     print('Mech')
            # elif Player.army[i].type == 'Reoon' :
            #     print("Reoon")
            # elif Player.army[i].type == 'APC' :
            #     print("ACP")
            # elif Player.army[i].type == 'Artillery' :
            #     print("Artillery")
            # elif Player.army[i].type == 'Tank' :
            #     print("Tank")
            # elif Player.army[i].type == 'Rockets' :
            #     print("Rockets")
            # elif Player.army[i].type == 'Medium Tank' :
            #     print("Medium Tank")
            # elif Player.army[i].type == 'Neotank' :
            #     print("Neotank")
            # elif Player.army[i].type == 'Megatank' :
            #     print("Megatank")
    for i in range(len(Player2.army)):
        if Player2.army[i].x:
            Sx = 200 + Player2.army[i].x * 30
            Sy = 100 + Player2.army[i].y * 30
            if turn == 2:
                gameDisplay.blit(Infantry_Self, (Sx, Sy))
            else:
                gameDisplay.blit(Infantry_Enemy, (Sx, Sy))


def pause():
    paused = True
    message_to_screen("Paused", black, -100, size="large")
    message_to_screen("Press C to continue playing or Q to quit", black, 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)


def game_intro():
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(yellow)

        button("--- Click Here To Start ---", 0, 0, 1024, 768, yellow, yellow, action="LoadingPage")

        pygame.display.update()

        clock.tick(15)


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        # my_group = pygame.sprite.Group(self)
        self.images = [pygame.image.load(img) for img in glob.glob("../img/loading-*.png")]
        self.index = 0
        self.rect = pygame.Rect(3, -50, 150, 198)

    def update(self):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1


def game_loading():
    # server conn By Paco
    # try:
    playerInfor = net.getP()
    global place
    place = playerInfor['player']
    # server conn By Paco
    pygame.init()
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)

    current_time = pygame.time.get_ticks()
    exit_time = current_time + 2000

    clock = pygame.time.Clock()
    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        current_time = pygame.time.get_ticks()

        if current_time >= exit_time:
            game_user()
            # game_controls()
        #     GO TO other page

        my_group.update()
        gameDisplay.fill(yellow)
        my_group.draw(gameDisplay)
        pygame.display.update()
        clock.tick(FPS)
        pygame.time.wait(10)


# except:
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_q:
#                     pygame.quit()
#                     quit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 pygame.quit()
#                 quit()
#
#         gameDisplay.fill(yellow)
#
#         button("No connection to server. Click to leave.", 0, 0, 1024, 768, yellow, yellow)
#
#         pygame.display.update()


def game_CreateGame(num):
    pygame.init()
    print(num)
    textinputName = GUINewGamePageTextBox.TextInput()  # TextBox for UserName
    TextArea = pygame.Surface((400, 50))
    TextArea.fill((62, 71, 74))
    textColor = yellow
    textMessage = ''
    buttonColor = yellow
    buttonHoverColor = yellow
    buttonMessage = ''
    enable = False

    GoOnBtn = pygame.image.load("../img/BgColor.png")
    GoOnBtn2 = pygame.image.load("../img/BgColor.png")

    while True:
        gameDisplay.fill(yellow)

        events = pygame.event.get()
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        message_to_screen("UserName", black, 1000, -130, size='medium')
        gameDisplay.blit(TextArea, (300, 350))
        gameDisplay.blit(textinputName.get_surface(), (310, 360))
        if textinputName.update(events):
            Name = textinputName.get_text()  # 在此取得UserName
            net.send({'event': 6, 'name': Name, 'num': num, 'player': place - 1})
            result = net.recv()
            result = json.loads(result)
            if result['result']:
                GoOnBtn = pygame.image.load("../img/GoOnBtn.png")  # 使用較小的圖案按鈕取代原有Button (debug) By Chin
                GoOnBtn2 = pygame.image.load("../img/GoOnBtn2.png")
                buttonMessage = 'Success, press here to go on.'
                buttonColor = orange
                buttonHoverColor = light_orange
                textColor = yellow
                textMessage = ''
                global name
                name = Name
                enable = True
            else:
                if num == 1:
                    textMessage = 'The name is used.'
                else:
                    textMessage = 'The name is nonexistent.'
                textColor = red
                enable = False
        # button(buttonMessage, 310, 450, 380, 50, buttonColor, buttonHoverColor, action='Home', enable=enable)
        BTN(700,330,731,765,365,390,GoOnBtn,GoOnBtn2,action='Home',enable=enable)
        message_to_screen(textMessage, textColor, 1000, 95, size='medium')
        button("Back", 350, 550, 300, 50, orange, light_orange, action="game_user")
        pygame.display.update()
        clock.tick(30)


# game_user()

game_intro()

# game_newgame()

# game_home()

# gameLoop()

