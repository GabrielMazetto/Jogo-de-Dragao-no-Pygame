from cgitb import text
from turtle import width
import pygame, random, os

os.chdir('C:/Users/gabri/OneDrive/Documentos/Projetos em Python/Jogo_corrida_infinita')

WIDHT = 1200
HEIGHT = 600
SPEED = 10
GAME_SPEED = 10
GROUND_WIDTH = 2 * WIDHT
GROUND_HEIGHT = 30
 



def start_screen():
    start=False
    image = pygame.image.load('fundo_start.jpg').convert_alpha()
    image = pygame.transform.scale(image, [WIDHT, HEIGHT])
    while (start==False):
        myfont=pygame.font.SysFont("Britannic Bold", 40)
        font_titulo = pygame.font.SysFont("Britannic Bold", 100)
        titulo=font_titulo.render("Dragon Fly", 1, (0, 0, 0))
        game_window.blit(image, (0, 0))
        texto=myfont.render("Start", 1, (0, 0, 0))
        botao = pygame.draw.rect(game_window, (255, 255, 255), (WIDHT/2 - 55, HEIGHT/2, 100, 50))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type==pygame.MOUSEBUTTONDOWN:
                if botao.collidepoint(pygame.mouse.get_pos()):
                    start=True
        game_window.blit(titulo, (WIDHT/2 - 130, 20))
        game_window.blit(texto, (WIDHT/2 - 40, HEIGHT/2 + 10))
        pygame.display.flip()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_run = [pygame.image.load('dragao1.png').convert_alpha(),
                          pygame.image.load('dragao2.png').convert_alpha(),
                          pygame.image.load('dragao3.png').convert_alpha(),
                          pygame.image.load('dragao4.png').convert_alpha(),
                          pygame.image.load('dragao5.png').convert_alpha(),
                          pygame.image.load('dragao6.png').convert_alpha(),
                          pygame.image.load('dragao7.png').convert_alpha(),
                          pygame.image.load('dragao8.png').convert_alpha(),
                          pygame.image.load('dragao9.png').convert_alpha(),
                          pygame.image.load('dragao10.png').convert_alpha(),
                          pygame.image.load('dragao11.png').convert_alpha(),
                          pygame.image.load('dragao12.png').convert_alpha(),
                          pygame.image.load('dragao13.png').convert_alpha(),
                          pygame.image.load('dragao14.png').convert_alpha(),
                          pygame.image.load('dragao15.png').convert_alpha(),
                          pygame.image.load('dragao16.png').convert_alpha(),
                          pygame.image.load('dragao17.png').convert_alpha(),
                          pygame.image.load('dragao18.png').convert_alpha(),
                          pygame.image.load('dragao19.png').convert_alpha(),
                          pygame.image.load('dragao20.png').convert_alpha()]
        self.image_fall = pygame.image.load('dragao1.png').convert_alpha()
        self.image = pygame.image.load('dragao1.png').convert_alpha()
        self.rect = pygame.Rect(80, 80, 80, 100)
        self.mask = pygame.mask.from_surface(self.image)
        self.current_image = 0

    def update(self, *args):
        def move_player(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                self.rect[0] += GAME_SPEED
            if key[pygame.K_a]:
                self.rect[0] -= GAME_SPEED
            self.current_image = (self.current_image + 1) % 10
            self.image = self.image_run[self.current_image]
            self.image = pygame.transform.scale(self.image, [150, 150])
        move_player(self)
        self.rect[1] += SPEED

        def fly(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                self.rect[1] -= 30
            self.current_image = (self.current_image + 1) % 10
            self.image = self.image_run[self.current_image]                
            self.image = pygame.transform.scale(self.image, [150, 150])
        fly(self)


        def down(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_s]:
                self.rect[1] += 15
            self.current_image = (self.current_image + 1) % 10
            self.image = self.image_run[self.current_image]                
            self.image = pygame.transform.scale(self.image, [150, 150])
        down(self)


        def fall(self):
            key = pygame.key.get_pressed()
            if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_w] and not key[pygame.K_s] and not key[pygame.K_d] and not key[pygame.K_a]:
                self.image = pygame.image.load('dragao17.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, [150, 150])

        fall(self)


class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('chao.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = HEIGHT - GROUND_HEIGHT

    def update(self, *args):
        self.rect[0] -= GAME_SPEED

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('obstaculo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [80, 80])
        self.rect = pygame.Rect(50, 50, 80, 80)
        self.rect[0] = xpos
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[1] = HEIGHT - ysize

    def update(self, *args):
        self.rect[0] -= GAME_SPEED


class Coins(pygame.sprite.Sprite):
    def __init__(self, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('moeda.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [40, 40])
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[0] = xpos
        self.rect[1] = HEIGHT - ysize

    def update(self, *args):
        self.rect[0] -= GAME_SPEED

def get_random_obstacles(xpos):
    size = random.randint(120, 600)
    box = Obstacles(xpos, size)
    return box

def get_random_coins(xpos):
    size = random.randint(60, 500)
    coin = Coins(xpos, size)
    return coin


def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

pygame.init()
game_window = pygame.display.set_mode([WIDHT, HEIGHT])

start_screen()

musica = pygame.mixer.music.load("musica_fundo.mp3")
pygame.mixer.music.play(-1)
barulho_asa_dragao = pygame.mixer.Sound("barulho_asa_dragao.wav")
barulho_moeda = pygame.mixer.Sound("barulho_moeda.wav")
barulho_rugido = pygame.mixer.Sound("barulho_rugido.wav")

pygame.display.set_caption('Jogo 01')

BACKGROUND = pygame.image.load('fundo.png').convert_alpha()
BACKGROUND = pygame.transform.scale(BACKGROUND, [WIDHT, HEIGHT])

playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)

groundGroup = pygame.sprite.Group()
for i in range(2):
    ground = Ground(WIDHT * i)
    groundGroup.add(ground)

coinsGroup = pygame.sprite.Group()
for i in range(2):
    coin = get_random_coins(WIDHT * i + 1000)
    coinsGroup.add(coin)

obstacleGroup = pygame.sprite.Group()
for i in range(2):
    obstacle = get_random_obstacles(WIDHT * i + 1000)
    obstacleGroup.add(obstacle)

gameloop = True
def draw():
    playerGroup.draw(game_window)
    groundGroup.draw(game_window)
    obstacleGroup.draw(game_window)
    coinsGroup.draw(game_window)

def update():
    playerGroup.update()
    groundGroup.update()
    obstacleGroup.update()
    coinsGroup.update()



clock = pygame.time.Clock()
placar = 0
barulho_asa_dragao.play(-1)
while gameloop:
    clock.tick(20)
    game_window.blit(BACKGROUND, (0,0))
    font = pygame.font.SysFont('Arial', 30)
    text = font.render('Pontos:', True, [255, 255, 255])
    
    game_window.blit(text, [ 1100, 20])
    contador = font.render(f'{placar}', True, [255, 255, 255])
    game_window.blit(contador, [1125, 50])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    key = pygame.key.get_pressed()
    if not key[pygame.K_w] and not key[pygame.K_s] and not key[pygame.K_d] and not key[pygame.K_a]:
        barulho_asa_dragao.set_volume(0)
    else:
        barulho_asa_dragao.set_volume(90)

        
    if is_off_screen(groundGroup.sprites()[0]):
        groundGroup.remove(groundGroup.sprites()[0])
        newGround = Ground(WIDHT - 20)
        groundGroup.add(newGround)
        newObstacle = get_random_obstacles(WIDHT*2.1)
        newObstacle1 = get_random_obstacles(WIDHT*1.8)
        newObstacle2 = get_random_obstacles(WIDHT*2.5)
        obstacleGroup.add(newObstacle)
        obstacleGroup.add(newObstacle1)
        obstacleGroup.add(newObstacle2)
        newCoin = get_random_coins(WIDHT * 2)
        newCoin1 = get_random_coins(WIDHT * 2.2)
        newCoin2 = get_random_coins(WIDHT * 2.4)
        newCoin3= get_random_coins(WIDHT * 2.6)
        newCoin4 = get_random_coins(WIDHT * 2.8)
        coinsGroup.add(newCoin)
        coinsGroup.add(newCoin1)
        coinsGroup.add(newCoin2)
        coinsGroup.add(newCoin3)
        coinsGroup.add(newCoin4)
    
    """
    if player.rect[0] < 0 or player.rect[2] > 500:
        SPEED = 0
    else:
        SPEED = 2      
    """         

    if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
        SPEED = 0
    else:
        SPEED = 2
    
    if pygame.sprite.groupcollide(playerGroup, coinsGroup, False, True):
        barulho_moeda.play()
        placar += 1

    if placar % 5 == 0 and placar != 0:
        GAME_SPEED += 0.08
        barulho_rugido.play()
    

    if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
        break


    update()
    draw()
    pygame.display.update()