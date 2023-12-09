import pygame
from sys import exit
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

sky_surface=pygame.image.load('graphics\Sky.png').convert_alpha()
ground_surface=pygame.image.load('graphics\ground.png').convert_alpha()

player_surf=pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect=player_surf.get_rect(midbottom=(40,300))



test_font=test_font.render('My first Game',False,'black').convert_alpha()

snail_surface1=pygame.image.load('graphics\snail\snail1.png').convert_alpha()
snail_rect=snail_surface1.get_rect(midbottom=(800,300))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom>=300:
                    player_gravity=-20

    
    
    if  snail_rect.x ==100:
         player_gravity=-20

    print(f"player : {player_rect.midbottom}" )
    print(f"snail : {snail_rect.midbottom}" )
    player_gravity +=1
    player_rect.y +=player_gravity
    if player_rect.bottom>=300:player_rect.bottom=300

    screen.blit(sky_surface,(0,0))                                       #sky
    screen.blit(ground_surface,(0,300))                                  #ground

                                             #player
    screen.blit(player_surf,player_rect)  
    

                                                    #snail
    screen.blit(snail_surface1,snail_rect)    
    

    if snail_rect.x<-100: snail_rect.x=800
    # if pos_player>800: pos_player=-100
    snail_rect.x=snail_rect.x-4
    # pos_player=pos_player+4

    # if posy%20==0:
    #     sub=sub*-1  
    # posy=posy+sub
    
    pygame.display.update()
    clock.tick(60)