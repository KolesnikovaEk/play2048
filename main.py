import numpy as np
import random
import pygame
import sys
import os
from pygame.locals import *


CP = {
    'back': (189, 172, 161),
    0: (204, 192, 179),
    2: (238, 228, 219),
    4: (240, 226, 202),
    8: (242, 177, 121),
    16: (236, 141, 85),
    32: (250, 123, 92),
    64: (234, 90, 56),
    128: (237, 207, 114),
    256: (242, 208, 75),
    512: (237, 200, 80),
    1024: (227, 186, 19),
    2048: (236, 196, 2),
    4096: (96, 217, 146)
}

level = 1

n = 4

size = width, height = 10, 10
screen = pygame.display.set_mode(size)
pygame.display.set_caption('')
clock = pygame.time.Clock()

FPS = 50

def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
        return image

def terminate():
    pygame.quit()
    sys.exit()

class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
	    

class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, random.choice([(189, 172, 161), (204, 192, 179), (238, 228, 219),
	                                            (240, 226, 202), (242, 177, 121), (236, 141, 85),
	                                            (250, 123, 92), (234, 90, 56), (237, 207, 114),
	                                            (242, 208, 75), (237, 200, 80), (227, 186, 19),
	                                            (236, 196, 2), (96, 217, 146)]), 
	                                            [radius, radius, radius, radius])
        self.rect=pygame.Rect(x, y, radius * 2, radius * 2)
        self.vx=random.randint(-5, 5)
        self.vy=random.randrange(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx

width, height = 700, 100
all_sprites = pygame.sprite.Group()

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
for i in range(100):
    Ball(10, 100, 50)

class Wow(pygame.sprite.Sprite):
    def __init__(self):
        super(Wow, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('Sprite1.png'))
        self.images.append(pygame.image.load('Sprite1.png'))
        self.images.append(pygame.image.load('Sprite1.png'))
        self.images.append(pygame.image.load('Sprite1.png'))
        self.images.append(pygame.image.load('Sprite1.png'))
        self.images.append(pygame.image.load('Sprite2.png'))
        self.images.append(pygame.image.load('Sprite2.png'))
        self.images.append(pygame.image.load('Sprite2.png'))
        self.images.append(pygame.image.load('Sprite2.png'))
        self.images.append(pygame.image.load('Sprite2.png'))

        self.index = 0

        self.image = self.images[self.index]
        self.rect = pygame.Rect(505, 555, 150, 198)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]

def rules():
    width = 800
    height = 1200
    width2 = 100
    height2 = 1200
    my_sprite = Wow()
    my_group = pygame.sprite.Group(my_sprite)    
    while True:
        clock.tick(30)
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if width2 / 2 <= mouse[0] <= width2 / 2 + 260 and height2 / 2 <= mouse[1] <= height2 / 2 + 60:
                    return
                break
        my_group.update()
        screen.fill(pygame.Color("white"))
        my_group.draw(screen)
        color = (255, 255, 255)
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        smallfont = pygame.font.SysFont('Corbel', 35)
        text2 = smallfont.render('на главную', True, color)
        mouse = pygame.mouse.get_pos()
        if width2 / 2 <= mouse[0] <= width2 / 2 + 360 and height2 / 2 <= mouse[1] <= height2 / 2 + 60:
            pygame.draw.rect(screen, color_light, [width2 / 2, height2 / 2, 360, 60])
        else:
            pygame.draw.rect(screen, color_dark, [width2 / 2, height2 / 2, 360, 60])
        screen.blit(text2, (width2 / 2 + 100, height2 / 2 + 17))
        fon1 = pygame.transform.scale(load_image('1.png'), (300, 300))
        fon2 = pygame.transform.scale(load_image('2.png'), (300, 300))
        screen.blit(fon1, (50, 200))
        screen.blit(fon2, (350, 200))
        all_sprites.draw(screen)
        pygame.display.flip()


