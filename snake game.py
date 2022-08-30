#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:12605
# datetime:2022/7/20 10:01
# file: snake 2.py
# software: PyCharm
import pygame
import sys
import random
from pygame.locals import *

redColor = pygame.Color(255,0,0)
whiteColor = pygame.Color(255,255,255)
blackColor = pygame.Color(0,0,0)

def main():
    pygame.init()
    fps = pygame.time.Clock()
    playSurface = pygame.display.set_mode((640,480))
    pygame.display.set_caption("snake game")
    eatenFlag = 1
    snakebody = [[100,100],[80,100],[60,100]]
    snakePosition = [100,100]
    targetposition = [300,300]
    direction = "right"
    changeDirection = direction
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirection = "right"
                if event.key == K_LEFT:
                    changeDirection = "left"
                if event.key == K_UP:
                    changeDirection = "up"
                if event.key == K_DOWN:
                    changeDirection = "down"
        if changeDirection == "left" and not direction == "right":
            direction = changeDirection
        if changeDirection == "right" and not direction == "left":
            direction = changeDirection
        if changeDirection == "up" and not direction == "down":
            direction = changeDirection
        if changeDirection == "down" and not direction == "up":
            direction = changeDirection


        if direction == "right":
            snakePosition[0] += 20
        if direction == "left":
            snakePosition[0] -= 20
        if direction == "up":
            snakePosition[1] -= 20
        if direction == "down":
            snakePosition[1] += 20

        if snakePosition in snakebody:
            pygame.quit()
            sys.exit()

        snakebody.insert(0,list(snakePosition))

        if snakePosition[0] == targetposition[0] and snakePosition[1] == targetposition[1]:
            eatenFlag = 0

        else:
            snakebody.pop()
        if eatenFlag == 0:

            x = random.randrange(1,32)
            y = random.randrange(1,24)

            targetposition = [int(x*20),int(y*20)]
            eatenFlag = 1

        if snakePosition[0] > 640 or snakePosition[0] < 0 or snakePosition[1] > 480 or snakePosition[1] < 0:
            pygame.quit()
            sys.exit()


        playSurface.fill(blackColor)
        # 左上角是0，0，后面是宽和高


        for position in snakebody:
            pygame.draw.rect(playSurface, whiteColor, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(playSurface, redColor, Rect(targetposition[0], targetposition[1], 20, 20))

        # flip不断刷新界面
        pygame.display.flip()
        fps.tick(2)
if __name__ == "__main__":
  main()