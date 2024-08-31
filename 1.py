import sys,os
import pygame
from pygame.locals import*

#게임의 색상 정의
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)

#게임시작 초기화
pygame.init()
#프레임 매니저 초기화
clock=pygame.time.Clock #파이게임의 time라이브러리에서 시계 클래스 이용해 객체 만듬
#프레임레이트
clock.tick(60)
#제목 표시줄 설정
pygame.display.set_caption('CRAZY DRIVER')
screen=pygame.display.set_mode((500,800))
screen.fill(WHITE)
#메이게임 루프
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()