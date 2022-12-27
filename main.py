import pygame as pg
from random import randint as rd

pg.init()

def draw_grid(scr):
    pg.draw.line(scr, (0, 0, 0), (100, 0), (100, 300), 3)
    pg.draw.line(scr, (0, 0, 0), (200, 0), (200, 300), 3)
    pg.draw.line(scr, (0, 0, 0), (0, 100), (300, 100), 3)
    pg.draw.line(scr, (0, 0, 0), (0, 200), (300, 200), 3)

def draw_tic_tac_toe(scr, items):
    for i in range(3):
        for j in range(3):
            if items[i][j] == '0':
                pg.draw.circle(scr, (255, 0, 0), (j * 100 + 50, i * 100 + 50), 45)
            elif items[i][j] == 'x':
                pg.draw.line(scr, (0, 0, 255), (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 3)
                pg.draw.line(scr, (0, 0, 255), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 3)

def get_win_check(fd, symbol):
    flag_win = False
    for line in fd:
        if line.count(symbol) == 3:
            flag_win = True
    for i in range(3):
        if fd[1][i] == fd[0][i] == fd[2][i] == symbol:
            flag_win = True
    if fd[0][0] == fd[1][1] == fd[2][2] == symbol:
        flag_win = True
    if fd[0][2] == fd[1][1] == fd[2][0] == symbol:
        flag_win = True
    return flag_win


screen_size = (300, 300)
window = pg.display.set_mode(screen_size)
screen = pg.Surface(screen_size)

pg.display.set_caption("Крестики нолики")
screen.fill((255, 255, 255))

field = [['', '', ''],
         ['', '', ''],
         ['', '', '']]
         
mainloop = True
game_over = False

while mainloop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mainloop = False

        if event.type == pg.MOUSEBUTTONDOWN and not game_over:
            pos = pg.mouse.get_pos()
            if field[pos[1] // 100][pos[0] // 100] == '':
                field[pos[1] // 100][pos[0] // 100] = 'x'
                x, y = rd(0, 2), rd(0, 2)
                while field[x][y] != '':
                    x, y = rd(0, 2), rd(0, 2)
                field[x][y] = '0'

            playr_win = get_win_check(field, 'x')
            ai_win = get_win_check(field, '0')

            if playr_win or ai_win:
                game_over = True
                if playr_win:
                    pg.display.set_caption('Вы победили')   
                else:
                     pg.display.set_caption('Компьютер победил')
            elif field[0].count('x') + field[0].count('0') + field[1].count('x') + \
                 field[1].count('0') + field[2].count('x') + field[2].count('0') == 8:
                pg.display.set_caption('Ничья')

    
    draw_tic_tac_toe(screen, field)
    draw_grid(screen)
    window.blit(screen, (0, 0))
    pg.display.update()
