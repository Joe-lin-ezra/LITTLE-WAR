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

pygame.init()

display_width = 1024
display_height = 768
n = Network()
# player = 0

# player1 = Constructer.constructPlayer(select.selectDeploy(1)) ##生成自己玩家物件
# player2 = Constructer.constructPlayer(select.selectDeploy(2)) ##生成對方玩家物件

##test  - Dan
import select
import Player
import Army
import Headquarter
import Constructer ##by Dan

player1 = Player.Player()
player2 = Player.Player()
army = Army.Army(type='Infantry', hp=10, movement=1, atk=1, atkRange=1, vision=0, x=2,y=1)
player1.army.append(army)
army = Army.Army(type='Infantry', hp=10, movement=1, atk=1, atkRange=1, vision=0, x=3,y=2)
player2.army.append(army)

player1.hq = Headquarter.Headquarter(hp=20, x=2, y=1)
player2.hq = Headquarter.Headquarter(hp=20, x=2, y=1)

transComman = []##紀錄指令的地方
##test-Dan

Infantry_Self = pygame.image.load('../img/Infantry-self.png')
Infantry_Self = pygame.transform.scale(Infantry_Self,(45,45))

Infantry_Enemy = pygame.image.load('../img/Infantry-enmy.png')
Infantry_Enemy = pygame.transform.scale(Infantry_Enemy,(45,45))

HQ = pygame.image.load("../img/HQ.png")
HQ = pygame.transform.scale(HQ,(45,45))


gameDisplay = pygame.display.set_mode((display_width, display_height))

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

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

FPS = 3

# map = open("map.json",'r')

def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])

def button(text, x, y, width, height, inactive_color, active_color, action=None, btncolor = black):
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