def start_screen():
    global level
    fon = pygame.transform.scale(load_image('2048.png'), (700, 700))
    screen.blit(fon, (0, 0))
    width = 400
    height = 550
    width3 = 400
    height3 = 700
    width2 = 250
    height2 = 1250
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    smallfont=pygame.font.SysFont('Corbel', 35)
    text = smallfont.render("Уровень: сложный", True, (255, 255, 255))
    text3 = smallfont.render("Уровень: легкий", True, (255, 255, 255))
    text2 = smallfont.render("Ознакомиться с правилами игры", True, (255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 <= mouse[0] <= width / 2 + 300 and height / 2 <= mouse[1] <= height / 2 + 60:
                    level = 1
                    return
                if width3 / 2 <= mouse[0] <= width3 / 2 + 300 and height3 / 2 <= mouse[1] <= height3 / 2 + 60:
                    level = 2
                    return
                if width2 / 2 <= mouse[0] <= width2 / 2 + 500 and height2 / 2 <= mouse[1] <= height2 / 2 + 60:
                    rules()

        fon = pygame.transform.scale(load_image('2048.png'), (700, 700))
        screen.blit(fon, (0, 0))
        mouse = pygame.mouse.get_pos()
        if width / 2 <= mouse[0] <= width / 2 + 300 and height / 2 <= mouse[1] <= height / 2 + 60:
	        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 300, 60])
        else:
	        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 300, 60])
        if width2 / 2 <= mouse[0] <= width2 / 2 + 500 and height2 / 2 <= mouse[1] <= height2 / 2 + 60:
	        pygame.draw.rect(screen, color_light, [width2 / 2, height2 / 2, 500, 60])
        else:
	        pygame.draw.rect(screen, color_dark, [width2 / 2, height2 / 2, 500, 60])
        if width3 / 2 <= mouse[0] <= width3 / 2 + 300 and height3 / 2 <= mouse[1] <= height3 / 2 + 60:
	        pygame.draw.rect(screen, color_light, [width3 / 2, height3 / 2, 300, 60])
        else:
	        pygame.draw.rect(screen, color_dark, [width3 / 2, height3 / 2, 300, 60])
        screen.blit(text, (width / 2 + 40, height / 2 + 15))
        screen.blit(text2, (width2 / 2 + 40, height2 / 2 + 15))
        screen.blit(text3, (width3 / 2 + 40, height3 / 2 + 15))
        pygame.display.update()
        clock.tick(FPS)


