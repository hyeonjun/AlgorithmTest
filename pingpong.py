import pygame
import sys
import random
import math
from pygame.locals import *

class Block:
    def __init__(self,col,rect):
        self.col = col
        self.rect = rect

    def draw_E(self):
        pygame.draw.ellipse(SURFACE, self.col, self.rect)
    def draw_R(self):
        pygame.draw.rect(SURFACE,self.col,self.rect)

pygame.init()
pygame.key.set_repeat(1,1)
WIDTH =800
HEIGHT = 600
SURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
FPSCLOCK = pygame.time.Clock()
Bigfont = pygame.font.SysFont(None, 80)
Smallfont = pygame.font.SysFont(None, 30)

def main():
    #변수설정
    game_over = 0
    P1_Score = 0
    P2_Score = 0

    #게임 공의 속도와 패들을 설정
    BALL_xspeed = 5
    BALL_yspeed = 5
    PADDLE_1 = Block((0, 255, 0), Rect(0, HEIGHT / 2 - 20, 20, 80))
    PADDLE_2 = Block((0, 255, 0), Rect(780, HEIGHT / 2 - 20, 20, 80))
    BALL = Block((255, 255, 255), Rect(WIDTH / 2, HEIGHT / 2, 20,20))



    M_P1 = Bigfont.render("P1 Win!!", True, (255, 255, 255))
    M_P2 = Bigfont.render("P2 Win!!", True, (255, 255, 255))
    while True:
        SURFACE.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    PADDLE_1.rect.centery -= 1
                elif event.key == K_s:
                    PADDLE_1.rect.centery += 1
                elif event.key == K_UP:
                    PADDLE_2.rect.centery -= 1
                elif event.key == K_DOWN:
                    PADDLE_2.rect.centery += 1


        # 승리한 사람 구분하기
        if game_over == 0 :
            if P1_Score >= 5:
                game_over = 1 # P1의 승리
            if P2_Score >= 5:
                game_over = 2 # P2의 승리

            # 볼 움직이기
            BALL.rect.centerx += BALL_xspeed
            BALL.rect.centery -= BALL_yspeed

            #볼과 벽의 충돌
            if BALL.rect.centerx < 0:
                P2_Score += 1
                BALL_xspeed = 5
                BALL_yspeed = 5
                BALL.rect.center = (400,300)
                PADDLE_1.rect.center = (10,HEIGHT/2-20)
                PADDLE_2.rect.center = (790, HEIGHT/2 - 20)
                BALL.rect.centerx += BALL_xspeed
                BALL.rect.centery -= BALL_yspeed

            elif BALL.rect.centerx > 800:
                P1_Score += 1
                BALL_xspeed = 5
                BALL_yspeed = 5
                BALL.rect.center = (400, 300)
                PADDLE_1.rect.center = (10, HEIGHT/2 - 20)
                PADDLE_2.rect.center = (790, HEIGHT/2 - 20)
                BALL.rect.centerx += BALL_xspeed
                BALL.rect.centery -= BALL_yspeed

            if BALL.rect.centery < 0 or BALL.rect.centery >600:
                BALL_yspeed *= -1

            # 패들과 공이 부딪힘
            if PADDLE_1.rect.colliderect(BALL.rect):
                BALL.rect.left = PADDLE_1.rect.right
                BALL_xspeed *= -1.05
                if BALL.rect.centery <= PADDLE_1.rect.top or BALL.rect.centery > PADDLE_1.rect.bottom:
                    BALL_yspeed *= -1.05
            elif PADDLE_2.rect.colliderect(BALL.rect):
                BALL.rect.right = PADDLE_2.rect.left
                BALL_xspeed *= -1.05
                if BALL.rect.centery <= PADDLE_2.rect.top or BALL.rect.centery > PADDLE_2.rect.bottom:
                    BALL_yspeed *=  -1.05


            # 패들을 화면 밖으로 못나가게하기
            if PADDLE_1.rect.centery <0:
                PADDLE_1.rect.centery = 0
            elif PADDLE_1.rect.centery >600:
                PADDLE_1.rect.centery = 600
            if PADDLE_2.rect.centery <0:
                PADDLE_2.rect.centery = 0
            elif PADDLE_2.rect.centery >600:
                PADDLE_2.rect.centery = 600
            M_P1_S = Smallfont.render("P1 : {}".format(P1_Score), True, (255, 255, 255))
            M_P2_S = Smallfont.render("P2 : {}".format(P2_Score), True, (255, 255, 255))
            M_SPEED = Smallfont.render("SPEED : %.2f"%abs(BALL_xspeed),True,(255,255,255))
            SURFACE.blit(M_P1_S,(10,30))
            SURFACE.blit(M_P2_S,(740,30))
            SURFACE.blit(M_SPEED,(350,30))
            #도형 그리기
            PADDLE_1.draw_R()
            PADDLE_2.draw_R()
            BALL.draw_E()
        elif game_over == 1:
            SURFACE.blit(M_P1,(300,300))
        elif game_over == 2:
            SURFACE.blit(M_P2,(300,300))
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()