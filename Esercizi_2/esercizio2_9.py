#Animazione del movimento serpentina
import game2d

screen_x = 600
screen_y = 800

dx = 150
dy = 150
image = game2d.image_load("http://www.sportspearl.com/wp-content/uploads/2017/05/football-150x150.png")
x_on = y_on = 0
input_open = True


def keydown(key: str):
    global x_on,y_on,input_open

    if x_on != 0 and y_on != 0:
        input_open = False

    if input_open:
        if key == "ArrowUp":
            y_on = -1
        elif key == "ArrowDown":
            y_on = 1
        elif key == "ArrowRight":
            x_on = 1
        elif key == "ArrowLeft":
            x_on = -1
    print("x: ",x_on,"y: ",y_on)

def keyup(key: str):
    print("k")

def update():
    global dx,dy,verso

    
    game2d.canvas_fill((255,255,255))
    game2d.image_blit(image, (dx, dy))

    if (0 < dx < screen_x - 160 and x_on != 0) and (0 < dy < screen_y - 160 and y_on != 0):
        dx += 10 * x_on
        dy += 10 * y_on
        print("1^Ciclo Dy: ",dy,"Dx: ",dx)
    elif (dx == 0 or dx == screen_x - 160) and 0 < dy < screen_y - 160:
        dy += 10 * y_on
        print("2^Ciclo Dy: ",dy,"Dx: ",dx)
    elif (dy == 0 or dy == screen_x - 160) and 0 < dx < screen_x - 160:
        dx += 10 * x_on
        print("3^Ciclo Dy: ",dy,"Dx: ",dx)

def main():
    global key_block
    
    game2d.canvas_init((screen_x,screen_y))
    game2d.handle_keyboard(keydown, keyup)
    
    
    game2d.set_interval(update,1000//30)

if __name__ == "__main__":
    main()
