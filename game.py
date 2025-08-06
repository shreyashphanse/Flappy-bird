import pygame as pg
import sys
import time
from bird import Bird
from pipe import Pipe


pg.init()

# sounds


class Game:
    def __init__(self):
        # window conif
        self.width = 600
        self.height = 700
        self.scale_factor=1.5
        self.win = pg.display.set_mode((self.width,self.height))
        self.setup_bg_and_ground()
        self.bird=Bird(self.scale_factor)
        self.is_enter_pressed=False
        self.clock=pg.time.Clock()
        self.move_speed=200
        self.is_game_started=True
        self.next_val=5

        # pipe contents
        self.pipe_list=[]
        self.pipe_generate_counter=80
        
        # self.d=[]
        # score elements
        self.dead_sound_played = False
        self.monitoring=False
        self.score=0

        # display score elements
        self.font=pg.font.Font('assets/font.ttf',24)
        self.score_text=self.font.render(f"Score:{self.score}",True,(255,255,255))
        self.score_text_rect=self.score_text.get_rect(center=(300,100))

        # restart button
        self.restart=self.font.render("RESTART",True,(0,0,0))
        self.restart_rect=self.restart.get_rect(center=(300,650))

        # display highscore
        self.highScore=[0]
        self.highScore1=self.highScore[0]
        self.highScore_text=self.font.render(f"High Score:{self.highScore1}",True,(0,255,0))
        self.highScore_text_rect=self.highScore_text.get_rect(center=(300,50))

        self.p_distance=150
        self.game_over=False

        pg.mixer.init()
        self.flap_sound=pg.mixer.Sound('assets/sfx/flap.wav')
        self.score_sound=pg.mixer.Sound('assets/sfx/score.wav')
        self.dead_sound=pg.mixer.Sound('assets/sfx/dead.wav')

        self.gameLoop()


    def gameLoop(self):
        last_time=time.time()
        while True:
            # calcukating delta time
            new_time=time.time()
            dlt_time=new_time-last_time
            last_time=new_time

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type== pg.KEYDOWN and self.is_game_started:
                    if event.key==pg.K_RETURN:
                        self.is_enter_pressed=True
                        self.bird.update_on=True
                    if event.key==pg.K_SPACE and self.is_enter_pressed:
                        self.bird.flap(dlt_time)
                        self.flap_sound.play()
                        
                if event.type==pg.MOUSEBUTTONDOWN:
                    if self.restart_rect.collidepoint(pg.mouse.get_pos()):
                        self.restartGame()
                if event.type== pg.KEYDOWN and not self.is_game_started:
                    if event.key==pg.K_RETURN:
                        self.restartGame()
                        
            self.updateEverything(dlt_time)
            self.checkCollision()
            self.checkScore()
            self.checkLevel()
            self.drawEverything()
            pg.display.update()
            self.clock.tick(60)

    def checkHighScore(self):
        self.highScore.append(self.score)
        if self.highScore:
            self.highScore.sort()
            if len(self.highScore)>1:
                for i in range(len(self.highScore)-1):
                    self.highScore.pop(0)
            self.highScore1=self.highScore[0]
            self.highScore_text=self.font.render(f"High Score:{self.highScore1}",True,(0,255,0))
            self.highScore_text_rect=self.highScore_text.get_rect(center=(300,50))

    def restartGame(self):
        self.checkHighScore()
        self.score=0
        self.score_text=self.font.render(f"Score:{self.score}",True,(255,255,255))
        self.is_enter_pressed=False
        self.is_game_started=True
        self.bird.resetPosition()
        self.pipe_list.clear()
        self.p_distance=150
        self.pipe_generate_counter=80
        self.bird.update_on=False
        self.next_val=5

    def checkLevel(self):
        if self.score >= self.next_val:
            self.p_distance = max(90, self.p_distance - 20)  # limit minimum distance
            self.next_val += 15
        # if self.score>5:
        #     self.score_val=self.score
        #     if self.score_val== self.next_val:
        #         self.p_distance-=100
        #         self.next_val+=5

    def drawEverything(self):
        self.win.blit(self.bg_img,self.bg_img_rect)
        self.win.blit(self.bg_img2,self.bg_img2_rect)
        # self.win.blit(self.bg_img1,self.bg_img1_rect)
        # self.win.blit(self.bg_img2,self.bg_img2_rect)
        # drawing pipes
        for pipe in self.pipe_list:
            pipe.drawPipe(self.win)
        self.win.blit(self.grnd_img1,self.grnd_img1_rect)
        self.win.blit(self.grnd_img2,self.grnd_img2_rect)
        self.win.blit(self.bird.image,self.bird.rect)
        self.win.blit(self.highScore_text,self.highScore_text_rect)
        self.win.blit(self.score_text,self.score_text_rect)

        
        if not self.is_game_started:
            self.win.blit(self.restart,self.restart_rect)

    def updateEverything(self,dlt_time):
        if self.is_enter_pressed:
            # for moving bg
            # self.bg_img1_rect.x-=int(self.move_speed*dlt_time)
            # self.bg_img2_rect.x-=int(self.move_speed*dlt_time)

            # if self.bg_img1_rect.right<0:
            #     self.bg_img1_rect.x=self.bg_img2_rect.right
            # if self.bg_img2_rect.right<0:
            #     self.bg_img2_rect.x=self.bg_img1_rect.right

            # for moving ground
            
            self.grnd_img1_rect.x-=int(self.move_speed*dlt_time)
            self.grnd_img2_rect.x-=int(self.move_speed*dlt_time)

            if self.grnd_img1_rect.right<0:
                self.grnd_img1_rect.x=self.grnd_img2_rect.right
            if self.grnd_img2_rect.right<0:
                self.grnd_img2_rect.x=self.grnd_img1_rect.right

            self.bg_img_rect.x-=int(((self.move_speed)-40)*dlt_time)
            self.bg_img2_rect.x-=int(((self.move_speed)-40)*dlt_time)

            if self.bg_img_rect.right<0:
                self.bg_img_rect.x=self.bg_img2_rect.right
            if self.bg_img2_rect.right<0:
                self.bg_img2_rect.x=self.bg_img_rect.right

            # generating pipes and appending them in the pipe list
            if self.pipe_generate_counter>90:
                self.pipe_list.append(Pipe(self.scale_factor,self.move_speed,self.p_distance))
                # self.d.append(1)
                # print(self.d)
                self.pipe_generate_counter=0
            self.pipe_generate_counter+=1
            for pipe in self.pipe_list:
                pipe.updatePipe(dlt_time)
            
            # removing the 1st pipe
            if len(self.pipe_list)!=0:
                if self.pipe_list[0].rect_up.right<0:
                    self.pipe_list.pop(0)
                    # self.d.pop(0)
                    # print(self.d)

            # self.checkCollision()
        self.bird.update(dlt_time)
        # print(self.score)
        # self.checkCollision()
        
    def setup_bg_and_ground(self):
        # setting background & ground img
        # self.bg_img=pg.transform.scale(pg.image.load('assets/bg.png').convert(),(600,1066))
        self.bg_img=pg.transform.scale_by(pg.image.load('assets/bg.png').convert(),self.scale_factor)
        self.bg_img2=pg.transform.scale_by(pg.image.load('assets/bg.png').convert(),self.scale_factor)
        # self.bg_img1=pg.image.load('assets/bg.png').convert()
        # self.bg_img2=pg.image.load('assets/bg.png').convert()
        self.grnd_img1=pg.transform.scale_by(pg.image.load('assets/ground.png').convert(),self.scale_factor)
        self.grnd_img2=pg.transform.scale_by(pg.image.load('assets/ground.png').convert(),self.scale_factor)

        # getting rectangle for bg
        self.bg_img_rect=self.bg_img.get_rect()
        self.bg_img2_rect=self.bg_img2.get_rect()
        # self.bg_img2_rect.x=self.bg_img1_rect.right

        # getting rectangle for both grnds
        self.grnd_img1_rect=self.grnd_img1.get_rect()
        self.grnd_img2_rect=self.grnd_img2.get_rect()

        # setting ground's x location
        self.grnd_img1_rect.x=0
        self.grnd_img2_rect.x=self.grnd_img1_rect.right

        self.bg_img_rect.x=0
        self.bg_img2_rect.x=self.bg_img_rect.right
        self.bg_img_rect.y=-300
        self.bg_img2_rect.y=-300

        # setting ground's y location
        # win_y=768 ,grnd_img_height=133*1.5=199.5 so we do y_cord=768-200=568
        self.grnd_img1_rect.y=568
        self.grnd_img2_rect.y=568

    def checkCollision(self):
        if len(self.pipe_list):
            if(self.bird.rect.bottom>568):
                self.bird.update_on=False
                self.is_enter_pressed=False
                self.is_game_started=False
                self.game_over=True
            if(self.bird.rect.colliderect(self.pipe_list[0].rect_up)
            or self.bird.rect.colliderect(self.pipe_list[0].rect_down)):
                # if((self.bird.rect.bottom>self.pipe_list[0].rect_up.top) or (self.bird.rect.top<self.pipe_list[0].rect_down.bottom)):
                #     self.is_enter_pressed=False
                #     self.bird.update_on=True
                self.is_enter_pressed=False
                self.is_game_started=False
                self.game_over=True
        if self.game_over==True:
            self.dead_sound.play()
            self.dead_sound.fadeout(75)
            # self.dead_sound.stop()
            self.game_over=False
            
        # if not self.dead_sound_played:
        #     self.dead_sound.play()
        #     self.dead_sound_played = True
        #     self.game_over = True
        # else:
        #     self.dead_sound_played = False
            
                
    def checkScore(self):
        if len(self.pipe_list)>0:
            if (self.bird.rect.left>self.pipe_list[0].rect_up.left and self.bird.rect.right<self.pipe_list[0].rect_up.right and not self.monitoring):
                self.monitoring=True
            if (self.bird.rect.right>self.pipe_list[0].rect_up.right and self.monitoring):
                self.monitoring=False
                self.score+=1
                self.score_sound.play()
                self.score_text=self.font.render(f"Score:{self.score}",True,(255,255,255))

# Add this variable at the top

# Inside your game loop, where collision is checked

    
      # reset if game is still active


game=Game()