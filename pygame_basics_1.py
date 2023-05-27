import pygame
from sys import exit # we use this after line 12 so even the while loop stops

pygame.init() #we are initialsing everything in the pygame module think of it like starting a car

screen=pygame.display.set_mode((700,700))#  this is the main game screen also called the main surface upon which other sub surfaces are added these can be text or images
pygame.display.set_caption("runner")
clock=pygame.time.Clock()

test_surface=pygame.Surface((100,200))# creating a sub surface
test_surface.fill('Red')

while True:
    #in this infinite loop we make all visuals,animation and other changes and also parallely make changes corresponding to player input

    for event in pygame.event.get():# this is called the event loop and used to check for player inputs
        if event.type==pygame.QUIT:
            pygame.quit()# what this does is uninitialize all the initialized modules and bcuz even after uninitializing the while loop still runs pygame.display and thus throws an error
            exit()
    screen.blit(test_surface,(0,0))# blit(block image transfer) puts the sub surface on the main screen or surface
    # in pygame the origin is in the top left and to move down we increase y and to move left x
    # when we place the sub_surface on the main screen we place the top left of the sub_surface on the point specified on the 2nd arguement of blit

    pygame.display.update()  # it is used to update all the changes we have made and put it on the screen use after all changes have been made
    clock.tick(60)# basically telling that the while loop shall run 60 times per second or 60 fps(frames per second)