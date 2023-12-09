import pygame
from sys import exit
from random import randint,choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1=pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()    #player1
        player_walk_2=pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()    #player2

        self.player_walk=[player_walk_1,player_walk_2]
        self.player_index=0
        self.player_jump=pygame.image.load('graphics/Player/jump.png').convert_alpha() 

        self.image = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(80,300))
        self.gravity=0
       
        self.jump_sound =  pygame.mixer.Sound('audio\jump.mp3')
        self.jump_sound.set_volume(0.5 )    

         
   

    def player_input(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom>=300:
            self.gravity=-15
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 0.7
        self.rect.y += self.gravity
        if self.rect.bottom >=300:
            self.rect.bottom=300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index +=0.1
            if self.player_index >= len(self.player_walk):self.player_index=0
            self.image=self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()        
        self.apply_gravity() 
        self.animation_state()       

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'fly':
            fly_surface_1=pygame.image.load('graphics\Fly\Fly1.png').convert_alpha()
            fly_surface_2=pygame.image.load('graphics\Fly\Fly2.png').convert_alpha()
            self.frames=[fly_surface_1,fly_surface_2]
            y_pos=210
        else:
            snail_surface_1=pygame.image.load('graphics\snail\snail1.png').convert_alpha()           #snail
            snail_surface_2=pygame.image.load('graphics\snail\snail2.png').convert_alpha()           #snail
            self.frames = [snail_surface_1,snail_surface_2]
            y_pos=300

        self.animation_index=0    
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900,1100),y_pos))

        self.speed=5
    
    def animation_state(self):
        self.animation_index +=0.1
        if self.animation_index >= len(self.frames): self.animation_index=0
        self.image=self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state() 
        self.speed +=0.1
        self.rect.x -= self.speed   
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= randint(5,8)
            
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface_1,obstacle_rect)
            else:
                screen.blit(fly_surf,obstacle_rect)    
        
        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-100]  #will copy item in obstac;e_list if item is not a lot far
        
        return obstacle_list    
        
    else:
        return []
    
def display_score():
    current_time=pygame.time.get_ticks() -start_time
    current_time=int(current_time/1000)
    score_surf=test_font.render(f'Score : {current_time}',False,(64,64,64))
    score_rect=score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    return current_time
    # print(current_time)

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                i=0
                j=0 
                while i!=100000:
                    while j!=1000000:
                        # screen.blit(player_stand,player_rect)
                        j+=1
                    i+=1

                return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else:
        return True
def player_animation():
    #walk if on floor
    #jump if above floor
    global player_surf,player_index

    if player_rect.bottom<300:
        #jump
        player_surf = player_jump
    else:
        player_index +=0.1
        if player_index >=len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]
        #walk    
  


pygame.init()
screen=pygame.display.set_mode((800,400))
screen.fill('white')
pygame.display.set_caption('Runner')
clock=pygame.time.Clock()
test_font=pygame.font.Font('font\Pixeltype.ttf',50)

snail_x_pos=700
pos_player=10
posy=220
sub=5
player_gravity=0
game_active=False
start_time=0
score=0


bg_Music = pygame.mixer.Sound('audio\music.wav')
bg_Music.set_volume(0.5)
bg_Music.play(loops=-1)
player=pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group= pygame.sprite.Group()


sky_surface=pygame.image.load('graphics\Sky.png').convert_alpha()                       #sky
ground_surface=pygame.image.load('graphics\ground.png').convert_alpha()

player_walk_1=pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()    #player1
player_walk_2=pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()    #player2
player_walk=[player_walk_1,player_walk_2]
player_index=0
player_jump=pygame.image.load('graphics/Player/jump.png').convert_alpha() 

player_surf=player_walk[player_index]

player_rect=player_surf.get_rect(midbottom=(40,300))

player_jump=pygame.image.load('graphics/Player/jump.png').convert_alpha()    #player2

# Intro Screen
player_stand=pygame.image.load('graphics\Player\player_stand.png').convert_alpha()
player_stand=pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect=player_stand.get_rect(center=(400,200))


# score_surf=test_font.render('My first Game',False,(64,64,64)).convert_alpha()               #score
# score_rect=score_surf.get_rect(midbottom=(400,50))

over_surf=test_font.render(' Game Over',False,(64,64,64)).convert_alpha()               #score
over_rect=over_surf.get_rect(midbottom=(400,50))

game_name=test_font.render('Pixel Runner',False,(111,196,169))
game_name_rect=game_name.get_rect(midbottom=(400,80))

game_message=test_font.render('Press Spacebar to Run',False,(111,196,169))
game_message_rect=game_message.get_rect(midbottom=(400,360))

# obstacles
snail_surface_1=pygame.image.load('graphics\snail\snail1.png').convert_alpha()           #snail
snail_surface_2=pygame.image.load('graphics\snail\snail2.png').convert_alpha()           #snail
snail_frames = [snail_surface_1,snail_surface_2]
snail_frame_index=0
snail_surf=snail_frames[snail_frame_index]

