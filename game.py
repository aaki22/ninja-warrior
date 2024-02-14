import pygame
import sys

pygame.init()

WIDTH=640
HEIGHT=480

screen=pygame.display.set_mode((WIDTH,HEIGHT))

clock=pygame.time.Clock()


while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	clock.tick(60)
