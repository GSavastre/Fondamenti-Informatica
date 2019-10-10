import game2d
import random

game2d.canvas_init((500,500))

rosso = random.randint(0,255)
verde = random.randint(0,255)
blu = random.randint(0,255)

centro_x = 250
centro_y = 250

raggio = 250

while raggio >= 10:

    game2d.draw_circle((rosso,verde,blu),(centro_x,centro_y),(raggio))
    rosso = random.randint(0,255)
    verde = random.randint(0,255)
    blu = random.randint(0,255)
    raggio -= random.randint(0,raggio - 5)
