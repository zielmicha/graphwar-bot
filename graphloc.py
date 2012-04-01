from __future__ import division
import pygame
import os
import sys
import time
import threading

import graphbot

winid = '0x3a00007'
winid = '0x3c00007'

def grab():
    status = os.system('import -windowid %s /tmp/img.png' % winid)
    if status == 2:
        sys.exit('ctrl-c')
    if status != 0:
        print('failed')
    return pygame.image.load('/tmp/img.png').convert()

wnd = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Graphwar bot by zielmicha')

grab_img = grab()

def grab_T():
    while True:
        global grab_img
        grab_img = grab()

threading.Thread(target=grab_T).start()


f_start = (14, 14)
f_end = (784, 464)
f_zero = (399, 240)

f_x = f_zero[0] - f_start[0]
f_y = f_zero[1] - f_start[1]

x_range = 25
y_range = 15

pts = []
ptsr = []

pygame.scrap.init()

pygame.font.init()
font = pygame.font.Font(None, 25)

fun = ''
while True:
    fun = fun[:int(len(fun) * 0.9)]
    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos = ev.pos[0] - f_zero[0], ev.pos[1] - f_zero[1]
            pos = pos[0] / f_x * x_range, -pos[1] / f_y * y_range
            pts.append(pos)
            ptsr.append(ev.pos)
            print pos, ev.pos
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
            if len(pts) >= 2:
                print
                try:
                    fun = graphbot.polygon(pts)
                except Exception as err:
                    fun = str(err)
                print fun
                pygame.scrap.put(pygame.SCRAP_TEXT, fun)
                print
            else:
                print 'no points...'
            pts = []
            ptsr = []
        if ev == pygame.QUIT:
            sys.exit()

    wnd.blit(grab_img, (0,0))
    for p in ptsr:
        wnd.fill((255,0,0), (p[0]-2, p[1]-2, 4,4))
    wnd.blit(font.render(fun[:110], 1, (255, 0, 0)), (0,0))
    pygame.display.flip()
    time.sleep(0.1)
