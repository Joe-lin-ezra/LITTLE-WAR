import pygame
import time
import random
import glob
import json
import sqlite3
import numpy as np
from network import Network
import pygame_textinput
import Player ##by Dan
import Constructer ##by Dan
import Commander ##by Dan
import os.path     #By Chin
import pygame.locals as pl #By Chin

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
import Constructer ##by Dan



##test  - Dan

pygame.init()
#net = Network()


display_width = 1024
display_height = 768
gameDisplay = pygame.display.set_mode((display_width, display_height))


transComman = []##紀錄指令的地方
##test-Dan

Infantry_Self = pygame.image.load('../img/Infantry-self.png')
Infantry_Self = pygame.transform.scale(Infantry_Self,(45,45))

Infantry_Enemy = pygame.image.load('../img/Infantry-enmy.png')
Infantry_Enemy = pygame.transform.scale(Infantry_Enemy,(45,45))

HQ = pygame.image.load("../img/HQ.png")
HQ = pygame.transform.scale(HQ,(45,45))

pygame.display.set_caption('Tanks')

Json = {
  "array": [
    {
      "ID": "",
      "Name": "",
      "win": ""
    }
  ]
}
try :
    with open("../Json/0.json") as f:
        data = json.loads(f.read())
except :
    with open("../Json/Test.json" , 'w') as file :
        data = json.dumps(Json)
        file.write(data)
    with open("../Json/Test.json") as f :
        data = json.loads(f.read())

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255,255,000)

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


def button(text, x, y, width, height, inactive_color, active_color, action=None, btncolor=black):
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
                game_controls()

            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()

            if action == "LoadingPage":
                game_loading()

            if action == "Ranking":
                game_rank()

            if action == "Home":
                game_home()

            if action == "Setting":
                game_setting()

            if action == "NewGame":
                # print("Comming Soon")
                game_newgame()

            if action == "Browse":
                return game_CreateGame(2)

            if action == "CreateGame":
                game_CreateGame(1)

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, btncolor, x, y, width, height)

def button_draw(Btn):               # Btn stands for button         Use for newgamepage (By Chin)
    # font = pygame.font.SysFont("comicsansms", 20)

    mouse = pygame.mouse.get_pos()

    if Btn['rect'].collidepoint(mouse):
        color = Btn['ac']
    else:
        color = Btn['ic']

    pygame.draw.rect(gameDisplay, color, Btn['rect'])

    image, rect = text_objects(Btn['msg'],black)
    rect.center = Btn['rect'].center
    gameDisplay.blit(image, rect)

def button_check(Btn):          #User for newgame Page (By Chin)

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


