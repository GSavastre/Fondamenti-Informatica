import game2d

dx = 50
dy = 50
screen_x = 500
screen_y = 500
image = game2d.image_load("http://www.sportspearl.com/wp-content/uploads/2017/05/football-150x150.png")

def update():
    global dx,dy,verso
    
    game2d.canvas_fill((255,255,255))
    game2d.image_blit(image, (dx, dy))
    
    if  dx < screen_x - 150 and dy < screen_y - 150:
        dx = (dx + 20)
        dy = (dy + 60)
    elif dx < screen_x - 150 and dy == screen_y -150:
        dx = (dx + 20)

def main():
    game2d.canvas_init((screen_x,screen_y))
    game2d.set_interval(update,1000//30)

if __name__ == "__main__":
    main()


