import game2d

cont = 0
raggio = 250
centro_x = 250
centro_y = 250

rosso = 255

game2d.canvas_init((500,500))

num_cerchi = int(input("Quanti cerchi vuoi disegnare?(Max 250)"))


if num_cerchi >= 0 and num_cerchi <= 250:
    
    decremento_rosso = 255 // num_cerchi
    decremento_raggio = 250 // num_cerchi
    while cont < num_cerchi:

        game2d.draw_circle((rosso,0,0),(centro_x,centro_y),(raggio))
        rosso -= decremento_rosso
        raggio -= decremento_raggio

        cont += 1
else:
    print("Input non valido!")
