import pygame
import GUINewGamePageTextBox
import GUIUserPageCreateGame
pygame.init()

display_width = 1024
display_height = 768
gameDisplay = pygame.display.set_mode((display_width, display_height))

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

            if action == "Browse":
                return GUIUserPageCreateGame.game_CreateGame(2)

            if action == "CreateGame":
                GUIUserPageCreateGame.game_CreateGame(1)

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, btncolor, x, y, width, height)

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

# game_user()