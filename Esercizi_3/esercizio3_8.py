import actors, game2d

screen_x = screen_y = 500

radius = 15

second_ball_distance = 3 * radius


balls = []

def keydown(key: str):
    
    if key == "ArrowRight":
            balls[0].go_right()
    elif key == "ArrowLeft":
            balls[0].go_left()
    elif key == "ArrowUp" or key == "ArrowDown":
            balls[0].stay()
    elif key == "KeyD":
            balls[1].go_right()
    elif key == "KeyA":
            balls[1].go_left()
    elif key == "KeyW" or key == "KeyS":
            balls[1].stay()
            
def keyup(key: str):
    return None


def update():
    game2d.canvas_fill((255,255,255))
    
    for b in balls:
        b.move(True, True, True)
        x, y, r = b.get_coord()        
        game2d.draw_circle((0,0,0),(x,y),(r+2))
        game2d.draw_circle((b.getter()),(x,y),(r))

def main():
    global balls
    arena = actors.Arena(screen_x, screen_y)
    balls.append(actors.Ball(0 + radius,arena.get_size()[1]//2,radius,arena))
    balls.append(actors.Ball(0 + radius + second_ball_distance,
                             arena.get_size()[1]//2,radius,arena))

    game2d.handle_keyboard(keydown, keyup)
    game2d.canvas_init((arena.get_size()))
    game2d.set_interval(update, 1000//30)

if __name__ == "__main__":
    main()