def message_to_screen(msg, color, x_displace = 0,y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(x_displace / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)



def game_user():
    run = True
    textinput = GUINewGamePageTextBox.TextInput()

    TextStyle = pygame.font.SysFont('Comic Sans MS',28)

    MsgFontSize = medfont
    IDTitle = MsgFontSize.render("ID", True, black)
    NameTitle = MsgFontSize.render("Name",True,black)
    # text_box = TextBox(350, 50, 500, 100, callback=callback)


    MSG = smallfont.render("No Any Record", True, red)
    BrowseReply = pygame.Surface((300, 100))

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
        # gameDisplay.blit(BrowseReply, (550, 500))
        button("CreateGame", 150, 300, 300, 170, red, light_red, action="CreateGame")
        button("Browse", 550, 300, 300, 170, green, light_green, action="Browse")
        pygame.display.update()
        clock.tick(15)

def game_home():
    run = True

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
        button("New Game", 450, 150, 180, 70, green, light_green, action="NewGame")
        button("Setting", 450, 250, 180, 70, red, light_red, action="Setting")
        button("Ranking", 450, 350, 180, 70, blue, light_blue, action="Ranking")

        pygame.display.update()
        clock.tick(15)


def game_rank():
    run = True

    # Server Part By Paco - Head #
    #rank_get = {'event': 4, 'player': place-1, 'ID': 2}
    #a = net.send(rank_get)
    #b = net.recv()
    #print(b)
    # Server Part By Paco - Foot#

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

        ID_txt = medfont.render("ID",True,black)
        gameDisplay.blit(ID_txt,(87,40))

        Name_txt = medfont.render("Name",True,black)
        gameDisplay.blit(Name_txt,(427,40))

        Win_txt = medfont.render("Win",True,black)
        gameDisplay.blit(Win_txt,(867,40))

        rank = json.loads(b)#player ID

        FirstI = rank["1"][0]
        FI = medfont.render(str(FirstI), True, black)
        gameDisplay.blit(FI, (87, 140))

        FirstN = rank["1"][1]
        FN = medfont.render(FirstN, True, black)
        gameDisplay.blit(FN, (427, 140))

        FirstW = rank["1"][2]
        FW = medfont.render(str(FirstW), True, black)
        gameDisplay.blit(FW, (870, 140))


        SecondI = rank["2"][0]
        SI = medfont.render(str(SecondI), True, black)
        gameDisplay.blit(SI, (87, 240))

        SecondN = rank['2'][1]
        SN = medfont.render(SecondN, True, black)
        gameDisplay.blit(SN, (427, 240))

        SecondW = rank['2'][2]
        SW = medfont.render(str(SecondW), True, black)
        gameDisplay.blit(SW, (870, 240))

        ThirdI = rank['3'][0]
        TI = medfont.render(str(ThirdI),True,black)
        gameDisplay.blit(TI,(87,340))

        ThirdN = rank['3'][1]
        TN = medfont.render(ThirdN,True,black)
        gameDisplay.blit(TN,(427,340))

        ThirdW = rank['3'][2]
        TW = medfont.render(str(ThirdW),True,black)
        gameDisplay.blit(TW,(870,340))

        line = medfont.render('------------------------------------------',True,black)
        gameDisplay.blit(line,(70,440))

        SelfI = rank['4'][0]
        SI = medfont.render(str(SelfI),True,black)
        gameDisplay.blit(SI,(87,540))

        SelfN = rank['4'][1]
        SN = medfont.render(SelfN,True,black)
        gameDisplay.blit(SN,(427,540))

        SelfW = rank['4'][2]
        SW = medfont.render(str(SelfW),True,black)
        gameDisplay.blit(SW,(870,540))

        button("Home", 60, 650, 157, 70, blue, light_blue, action="Home",btncolor=white)

        pygame.display.update()
        clock.tick(15)


def game_setting():
    run = True

    while run:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(yellow)
        # message_to_screen("Change ColorTheme",black,50,50,size="large")
        Title = largefont.render("Change Color Theme",True,green)
        gameDisplay.blit(Title,(80,70))
        button("Home", 87, 650, 180, 70, blue, light_blue, action="Home")

        pygame.display.update()
        clock.tick(15)


def game_newgame():
    intro = True
    # 都是 TextBox 的東西 By Chin - Head#
    n = 0
    y = 0
    x = 0
    myTurn = False

    # open room By Paco
    #a = net.send({'event': 1, 'player': place - 1})
    #b = net.recv() #get dic {'room': value, 'turn': value} turn = 1 is player1, = 2 player2
    #rm = json.loads(b)
    #room = rm['room']
    #if rm['room'] == 1:
    #    myTurn = True
    # open room By Paco

    textinput = GUINewGamePageTextBox.TextInput()           # 建立一個Textinput 的地方
    ResponseArea = pygame.Surface((600,150))
    ResponseArea.fill(black)
    # 都是 TextBox 的東西 By Chin - Foot#

    # 呢邊是 Button 的東西 By Chin - Head #
    SendBtn = GUINewGamePageButtonClick.button(blue,750,590,170,120,"GO")  # color , x, y, width, height , text
    token = True        # 模仿回合的結束 用來不給玩家在不是自己的回合中輸入
    Pass = False         # Pause 專用
    # 呢邊是 Button 的東西 By Chin - Foot #

    # player conn server select By Paco
    #net.send({'event': 7,'room': room,'player': place - 1})
    #player = net.recv()##1在這邊要接收 server告訴本地適用哪的玩家
    #player1 = Constructer.constructPlayer(player)
    #player1.playerID = 1  ##server give us - By Dan
    #player2 = Constructer.constructPlayer(player)
    #player2.playerID = 2  ##server give us - By Dan
    # player conn server select By Paco

    player = select.selectDeploy(1) ##1在這邊要接收 server告訴本地適用哪的玩家
    player = json.dumps(player)
    player1 = Constructer.constructPlayer(player)  ##正確建構玩家物件
    player1.playerID = 1 ##server give us - By Dan
    player2 = Constructer.constructPlayer(player)
    player2.playerID = 2  ##server give us - By Dan

    #server get map By Paco
    #net.send({'event': 5, 'player': place-1, 'room': room})
    #map = net.recv()
    #datas = eval(map)
    #map = select.constructMap(map)
    # server get map By Paco

    map = select.selectMap(2)
    map = json.dumps(map)
    datas = eval(map) ##把map轉乘Dic儲存在datas，以便設置玩家基地時用
    map = select.constructMap(map)

    player1.hq = Headquarter.Headquarter(hp=20, x=datas["Player1_HQ"]["x"], y=datas["Player1_HQ"]["y"]) ##建構玩家1物件
    player2.hq = Headquarter.Headquarter(hp=20, x=datas["Player2_HQ"]["x"], y=datas["Player2_HQ"]["y"]) ##建構玩家2物件

    head_font = smallfont  ##建立文字物件 by Dan  Changed : pygame.font.SysFont(None, 60) -> smallfont (By Chin)
    text_surface = head_font.render('illegal instruction', True, (255, 255, 255))  ##宣告文字物件的格式by Dan

    Sx = None  # Set up Army position x Default Value - By Chin
    Sy = None  # Set up Army position y Default Value - By Chin

    msg = smallfont  # 用於顯示不是目前玩家的回合
    MSG = msg.render("Not Your Turn", True, red)

    while intro:
        gameDisplay.fill(yellow)
        message_to_screen("Game Start", black, 1000, -340, size='large')
        gameDisplay.blit(ResponseArea, (80, 580))
        SendBtn.draw(gameDisplay)

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
        Reco = pygame.transform.scale(Reco,(50,50))
        gameDisplay.blit(Reco,(20,380))
        message_to_screen("Reco",navy,280,30)
        message_to_screen("> Move : 2 px",navy,180,70)
        message_to_screen("> ATK : 1 px  ",navy,180,110)

        events = pygame.event.get()
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SendBtn.isOver(pos):
                    # net.send({'event': 3, 'player': place-1, 'action': transComman})
                    TorF = winOrLose.wOrL(player2)  ##判斷對方是否輸了
                    if TorF == True:
                        print("對方輸了")
                    else:
                        print("下一回合")
                    print("TextBox Locked!")
                    # myTurn = False
                    token = False                # 還未做出下一回合, 回恢權限 By Chin
            if event.type == pygame.MOUSEMOTION:
                if SendBtn.isOver(pos):
                    SendBtn.color = (light_blue)
                else :
                    SendBtn.color = (blue)

        GUINewGamePageMap.Map(gameDisplay,map)


        if token :
            if textinput.update(events):              # 輸入指令的地方 By Chin
                n += 1
                y = 30
                command = textinput.get_text()
                print(command)  # 透過get_text() 取得輸入的資訊 By Chin
                TorF = Commander.inputCommand(player1,player2,1,command,map)##呼叫commander來解析指令 by Dan
                if TorF == True:##如果回傳值是true 就要記錄下來 by Dan
                    transComman.append(command)
                else:##指令有問題
                    print("DFG : ",player1.army[0].x, player1.army[0].y)
                    ResponseArea.blit(text_surface, (10, 30 + (y * n))) ##顯示文字物件 by Dan

        DisplayArmy(player1,player2, Sx, Sy)

        # 如不是玩家回合則顯示MSG - By Chin
        if token == False:
            gameDisplay.blit(MSG,(750,720))

        gameDisplay.blit(textinput.get_surface(), (90, 585))         # TextInput position By Chin


        if Sx and Sy:
            gameDisplay.blit(Infantry_Self, (Sx, Sy))
            # Sx = None
            # Sy = None


        # draw HQ position - By Chin
        gameDisplay.blit(HQ, (200, 360))

        # draw Infantry - Start By Chin

        # Get PlayerID , Sx , Sy
        # Run DisplayArmy()
        # draw Infantry - End By Chin

        pygame.display.update()
        clock.tick(30)




# Draw Army Function - By Chin
def DisplayArmy(Player1,Player2,Sx , Sy):                  #PlayerID Default is Player1 (Local Player)
    for i in range (len(Player1.army)):
        if Player1.army[i].x:
            Sx = 200 + Player1.army[i].x * 30
            Sy = 100 + Player1.army[i].y * 30
            gameDisplay.blit(Infantry_Self, (Sx, Sy))
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
    intro = True

    while intro:
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
        self.rect = pygame.Rect( 3,-50, 150, 198)

    def update(self):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1

def game_loading():
    # server conn By Paco
    #a = net.getP()
    #print(a)
    #global place
    #place = a['player']
    # server conn By Paco
    #pygame.init()
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
    pygame.quit()


def game_CreateGame(num):
    pygame.init()
    intro = True

    textinputName = GUINewGamePageTextBox.TextInput()           # TextBox for UserName
    textinputPw = GUINewGamePageTextBox.TextInput()             # TextBox for Set up Password
    textinputPwC = GUINewGamePageTextBox.TextInput()            # TextBox for Confirm Password
    TextArea = pygame.Surface((400, 55))
    TextArea.fill(light_gray)
    token = 0
    while intro:
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
            Name = textinputName.get_text()         # 在此取得UserName
            net.send({'event': 6, 'name': Name, 'num': num})
            print(Name)
        button("Home",350,500,300,50,orange,light_orange,action="Home")
        pygame.display.update()
        clock.tick(30)


# game_user()

# game_intro()

game_newgame()

# game_rank()

# gameLoop()

