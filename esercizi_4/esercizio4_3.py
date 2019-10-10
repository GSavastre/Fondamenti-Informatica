import game2d

def sierpiski(livello, x0, y0, w, h):
    ws = w // 2
    hs = h // 2
    if livello == 0 or ws == 0 or hs == 0:
        return
    for x in range(2):
        for y in range(2):
            xs = x0 + x * ws
            ys = y0 + y * hs
            if x == 1 and y == 0:
                game2d.draw_rect((255,255,255),(xs,ys,ws,hs))
            else:
                sierpiski(livello - 1, xs, ys, ws, hs)
    
        


screen = 400

livello = int(input("A quale livello vuoi arrivare? "))

game2d.canvas_init((screen, screen))
game2d.canvas_fill((0,0,0))
w = h = screen

sierpiski(livello, 0, 0, w, h)
