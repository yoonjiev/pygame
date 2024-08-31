import sys,os, random
import pygame
from pygame.locals import*
#이미지 폴더
GAME_ROOT_FOLDER=payh.dirname(__file__)
IMAGE_FOLDER=os.payh.join(GAME_ROOT_FOLDER,"Images")

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
#이미지 불러오기
IMG_ROAD=pygame.load(os.path.join(IMAGE_FOLDER,"Road.png"))
IMG_PLAYER=pygame.load(os.path.join(IMAGE_FOLDER,"PLAYER.png"))
IMG_ENEMY=pygame.load(os.path.join(IMAGE_FOLDER,"Enemy.png"))

#초기화
screen=pygame.display.set_mode(IMG_ROAD.get_size())
#게임 객체 플레이어 초기 위치
h=IMG_ROAD.get_width()//2
v=IMG_ROAD.get_height()-(IMG_PLAYER.get_height()//2)
#player스프라ㅣ트 
player=pygame.sprite.Sprite()
player.image= IMG_PLAYER
player.surf=pygame.Surface(IMG_PLAYER.get_size())
player.rect=player.surf.get_rect(center=(h,v))
#enemy
h1=IMG_ENEMY.get_width()//1 #가장 왼쪽
hr=IMG_ROAD.get_whidth()-(IMG_ENEMY.get_height()//2) #가장 오른쪽
h=random.randrage(h1,hr)
v=0
enemy=pygame.sprite.Sprite()
enemy.image= IMG_ENEMY
enemy.surf=pygame.Surface(IMG_ENEMY.get_size())
enemy.rect=enemy.surf.get_rect(center=(h,v))
"""
스프라이트: 컴퓨터 그래픽에서 큰 이미지 위에 노ㅎ이 2차원 이미지
스프라이트는 표시하거나 숨길 수 있고 움직이거나 회전 변형가능 
자동차는 스프라이트로 만듬
"""


screen.fill(WHITE)
#메이게임 루프
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    #배경 플레이처 적 이미지
    screen.blit(IMG_ROAD,(0,0))
    screen.blit(IMG_PLAYER,player.rect)
    screen.blit(IMG_ROAD,enemy.rect)
    

    pygame.display.update()