fly_surface_1=pygame.image.load('graphics\Fly\Fly1.png').convert_alpha()
fly_surface_2=pygame.image.load('graphics\Fly\Fly2.png').convert_alpha()
fly_frames=[fly_surface_1,fly_surface_2]
fly_frame_index=0
fly_surf=fly_frames[fly_frame_index]

obstacle_rect_list = []

# snail_surface2=pygame.image.load('graphics\snail\snail2.png').convert_alpha()           #sanil2
# snail_rect_2=snail_surface2.get_rect(midbottom=(700,300))

obstacle_timer=pygame.USEREVENT +1    
pygame.time.set_timer(obstacle_timer,1000)                #if any event happen in 900 msecs record or do shit

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        # if event.type==pygame.MOUSEMOTION:                #makes gra=-20 if mouse touch palyer rect             
        #     if player_rect_1.collidepoint(event.pos):
        #         player_gravity=-20

        if game_active:
            if event.type==pygame.MOUSEBUTTONDOWN :                #makes gra=-20 if mouse touch palyer rect             
                if player_rect.collidepoint(event.pos) and player_rect.bottom>=300:
                    player_gravity=-18

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom>=300:
                    player_gravity=-15

            if event.type == obstacle_timer :
                obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
                # if randint(0,2):
                #     obstacle_rect_list.append(snail_surface_1.get_rect(midbottom=(randint(900,1100),300)))
                # else:
                #     obstacle_rect_list.append(fly_surf.get_rect(midbottom=(randint(900,1100),150))) 

            if event.type == snail_animation_timer:
                if snail_frame_index==0:snail_frame_index=1
                else: snail_frame_index=0
                snail_surf=snail_frames[snail_frame_index]           
            
            if event.type == fly_animation_timer:
                if fly_frame_index==0 : fly_frame_index=1
                else: fly_frame_index=0
                fly_surf=fly_frames[fly_frame_index]

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active=True

                # bg_Music.play()
                
                # snail_rect.left=800
                start_time=pygame.time.get_ticks()



    if game_active:
        screen.blit(sky_surface,(0,0))                                       #sky
        screen.blit(ground_surface,(0,300))                                  #ground
        score = display_score()
        # if player_gravity>20:
        #     player_gravity=-20
        
        # player_gravity +=0.7
        # player_rect.y +=player_gravity
        # if player_rect.bottom>=300:player_rect.bottom=300
        # player_animation()
        # screen.blit(player_surf,player_rect)
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active=collision_sprite()
        #obstacle movement
        # obstacle_rect_list=obstacle_movement(obstacle_rect_list)

        # game_active=collisions(player_rect,obstacle_rect_list)

        # if player_rect_1.bottom<300:                       #animation change on jump
        #     screen.blit(player_jump,player_rect_1 )        #just use tht player rectangle
        # else:
        #     screen.blit(player_walk_1,player_rect_1) 

        
        

        # if player_rect_2.left%5==0:                                          #player
        #     screen.blit(player_walk_1,player_rect_1)  
        # else:
        #     screen.blit(player_walk_2,player_rect_2)

                                                                            #snail

        # screen.blit(snail_surface1,snail_rect_1)              #prev snail walk logic 
        # if snail_rect_1.left <-100:snail_rect_1.left =800
        # snail_rect_1.x -=6


        # pygame.draw.rect(screen,'#c0e8ec',score_rect) 
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10,8) 
        # screen.blit(score_surf,score_rect)
        # pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(),10)   #drawsa line following th emouse

                                            #score
        # if player_rect_2.left>800: player_rect_2.left=-100
        # if player_rect_1.left>800: player_rect_1.left=-100

        
        
        # keys=pygame.key.get_pressed()             #output if space pressed
        # if keys[pygame.K_SPACE]:
        #     print('jump')
        
        # player_rect_1.x +=4
        # player_rect_2.x +=4

        # if player_rect_1.colliderect(snail_rect_1):
        #     print('snail aya')
        # else:
        #     print('snail gaya------')     


        # if posy%20==0:
        #     sub=sub*-1  
        # posy=posy+sub
        # if player_rect_1.colliderect(snail_rect_1):
        #     print('collision')
        # else:
        #     print('none')
        
        # collision
        # if snail_rect_1.colliderect(player_rect_1):
        #     game_active=False
            # screen.blit(over_surf,score_rect)
            # pygame.quit()
            # exit()
    else:
        screen.fill((94,129,162))
        screen.blit(game_name,game_name_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom=(80,300)
        player_gravity=0

        score_message=test_font.render(f'Your Score : {score}',False,(111,196,169))
        score_message_rect=score_message.get_rect(center=(400,330))
        if score==0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)
        screen.blit(player_stand,player_stand_rect)        

    pygame.display.update()
    clock.tick(60)