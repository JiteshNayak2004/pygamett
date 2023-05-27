import pygame
from sys import exit # we use this after line 12 so even the while loop stops

pygame.init() #we are initialsing everything in the pygame module think of it like starting a car

screen=pygame.display.set_mode((800,400))#  this is the main game screen also called the main surface upon which other sub surfaces are added these can be text or images
pygame.display.set_caption("runner")
clock=pygame.time.Clock()
test_font=pygame.font.Font('font/Pixeltype.ttf',50)# the first arguement is the font type and the second is the font size

sky_surface=pygame.image.load('graphics/Sky.png')# we store the png image as a surface
ground_surface=pygame.image.load('graphics/ground.png')
text_surface=test_font.render('my game', False , 'Black')# first arg is text second is anti-aliasing(makes edges of pixelloid text smooth) and third is the colour
#in pygame u can't directly display a text u write the text into a surface and blit it onto main screen
player_surface=pygame.image.load('graphics\Player\player_walk_1.png')
player_rect=player_surface.get_rect(midleft=(80,260))

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
        if event.type==pygame.MOUSEMOTION:
            #this if checks whether mouse is moved and if yes we can call or do something
            if player_rect.collidepoint(event.pos):
                print('collision')#replicating what we did in line no 57 and 58


    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    # blit(block image transfer) puts the sub surface on the main screen or surface
    # in pygame the origin is in the top left and to move down we increase y and to move left x
    # when we place the sub_surface on the main screen we place the top left of the sub_surface on the point specified on the 2nd arguement of blit

    screen.blit(snail_surface,snail_rect)
    snail_rect.left=snail_rect.left-1
    if snail_rect.right<=0: snail_rect.left=800# so that snal reappears in the screen after crossing the border

    screen.blit(player_surface,player_rect)# we can pass the rectangle as an arguement
    player_rect.left=player_rect.left+2
     # what we do is we grab the left of the rectangle and move it
    #generally we don't move the surface we move the rectangle that encloses the surface

    if player_rect.colliderect(snail_rect):
        print("collisison")
         # used to check whether player_rect collides with snail_rect and we can perform some functiont then

    a=pygame.mouse.get_pos()

    if player_rect.collidepoint(a):
        print('collision')
        # what we do here is to check whether the rectangle collides with a point and here it is the cursor of the mouse for instance
        #we can do the same in event loop


        


    pygame.display.update()  # it is used to update all the changes we have made and put it on the screen use after all changes have been made
    clock.tick(60)# basically telling that the while loop shall run 60 times per second or 60 fps(frames per second)