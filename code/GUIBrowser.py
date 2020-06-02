import pygame
import os , sys

display_width = 1024
display_height = 768
# gameDisplay = pygame.display.set_mode((display_width, display_height))


# dir_path = os.path.dirname(os.path.realpath(__file__))                  #current directory path
# dir_path = "."

dir_path = os.chdir('C:/Users/chin/Documents/GitHub')                   # 換路徑
dirs = os.listdir(dir_path)
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)
# Filename = Filename+".py"

def FileCheck(FileName,gameDisplay):
    Exist = 0
    msg = smallfont  # 用於顯示不是目前玩家的回合
    IDy = 110
    for file in dirs:
        # print(file)
        if file == FileName:
            Exist = 1
    if Exist:
        print("File Found!")
        for file in dirs:
            IDy = IDy + 50
            MSG = msg.render(FileName, True, (0,0,0))
            gameDisplay.blit(MSG,(200,IDy))
        return True
    else:
        print("File Don't exist!")
        return False

