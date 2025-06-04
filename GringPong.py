from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, spr_image, spr_speed, spr_x, spr_y, size_1, size_2):
        super().__init__()
        self.s_1 = size_1
        self.s_2 = size_2
        self.image = transform.scale(image.load(spr_image), (self.s_1, self.s_2))
        self.speed = spr_speed
        self.rect = self.image.get_rect()
        self.rect.x = spr_x
        self.rect.y = spr_y
        self.spr_x = spr_x
        self.spr_y = spr_y

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(spr_image), (self.s_1, self.s_2))
        self.speed = spr_speed

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = spr_x
        self.rect.y = spr_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        
        if key_pressed[K_s] and self.rect.y < 530:
            self.rect.y += self.speed

        if key_pressed[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
    
    def pais_origen (self):
        self.rect.x = self.spr_x
        self.rect.y = self.spr_y

class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        
        if key_pressed[K_DOWN] and self.rect.y < 530:
            self.rect.y += self.speed

        if key_pressed[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed
    
    def pais_origen (self):
        self.rect.x = self.spr_x
        self.rect.y = self.spr_y
    
window = display.set_mode((1280, 720))
display.set_caption("Gring Pong - The Game")
background = transform.scale(image.load("benidorm.jpg"), (1280, 720))

grupo_sprite1_espana = sprite.Group()
sprite1_espana = Player1("es_pala.png",12, 20, 350, 40, 175)
grupo_sprite1_espana.add(sprite1_espana)
grupo_sprite2_uk = sprite.Group()
sprite2_uk = Player2("uk_pala.png",12, 1220, 350, 40, 175)
grupo_sprite2_uk.add(sprite2_uk)

game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load("background_song.ogg")
mixer.music.play(loops=-1)

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    window.blit(background, (0, 0))
    grupo_sprite1_espana.draw(window)
    grupo_sprite1_espana.update()
    grupo_sprite2_uk.draw(window)
    grupo_sprite2_uk.update()
    display.update()