class Over(pygame.sprite.Sprite):
    image = load_image("gameover.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Over.image
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0
        self.flag = True

    def update(self, *args):
        if self.flag:
            self.rect = self.rect.move(1, 0)
            if self.rect.x >= 0:
                self.flag = False


class Py2048:
    def __init__(self):
        self.grid = np.zeros((n, n), dtype=int)
        self.score = 0
        self.W = 700
        self.H = self.W
        self.SPACING = 10
        self.pred = []
        self.flag = True
        self.start = True
        self.star = load_image('star.png')
        self.particles = []
        self.a = 0

        pygame.init()
        pygame.display.set_caption("2048")

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        self.screen = pygame.display.set_mode((self.W, self.H))

    def record(self):
        f = open("score.txt", 'r')
        a = f.readlines()
        f.close()
        self.a = max(list(map(int, a)))
        value = pygame.font.SysFont("comicsansms", 40).render("Лучший результат: " + str(self.a), True, (255, 255, 102))
        self.screen.blit(value, [0, 50])

    def __str__(self):
        return str(self.grid)

    def Your_score(self, score):
        value = pygame.font.SysFont("comicsansms", 50).render("Ваш счёт: " + str(score), True, (255, 255, 102))
        self.screen.blit(value, [0, 0])

    def new_number(self, k=1):
        global level
        if level == 1:
            k = k
            free_poss = list(zip(*np.where(self.grid == 0)))
            for pos in random.sample(free_poss, k=k):
                if random.random() < .1:
                    self.grid[pos] = 4
                else:
                    self.grid[pos] = 2
        else:
            k = k
            free_poss = list(zip(*np.where(self.grid == 0)))
            for pos in random.sample(free_poss, k=k):
                if random.random() < .1:
                    self.grid[pos] = 8
                else:
                    self.grid[pos] = 4
		

    def _get_nums(self, this):
        this_n = this[this != 0]
        this_n_sum = []
        skip = False
        for j in range(len(this_n)):
            if skip:
                skip = False
                continue
            if j != len(this_n) - 1 and this_n[j] == this_n[j + 1]:
                new_n = this_n[j] * 2
                self.score += this_n[j] * 2
                skip = True
            else:
                new_n = this_n[j]
            this_n_sum.append(new_n)
        return np.array(this_n_sum)

    def make_move(self, move):
        for i in range(n):
            if move in 'lr':
                this = self.grid[i, :]
            else:
                this = self.grid[:, i]

            flipped = False
            if move in 'rd':
                flipped = True
                this = this[::-1]
                
            this_n = self._get_nums(this)

            new_this = np.zeros_like(this)
            new_this[:len(this_n)]=this_n
            if flipped:
                new_this = new_this[::-1]
            if move in 'lr':
                self.grid[i, :] = new_this
            else:
                self.grid[:, i] = new_this


    def emit_particle(self, x, y, x_vel, y_vel, radius):
        self.particles.append([[x, y], [x_vel, y_vel], radius])

    
    def update_particles(self):
        for i, particle in reversed(list(enumerate(self.particles))):
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 1
        
            reversed_particle = self.particles[len(self.particles) - i - 1]
            image_copy = pygame.transform.scale(self.star, (reversed_particle[2], reversed_particle[2]))
            screen.blit(image_copy, (int(reversed_particle[0][0]), int(reversed_particle[0][1])))

            if particle[2] <= 0:
                self.particles.pop(i)

    def draw_game(self):
        self.screen.fill(CP['back'])
        self.record()
        self.Your_score(self.score)
	
        for i in range(n):
            for j in range(n):
                n2 = self.grid[i][j]
                a = [130, 240, 350, 460]
                rect_w = rect_h = 105
                if j == 0:
                    rect_x = a[0]
                elif j == 1:
                    rect_x = a[1]
                elif j == 2:
                    rect_x = a[2]
                elif j == 3:
                    rect_x = a[3]
                if i == 0:
                    rect_y = a[0]
                elif i == 1:
                    rect_y = a[1]
                elif i == 2:
                    rect_y = a[2]
                elif i == 3:
                    rect_y = a[3]

                pygame.draw.rect(self.screen,
                                CP[n2],
                                pygame.Rect(rect_x, rect_y, rect_w, rect_h),
                                border_radius=8)
                if n2 == 0:
                    continue
                text_surface = self.myfont.render(f'{n2}', True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(rect_x + rect_w / 2,
                                                          rect_y + rect_h / 2))
                self.screen.blit(text_surface, text_rect)

		
    def wait_for_key(self):
        color = (255, 255, 255)
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        width = 950
        height = 100
        width2 = 950
        height2 = 1200
        smallfont = pygame.font.SysFont('Corbel', 35)
        text = smallfont.render('Выйти', True, color)
        text2 = smallfont.render('Обновить', True, color)
        while True:

            mouse = pygame.mouse.get_pos()
            if width / 2 <= mouse[0] <= width / 2 + 200 and height / 2 <= mouse[1] <= height / 2 + 60:
                pygame.draw.rect(screen, color_light, [width / 2, height / 2, 200, 60])
            else:
                pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 200, 60])
            if width2 / 2 <= mouse[0] <= width2 / 2 + 200 and height2 / 2 <= mouse[1] <= height2 / 2 + 60:
                pygame.draw.rect(screen, color_light, [width2 / 2, height2 / 2, 200, 60])
            else:
                pygame.draw.rect(screen, color_dark, [width2 / 2, height2 / 2, 200, 60])
            screen.blit(text2, (width2 / 2 + 45, height2 / 2 + 20))
            screen.blit(text, (width / 2 + 45, height / 2 + 20))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    return 'q'
                if event.type == MOUSEBUTTONDOWN:
                    if width / 2 <= mouse[0] <= width / 2 + 200 and height / 2 <= mouse[1] <= height / 2 + 60:
                        return 'q'
                    if width2 / 2 <= mouse[0] <= width2 / 2 + 200 and height2 / 2 <= mouse[1] <= height2 / 2 + 60:
                        return 'update'
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        return 'u'                   
                    elif event.key == K_RIGHT:
                        return 'r'
                    elif event.key == K_LEFT:
                        return 'l'
                    elif event.key == K_DOWN:
                        return 'd'


    def game_over(self):
        grid_bu = self.grid.copy()
        for move in 'lrud':
            self.make_move(move)
            if not all((self.grid == grid_bu).flatten()):
                self.grid = grid_bu
                return False
        return True

    def update(self):
        f = open("score.txt", 'w')
        f.write('0')
        f.close()        
     

    def play(self):
        if self.start:
            self.start = False
            start_screen()
        self.grid = np.zeros((n, n), dtype=int)
        self.score = 0
        self.W = 700
        self.H = self.W
        self.SPACING = 10
        self.pred = []
        self.flag = True

        pygame.init()
        pygame.display.set_caption("2048")

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        self.screen = pygame.display.set_mode((self.W, self.H))
        
        self.new_number(k=2)
        while True:
            self.draw_game()
            pygame.display.flip()
            cmd = self.wait_for_key()
            if cmd == 'update':
                self.update()
                continue
            elif cmd == 'q':
                self.flag = False
            elif self.flag:
                old_grid = self.grid.copy()
                self.make_move(cmd)
		

            if self.game_over() or not self.flag:
                f = open("score.txt", 'r')
                a = f.readlines()
                f.close()
                self.a = max(list(map(int, a)))
                f = open("score.txt", 'a')
                f.write('\n' + str(self.score))
                f.close()
                pygame.init()
                pygame.display.set_caption("Game Over")
                pygame.font.init()
                self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
                self.screen = pygame.display.set_mode((700, 700))
                clock = pygame.time.Clock()

                all_sprites = pygame.sprite.Group()
                width = 800
                height = 1200
                width2 = 100
                height2 = 1200
                Over(all_sprites)
		

                running = True
                while running:
                    clock.tick(500)
                    all_sprites.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                if width / 2 <= mouse[0] <= width / 2 + 260 and height / 2 <= mouse[1] <= height / 2 + 60:
                                        terminate()
                                if width2 / 2 <= mouse[0] <= width2 / 2 + 260 and height2 / 2 <= mouse[1] <= height2 / 2 + 60:
                                        self.start = True
                                        self.play()
                                break


                    screen.fill(pygame.Color("white"))

                    color = (255, 255, 255)
                    color_light = (170, 170, 170)
                    color_dark = (100, 100, 100)
                    smallfont = pygame.font.SysFont('Corbel', 35)
                    text = smallfont.render('выйти', True, color)
                    text2 = smallfont.render('играть', True, color)

                    mouse = pygame.mouse.get_pos()
                    if width / 2 <= mouse[0] <= width / 2 + 260 and height / 2 <= mouse[1] <= height / 2 + 60:
                            pygame.draw.rect(screen, color_light, [width / 2, height / 2, 260, 60])
                    else:
                            pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 260, 60])
                    if width2 / 2 <= mouse[0] <= width2 / 2 + 260 and height2 / 2 <= mouse[1] <= height2 / 2 + 60:
                            pygame.draw.rect(screen, color_light, [width2 / 2, height2 / 2, 260, 60])
                    else:
                            pygame.draw.rect(screen, color_dark, [width2 / 2, height2 / 2, 260, 60])
                    screen.blit(text, (width / 2 + 100, height / 2 + 17))
                    screen.blit(text2, (width2 / 2 + 100, height2 / 2 + 17))

                    if self.a < self.score:
                        self.emit_particle(300, 300, random.uniform(-15, 15), random.uniform(-15, 15), 50)
                        self.update_particles()

                        intro_text = "Новый рекорд!"
                        font = pygame.font.Font(None, 60)
                        string_rendered = font.render(intro_text, 1, pygame.Color('black'))
                        screen.blit(string_rendered, [200, 50])
                    all_sprites.draw(screen)
                    pygame.display.update()
                break

            if not all((self.grid == old_grid).flatten()):
                self.new_number()


if __name__ == '__main__':
    game = Py2048()
    game.play()