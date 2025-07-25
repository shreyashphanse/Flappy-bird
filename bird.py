import pygame as pg
import time

class Bird(pg.sprite.Sprite):
    # initialize the constructor for the Bird class using super
    def __init__(self,scale_factor):
        super(Bird,self).__init__()
        self.img_list=[
            pg.transform.scale_by(pg.image.load('assets/birdup.png').convert_alpha(),scale_factor),
            pg.transform.scale_by(pg.image.load('assets/birddown.png').convert_alpha(),scale_factor)
            ]
        self.image_index=0
        self.image=self.img_list[self.image_index]
        self.rect=self.image.get_rect(center=(100,100))
        # setting gravity and velocity
        self.y_velocity=0
        self.gravity=25
        self.flap_speed=250
        self.anim_counter=0
        self.update_on=False

    def update(self,dlt_time):
        if self.update_on:
            self.playAnimation()
            self.apply_gravity(dlt_time)
            self.rotate()

            if self.rect.y<=0 and self.flap_speed==250:
                self.rect.y=0
                self.flap_speed=0
                self.y_velocity=0
            elif self.rect.y>0 and self.flap_speed==0:
                self.flap_speed=250

    
    def apply_gravity(self,dlt_time):
        self.y_velocity+=self.gravity*dlt_time
        self.rect.y+=self.y_velocity

    def flap(self,dlt_time):
        self.y_velocity=-self.flap_speed*dlt_time*1.3

    def playAnimation(self):
        if self.anim_counter==6:
            self.image=self.img_list[self.image_index]
            if self.image_index==0:self.image_index=1
            else: self.image_index=0
            self.anim_counter=0
        self.anim_counter+=1
        
    def resetPosition(self):
        self.rect.center=(100,100)
        self.y_velocity=0
        self.anim_counter=0

    def rotate(self):
        # Limit the angle to a reasonable range
        angle = max(min(-self.y_velocity * 5, 25), -90)  # tilt up to -90°, down to 25°
        self.image = pg.transform.rotate(self.img_list[self.image_index], angle)
        # Keep center consistent after rotation
        self.rect = self.image.get_rect(center=self.rect.center)
