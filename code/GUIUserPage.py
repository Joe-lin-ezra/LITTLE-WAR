import pygame
import GUINewGamePageTextBox
import GUIBrowser

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
        Text = TextStyle.render("Please Input your Username : ", 0, black)
        gameDisplay.blit(Text, (90, 45))

        # text_box.draw(gameDisplay)
        pygame.draw.rect(gameDisplay, gray, (480,40,350,50))
        if textinput.update(events):
            FileName = textinput.get_text()
            if GUIBrowser.FileCheck(FileName,gameDisplay):
                print("Success!")
            else:
                print("Fail!")

        gameDisplay.blit(textinput.get_surface(), (500, 50))

        gameDisplay.blit(IDTitle,(200,110))
        gameDisplay.blit(NameTitle,(550,110))

        # Select Character
        button("GO!", 87, 600, 180, 70, blue, light_blue, action="Home")

        pygame.display.update()
        clock.tick(15)

game_user()