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

def Map(gameDisplay,map):
    run = True
    SeaArea = []           # GUI 中的地圖海洋座標
    MountainArea = []      # GUI 中的地圖山座標

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
    # print(map)
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
            tmpX += 1
        tmpY += 1
    # print(i,k)

# Map(gameDisplay)