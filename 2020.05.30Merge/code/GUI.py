import pygame
import time
import random
import glob
import json
import select
import sqlite3
from network import Network

pygame.init()

display_width = 1024
display_height = 768
n = Network()
# player = 0

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
    with open("Json/0.json") as f:
        data = json.loads(f.read())
except :
    with open("Json/Test.json" , 'w') as file :
        data = json.dumps(Json)
        file.write(data)
    with open("Json/Test.json") as f :
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


class TextBox:
    def __init__(self, w, h, x, y, font=None, callback=None):
        """
        :param w:文本框宽度
        :param h:文本框高度
        :param x:文本框坐标
        :param y:文本框坐标
        :param font:文本框中使用的字体
        :param callback:在文本框按下回车键之后的回调函数
        """
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.text = ""  # 文本框内容
        self.callback = callback
        # 创建
        self.__surface = pygame.Surface((w, h))
        self.__surface.fill((79,93,92))     #change textbox color
        # 如果font为None,那么效果可能不太好，建议传入font，更好调节
        if font is None:
            self.font = pygame.font.Font(None, 60)  # 使用pygame自带字体
        else:
            self.font = font

    def draw(self, dest_surf):
        text_surf = self.font.render(self.text, True, (249,246,231))        # Change Font color
        dest_surf.blit(self.__surface, (self.x, self.y))
        dest_surf.blit(text_surf, (self.x, self.y + (self.height - text_surf.get_height())),
                       (0, 0, self.width, self.height))

    def key_down(self, event):
        unicode = event.unicode
        key = event.key

        # 退位键
        if key == 8:
            self.text = self.text[:-1]
            return

        # 切换大小写键
        if key == 301:
            return

        # 回车键
        if key == 13:
            if self.callback is not None:
                self.callback(self.text)
            return

        if unicode != "":
            char = unicode
        else:
            char = chr(key)

        self.text += char


def callback(key):
    print(key)
    # To send the username to DB

def game_user():
    run = True
    text_box = TextBox(350, 50, 500, 100, callback=callback)
    while run:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                text_box.key_down(event)

        gameDisplay.fill(yellow)
        # button("New Game", 450, 150, 180, 70, green, light_green, action="NewGame")
        # button("Setting", 450, 250, 180, 70, red, light_red, action="Setting")
        Text = smallfont.render("Please Input your Username : ",0,black)
        gameDisplay.blit(Text,(150,100))

        text_box.draw(gameDisplay)

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

        gameDisplay.fill(yellow)
        button("New Game", 450, 150, 180, 70, green, light_green, action="NewGame")
        button("Setting", 450, 250, 180, 70, red, light_red, action="Setting")
        button("Ranking", 450, 350, 180, 70, blue, light_blue, action="Ranking")

        pygame.display.update()
        clock.tick(15)

def game_rank():
    run = True
    d = {'event': 4, 'player': 0, 'ID': 1}
    d['player'] = player-1
    a = n.send(d)
    # print(a,123)
    b = n.recv()
    # print(b)
    while run:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(yellow)

        ID_txt = medfont.render("ID",True,black)
        gameDisplay.blit(ID_txt,(87,40))

        Name_txt = medfont.render("Name",True,black)
        gameDisplay.blit(Name_txt,(427,40))

        Win_txt = medfont.render("Win",True,black)
        gameDisplay.blit(Win_txt,(867,40))

        # rank = json.loads(select.selectRank(2))#player ID
        rank = json.loads(b)
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
    run = True
    n.send({'event': 1, 'player': (player-1)})
    while run:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(yellow)
        Map(gameDisplay)
        Title = largefont.render("Game Start!",True,gray)
        gameDisplay.blit(Title,(270,30))
        pygame.display.update()
        clock.tick(15)

def Map(gameDisplay):
    gameDisplay.fill((255,255,000))

    n.send({'event': 5, 'player': (player-1)})
    map = n.recv()
    print(map)
    map = select.constructMap(map)
    # map = select.selectMap(1)
    # map = select.constructMap(map)

    # map -> color
    # 0 - green (normal)
    # 1 - blue (water)
    # 2 - brown (mountain)
    # print(map[1][0])
    # print(len(map[1]))

    x=137
    y=200
    row = len(map)
    col = print(len(map))  #row y,x
    i = 0

    while row:
        if(map[i][1] == 0):
            Color = light_green
        elif(map[i][1] == 1):
            Color = blue
        elif(map[i][1] == 2):
            Color = brown
        pygame.draw.rect(gameDisplay,Color,(x,y,40,40))
        x += 40
        row -= 1
        i += 1

    pygame.display.update()


def game_controls():
    gcont = True

    while gcont:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
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


def button(text, x, y, width, height, inactive_color, active_color, action=None, btncolor = black):
    cur = pygame.mouse.get_pos()
    print(cur)
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
                game_newgame()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, btncolor, x, y, width, height)


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
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:

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
        self.images = [pygame.image.load(img) for img in glob.glob("img/loading-*.png")]
        self.index = 0
        self.rect = pygame.Rect( 3,-50, 150, 198)

    def update(self):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1

def game_loading():
    a = n.getP()
    # print(a)
    global player
    player = a['player']
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

# game_rank()

# gameLoop()

# map.close()

# game_newgame()
