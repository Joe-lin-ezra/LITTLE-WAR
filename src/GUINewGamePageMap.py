import pygame


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

clock = pygame.time.Clock()
# gameDisplay = pygame.display.set_mode((1024, 768))

def Map(gameDisplay,map,mapInfor,turn):
    run = True
    SeaArea = []           # GUI 中的地圖海洋座標
    MountainArea = []      # GUI 中的地圖山座標
    Player1Area = []
    Player2Area = []
    xpix = len(map)     # 15
    ypix = len(map[0])  # 10

    Ax = 200
    Ay = 50

    Ix = 250

    Bx = 800
    By = 50

    Cx = 200
    Cy = 400

    Dx = 800
    Dy = 400
    count = 0

    tmpX = 0
    tmpY = 0    #用來虛擬mapIndex
    size = 50

    # 畫出可生成地區
    Player1_x1 = mapInfor['Player1_Area']['x1']
    Player1_y1 = mapInfor["Player1_Area"]['y1']

    Player1_x2 = mapInfor["Player1_Area"]['x2']
    Player1_y2 = mapInfor["Player1_Area"]['y2']

    for x in range(Player1_x1,Player1_x2+1):
        for y in range(Player1_y1,Player1_y2+1):
            Player1Area.append([x,y])

    Player2_x1 = mapInfor['Player2_Area']['x1']
    Player2_y1 = mapInfor["Player2_Area"]['y1']

    Player2_x2 = mapInfor["Player2_Area"]['x2']
    Player2_y2 = mapInfor["Player2_Area"]['y2']

    for x in range(Player2_x1,Player2_x2+1):
        for y in range(Player2_y1,Player2_y2+1):
            Player2Area.append([x,y])

    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == 1:
                SeaArea.append([x,y])
    # print(SeaArea)
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == 2:
                MountainArea.append([x, y])
    # print(MountainArea)

    tmpX = 0
    tmpY = 0
    check = 0       # 0 : 能夠生成的 1 : 不能生成的
    for k in range(Ay,Cy+3*size,size):
        tmpX = 0
        for i in range(Ax,Bx+3*size,size):
            color = green
            for q in range(len(SeaArea)):
                if tmpX == SeaArea[q][0] and tmpY == SeaArea[q][1]:
                    color = blue
            for q in range(len(MountainArea)):
                if tmpX == MountainArea[q][0] and tmpY == MountainArea[q][1]:
                    color = brown
            pygame.draw.rect(gameDisplay, color, (i, k, size, size))
            pygame.draw.rect(gameDisplay, black, pygame.Rect(i, k, size, size),2)          # draw rect border with 2 px
            if turn == 1:
                for q in range(len(Player1Area)):
                    check = 0
                    if tmpX == Player1Area[q][0] and tmpY == Player1Area[q][1]:
                        bg_img = pygame.Surface((size, size))
                        bg_img.set_alpha(150)
                        pygame.draw.rect(bg_img, red, bg_img.get_rect())
                        if check != 1:
                            gameDisplay.blit(bg_img, (i,k))
            else:
                for q in range(len(Player2Area)):
                    check = 0
                    if tmpX == Player2Area[q][0] and tmpY == Player2Area[q][1]:
                        bg_img = pygame.Surface((size, size))
                        bg_img.set_alpha(150)
                        pygame.draw.rect(bg_img, red, bg_img.get_rect())
                        if check != 1:
                            gameDisplay.blit(bg_img, (i,k))
            tmpX += 1
        tmpY += 1
    # print(i,k)

# Map(gameDisplay)