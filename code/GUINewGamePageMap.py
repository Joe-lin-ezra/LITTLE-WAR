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
    # gameDisplay.fill((255, 255, 000))

    # map = np.array(select.constructMap(map))
    # map = map.transpose()

    # print(map)
    # map -> color
    # 0 - green (normal)
    # 1 - blue (water)
    # 2 - brown (mountain)

    x = 200
    y = 50

    xAis = len(map)  # 15
    yAis = len(map[2])  # 10

    xIndex = 0
    yIndex = 0
    # print(map[xIndex])
    # print(map[xIndex][yIndex])

    while yAis:
        if (yIndex == yAis):
            break
        xIndex = 0
        y += 40
        x = 200
        while xAis:
            if (xIndex == xAis):
                break
            if (map[xIndex][yIndex] == 0):
                Color = light_green
            elif (map[xIndex][yIndex] == 1):
                Color = blue
            elif (map[xIndex][yIndex] == 2):
                Color = brown
            pygame.draw.rect(gameDisplay, Color, (x, y, 50, 50))
            x += 40
            # y+=40
            xIndex += 1
        yIndex += 1

    pygame.display.update()

# Map(gameDisplay)