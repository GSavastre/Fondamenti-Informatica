import game2d

canvas_x = 500
canvas_y = 500

cell_x = 0
cell_y = 0

conta_x = 0
conta_y = 0


def main():

    global cell_x,cell_y,conta_x,conta_y
    
    game2d.canvas_init((canvas_x,canvas_y))
    rosso = verde = blu = 0

    colonne = int(input("Ok e quante colonne devo disegnare?"))
    righe = int(input("Quante righe devo disegnare?"))
   
    #Determino di quanto devo incrementare la posizione dei quadri e tolgo 1 px per il margine        
    incremento_x = canvas_x // colonne 
    incremento_y = canvas_y // righe 

    #Incrementi usati per avere sempre il quadrato (0,255,0) in basso sx il quad(0,0,255) in alto a dx e il quad(0,255,255)
    incremento_blu = 255 // (colonne - 1)
    incremento_verde = 255 // (righe - 1 )
    
  
    for conta_y in range(canvas_y // incremento_y):
        for conta_x in range(canvas_x // incremento_x):
            game2d.draw_rect((rosso,verde,blu),(cell_x,cell_y,incremento_x,incremento_y))
            cell_x += incremento_x + 1
            blu += incremento_blu
            conta_x += 1

        cell_x = 0
        conta_x = blu = 0
        cell_y += incremento_y + 1
        verde += incremento_verde
        conta_y += 1 

if __name__ == "__main__":
    main()