class TextInput:

    """
    This class lets the user input a piece of text, e.g. a name or a message.
    This class let's the user input a short, one-lines piece of text at a blinking cursor
    that can be moved using the arrow-keys. Delete, home and end work as well.
    """
    def __init__(
            self,
            initial_string="> ",
            font_family="",
            font_size=35,
            antialias=True,        #反鋸齒
            text_color=(255,255,255),
            cursor_color=(0,0,1),   #游標color
            repeat_keys_initial_ms=400,  #感應字元輸入速度
            repeat_keys_interval_ms=35,
            max_string_length=-1):
        """
        :param initial_string: Initial text to be displayed
        :param font_family: name or list of names for font (see pygame.font.match_font for precise format)
        :param font_size:  Size of font in pixels
        :param antialias: Determines if antialias is applied to font (uses more processing power)
        :param text_color: Color of text (duh)
        :param cursor_color: Color of cursor
        :param repeat_keys_initial_ms: Time in ms before keys are repeated when held
        :param repeat_keys_interval_ms: Interval between key press repetition when held
        :param max_string_length: Allowed length of text
        """

        # Text related vars:
        self.antialias = antialias
        self.text_color = text_color
        self.font_size = font_size
        self.max_string_length = max_string_length
        self.input_string = initial_string  # Inputted text

        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)

        self.font_object = pygame.font.Font(font_family, font_size)

        # Text-surface will be created during the first update call:
        self.surface = pygame.Surface((1, 1))
        self.surface.set_alpha(0)

        # Vars to make keydowns repeat after user pressed a key for some time:
        self.keyrepeat_counters = {}  # {event.key: (counter_int, event.unicode)} (look for "***")
        self.keyrepeat_intial_interval_ms = repeat_keys_initial_ms
        self.keyrepeat_interval_ms = repeat_keys_interval_ms

        # Things cursor:
        self.cursor_surface = pygame.Surface((int(self.font_size / 20 + 1), self.font_size))    # cursor 的width and height
        self.cursor_surface.fill(cursor_color)
        self.cursor_position = len(initial_string)  # Inside text
        self.cursor_visible = True  # Switches every self.cursor_switch_ms ms
        self.cursor_switch_ms = 500  # /|\
        self.cursor_ms_counter = 0

        self.clock = pygame.time.Clock()

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.cursor_visible = True  # So the user sees where he writes

                # If none exist, create counter for that key:
                if event.key not in self.keyrepeat_counters:
                    self.keyrepeat_counters[event.key] = [0, event.unicode]

                if event.key == pl.K_BACKSPACE:
                    self.input_string = (
                        self.input_string[:max(self.cursor_position - 1, 0)]
                        + self.input_string[self.cursor_position:]
                    )

                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)
                elif event.key == pl.K_DELETE:
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + self.input_string[self.cursor_position + 1:]
                    )

                elif event.key == pl.K_RETURN:
                    if self.callback is not None:
                        # print(self.input_string[2:])
                        self.input_string = "> "
                    return

                elif event.key == pl.K_RIGHT:
                    # Add one to cursor_pos, but do not exceed len(input_string)
                    self.cursor_position = min(self.cursor_position + 1, len(self.input_string))

                elif event.key == pl.K_LEFT:
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)

                elif event.key == pl.K_END:
                    self.cursor_position = len(self.input_string)

                elif event.key == pl.K_HOME:
                    self.cursor_position = 0

                elif len(self.input_string) < self.max_string_length or self.max_string_length == -1:
                    # If no special key is pressed, add unicode of key to input_string
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + event.unicode
                        + self.input_string[self.cursor_position:]
                    )
                    self.cursor_position += len(event.unicode)  # Some are empty, e.g. K_UP

            elif event.type == pl.KEYUP:
                # *** Because KEYUP doesn't include event.unicode, this dict is stored in such a weird way
                if event.key in self.keyrepeat_counters:
                    del self.keyrepeat_counters[event.key]
        # Update key counters:
        for key in self.keyrepeat_counters:
            self.keyrepeat_counters[key][0] += self.clock.get_time()  # Update clock

            # Generate new key events if enough time has passed:
            if self.keyrepeat_counters[key][0] >= self.keyrepeat_intial_interval_ms:
                self.keyrepeat_counters[key][0] = (
                    self.keyrepeat_intial_interval_ms
                    - self.keyrepeat_interval_ms
                )

                event_key, event_unicode = key, self.keyrepeat_counters[key][1]
                pygame.event.post(pygame.event.Event(pl.KEYDOWN, key=event_key, unicode=event_unicode))

        # Re-render text surface:
        self.surface = self.font_object.render(self.input_string, self.antialias, self.text_color)

        # Update self.cursor_visible
        self.cursor_ms_counter += self.clock.get_time()
        if self.cursor_ms_counter >= self.cursor_switch_ms:
            self.cursor_ms_counter %= self.cursor_switch_ms
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            cursor_y_pos = self.font_object.size(self.input_string[:self.cursor_position])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursor_position > 0:
                cursor_y_pos -= self.cursor_surface.get_width()
            self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))

        self.clock.tick()
        return False

    def get_surface(self):
        return self.surface

    def get_text(self):
        return self.input_string

    def get_cursor_position(self):
        return self.cursor_position

    def set_text_color(self, color):
        self.text_color = color

    def set_cursor_color(self, color):
        self.cursor_surface.fill(color)

    def clear_text(self):
        self.input_string = "> "
        self.cursor_position = 0

    def callback(key):
        1
        # print(key)

