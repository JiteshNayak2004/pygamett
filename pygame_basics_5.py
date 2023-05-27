import pygame
from sys import exit # we use this after line 12 so even the while loop stops

def display_score():
    current_time=int(pygame.time.get_ticks()/1000)-start_time
    # gives us time in milliseconds after pygame.init is called  but even after game restarts time does'nt start from first so what we do is we subtract the time 
    #of the previous play check line 61 

    score_surface=test_font.render(f'{current_time}',False,(64,64,64))
    score_rect=score_surface.get_rect(center=(600,50))
    screen.blit(score_surface,score_rect)


pygame.init() #we are initialsing everything in the pygame module think of it like starting a car

screen=pygame.display.set_mode((800,400))#  this is the main game screen also called the main surface upon which other sub surfaces are added these can be text or images
pygame.display.set_caption("runner")
clock=pygame.time.Clock()
test_font=pygame.font.Font('font/Pixeltype.ttf',50)# the first arguement is the font type and the second is the font size
game_active=True
start_time=0

sky_surface=pygame.image.load('graphics/Sky.png')# we store the png image as a surface
ground_surface=pygame.image.load('graphics/ground.png')
text_surface=test_font.render('my game', False , 'Black')# first arg is text second is anti-aliasing(makes edges of pixelloid text smooth) and third is the colour
#in pygame u can't directly display a text u write the text into a surface and blit it onto main screen
player_surface=pygame.image.load('graphics\Player\player_walk_1.png')
player_rect=player_surface.get_rect(midleft=(80,260))
player_gravity=0

snail_surface=pygame.image.load('graphics/snail/snail1.png')
snail_rect=snail_surface.get_rect(bottomright=(600,300))
#as placing sub_surfaces from the top left is not convenient we enclose the image with a rectangle
#and we can use the points of the rectangle like mid left, top right , center etc to place it conveniently
#and use it in blit function to position the image accurately



while True:
    #in this infinite loop we make all visuals,animation and other changes and also parallely make changes corresponding to player input

    for event in pygame.event.get():# this is called the event loop and used to check for player inputs
        if event.type==pygame.QUIT:
            pygame.quit()# what this does is uninitialize all the initialized modules and bcuz even after uninitializing the while loop still runs pygame.display and thus throws an error
            exit()
        if game_active:    
            if event.type==pygame.MOUSEBUTTONDOWN and player_rect.bottom>=300:# to check whether any button was placed in the first place
                if player_rect.collidepoint(event.pos):# if button pressed owrk with a specific key
                    player_gravity=-20

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and player_rect.bottom>=300:# we use the second condition so that player can jump only when it touches the ground
                    player_gravity=-20                                                                     #and if we would'nt do this the player could jump infinitely and go beyond the up part of the screen
        else:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_active=True
                    # now there is a problem when we try to restart the game the snail and player have collided and we have to keep pressing spacebar until the snail rectangle
                    #and the player rectangle have crossed each other to fix this we also make the snail to go to the right of the screen
                    snail_rect.left=800 
                    start_time=int(pygame.time.get_ticks()/1000)
    


    if game_active:# we do this because when the player looses we want the game_over state to be displayed 

        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        screen.blit(text_surface,(300,50))
        # blit(block image transfer) puts the sub surface on the main screen or surface
        # in pygame the origin is in the top left and to move down we increase y and to move left x
        # when we place the sub_surface on the main screen we place the top left of the sub_surface on the point specified on the 2nd arguement of blit

        pygame.draw.rect(screen,'Pink',player_rect)#we use this method to draw figures and fill in colours in them first arg where u wana draw 2nd color and 3rd \
        #is which rectangle to draw

        screen.blit(snail_surface,snail_rect)
        snail_rect.left=snail_rect.left-4
        if snail_rect.right<=0: snail_rect.left=800# so that snal reappears in the screen after crossing the border
        # what we do is we grab a point on the rectangle and move it
        #generally we don't move the surface we move the rectangle that encloses the surface

        player_gravity=player_gravity+1# incrementing the gravity
        player_rect.y=player_rect.y+player_gravity#we add the increment gravity to the y coordinate of the rectangle and thus the rectangle or the player falls down
        if player_rect.bottom>=300: player_rect.bottom=300# we do this so that the player doesn't fall below the ground
        screen.blit(player_surface,player_rect)# we can pass the rectangle as an arguement

        if snail_rect.colliderect(player_rect):# condition for the game to be over
            game_active=False

    else:# game over state where we can ask the player to start the game again or quit
        screen.fill('Yellow')



    display_score()
    pygame.display.update()  # it is used to update all the changes we have made and put it on the screen use after all changes have been made
    clock.tick(60)# basically telling that the while loop shall run 60 times per second or 60 fps(frames per second)
    