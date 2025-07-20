import pygame as pg
from random import randint

class Pipe(pg.sprite.Sprite):
    def __init__(self,scale_factor,move_speed,p_distance):
        super(Pipe,self).__init__()
        self.img_up=pg.transform.scale_by(pg.image.load('assets/pipeup.png').convert_alpha(),scale_factor)
        self.img_down=pg.transform.scale_by(pg.image.load('assets/pipedown.png').convert_alpha(),scale_factor)
        self.rect_up=self.img_up.get_rect()
        self.rect_down=self.img_down.get_rect()
        self.p_distance=p_distance
        self.rect_up.y=randint(250,520)
        self.rect_up.x=600
        self.rect_down.x=600
        self.move_speed=move_speed
        self.rect_down.y=self.rect_up.y-self.p_distance-self.rect_up.height

    def drawPipe(self,win):
        win.blit(self.img_up,self.rect_up)
        win.blit(self.img_down,self.rect_down)

    def updatePipe(self,dlt_time):
        self.rect_up.x-=int(self.move_speed*dlt_time)
        self.rect_down.x-=int(self.move_speed*dlt_time)