def game_user():
    run = True
    textinput = GUINewGamePageTextBox.TextInput()

    # text_box = TextBox(350, 50, 500, 100, callback=callback)
    while run:
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
        # button("New Game", 450, 150, 180, 70, green, light_green, action="NewGame")
        # button("Setting", 450, 250, 180, 70, red, light_red, action="Setting")
        Text = smallfont.render("Please Input your Username : ", 0, black)
        gameDisplay.blit(Text, (150, 100))

        # text_box.draw(gameDisplay)
        pygame.draw.rect(gameDisplay, gray, (480,90,350,50))
        if textinput.update(events):
            print(textinput.get_text())
        gameDisplay.blit(textinput.get_surface(), (500, 100))

        # Select Character
        button("GO!", 87, 579, 180, 70, blue, light_blue, action="Home")

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
    #rank_get = {'event': 5 , 'player': player1-1}
    #n.send(rank_get)
    #b = n.recv
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

        rank = json.loads(select.selectRank(2))#player ID

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
    count = 0

    textinput = GUINewGamePageTextBox.TextInput()           # 建立一個Textinput 的地方
    ResponseArea = pygame.Surface((600,150))
    ResponseArea.fill(black)
    # 都是 TextBox 的東西 By Chin - Foot#

    # 呢邊是 Button 的東西 By Chin - Head #
    SendBtn = GUINewGamePageButtonClick.button(blue,750,590,170,120,"GO")  # color , x, y, width, height , text
    token = True        # 模仿回合的結束 用來不給玩家在不是自己的回合中輸入
    # 呢邊是 Button 的東西 By Chin - Foot #

    map = select.selectMap(2)
    map = json.dumps(map)
    map = select.constructMap(map)

    head_font = smallfont  ##建立文字物件 by Dan  Changed : pygame.font.SysFont(None, 60) -> smallfont (By Chin)
    text_surface = head_font.render('illegal instruction', True, (255, 255, 255))  ##宣告文字物件的格式by Dan

    Sx = 200  # Set up Army position x Default Value - By Chin
    Sy = 90  # Set up Army position y Default Value - By Chin

    msg = smallfont  # 用於顯示不是目前玩家的回合
    MSG = msg.render("Not Your Turn", True, red)

    while intro:
        gameDisplay.fill(yellow)
        message_to_screen("Game Start", black, 1000, -340, size='large')
        gameDisplay.blit(ResponseArea, (80, 580))
        SendBtn.draw(gameDisplay)
        events = pygame.event.get()
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SendBtn.isOver(pos):
                   print("TextBox Locked!")
                   token = False                # 還未做出下一回合, 回恢權限 By Chin
            if event.type == pygame.MOUSEMOTION:
                if SendBtn.isOver(pos):
                    SendBtn.color = (light_blue)
                else :
                    SendBtn.color = (blue)


        if count < 4 and token:
            if textinput.update(events):              # 輸入指令的地方 By Chin
                # if count >= 3:
                    # 會否考慮顥示訊息 讓玩家知道不能輸入? By Chin
                # ResponseArea.blit(textinput.get_surface(), (10, 30 + (y * n)))
                n += 1
                y = 30
                command = textinput.get_text()
                print(command)  # 透過get_text() 取得輸入的資訊 By Chin
                TorF = Commander.inputCommand(player1,player2,1,command,map)##呼叫commander來解析指令 by Dan
                if TorF == True:##如果回傳值是true 就要記錄下來 by Dan
                    transComman.append(command)
                else:##指令有問題

                    ResponseArea.blit(text_surface, (10, 30 + (y * n))) ##顯示文字物件 by Dan
                count += 1

        # 如不是玩家回合則顯示MSG - By Chin
        if token == False:
            gameDisplay.blit(MSG,(750,720))

        gameDisplay.blit(textinput.get_surface(), (90, 585))         # TextInput position By Chin

        GUINewGamePageMap.Map(gameDisplay,map)

        # draw HQ position - By Chin
        gameDisplay.blit(HQ, (200, 360))
        # draw Infantry - Start By Chin
        # for i in len(Player.army):
        # Sx = Player.army[i].x
        # Sy = Player.army[i].y
        gameDisplay.blit(Infantry_Self, (Sx, Sy))
        # draw Infantry - End By Chin

        pygame.display.update()
        clock.tick(30)



def game_controls():
    gcont = True

    while gcont:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Controls", green, -100, size="large")
        message_to_screen("Fire: Spacebar", black, -30)
        message_to_screen("Move Turret: Up and Down arrows", black, 10)
        message_to_screen("Move Tank: Left and Right arrows", black, 50)
        message_to_screen("Pause: P", black, 90)

        button("play", 150, 500, 100, 50, green, light_green, action="play")
        button("Main", 350, 500, 100, 50, yellow, yellow, action="main")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")

        pygame.display.update()

        clock.tick(15)


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
    # a = n.getP()
    # # print(a)
    # global player
    # player = a['player']
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
    pygame.quit()


def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15

    while not gameExit:

        if gameOver == True:
            # gameDisplay.fill(white)
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass

                elif event.key == pygame.K_RIGHT:
                    pass

                elif event.key == pygame.K_UP:
                    pass


                elif event.key == pygame.K_DOWN:
                    pass

                elif event.key == pygame.K_p:
                    pause()

        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


# game_user()

game_intro()

# game_newgame()

# game_rank()

# gameLoop()

