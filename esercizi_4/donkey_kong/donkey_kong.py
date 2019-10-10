import game2d, actor, jumper,entities, dk_elements

screen_x, screen_y = 224,256

def initialize():

    global arena, mario, background, sprites, platforms
    
    arena = actor.Arena(screen_x,screen_y)

    mario = jumper.Jumper(arena,16,248)
    
    game2d.canvas_init(arena.size())

    platforms = []

    for n in range(len(dk_elements.map_elements)):
        if dk_elements.map_elements[n][0] == "Platform":
            
            x, y, w, h = dk_elements.map_elements[n][-4:]
            platforms.append(entities.Platform(x, y, w, h, arena))
            
            print(platforms)

    background = game2d.image_load("dk_background.png")

    sprites = game2d.image_load("dk_sprites.png")

    game2d.handle_keyboard(keydown, keyup)

def keydown(key: str):
    print(key)
    if key == "ArrowUp":
        mario.go_up()
    elif key == "Spacebar":
        mari.jump()
    elif key == "ArrowDown":
        mario.go_down()
    elif key == "ArrowLeft":
        mario.go_left()
    elif key == "ArrowRight":
        mario.go_right()

def keyup(key: str):
    mario.stay()
    
def update():
    game2d.image_blit(background,(0,0),(0,0,arena.size()[0],arena.size()[1]))
    mario.move()
    """
    x, y, w, h = mario.rect()
    for p in platforms:
        x1, y1, h1, w1 = p.rect()
        if arena.check_collision(mario, p):
            mario.repos_y(y1+h)
            
    if y+h not in platforms[][2]:
        mario.go_down()
    """       
    game2d.image_blit(sprites,mario.rect(),mario.symbol())

def main():
    initialize()
    game2d.set_interval(update, 1000//30)
    
if __name__ == "__main__":
    main()
