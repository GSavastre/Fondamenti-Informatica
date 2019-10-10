import game2d
import random

raggio = 50

cont = 0

game2d.canvas_init((500,500))
num_cerchi = int(input("Quanti cerchi vuoi disegnare ?"))

if num_cerchi >= 0:
    while cont < num_cerchi:
        
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)

        center_x = random.randint(0+raggio,500-raggio)
        center_y = random.randint(0+raggio,500-raggio)

        game2d.draw_circle((0,0,0),(center_x,center_y),(raggio+3))
        game2d.draw_circle((red,green,blue),(center_x,center_y),(raggio))
        
        cont += 1
else:
    print("Input non valido")
