import pygame

class PhysicsEntity:
	def def __init__(self, game,e_type,pos,size):
	    self.game=pygame
	    self.type=e_type
	    self.pos=list(pos)
	    self.size=size
	    self.velocity=[0,0]

	    def update(self,game,movement=[0,0]):
	    	frame_movement=(self.movement[0]+self.velocity[0],self.movement[1]+self.velocity[1])

	    	self.pos[0]=self.frame_movement[0]
	    	self.pos[1]=self.frame_movement[1]

	    def render(self,surf):
	    	surf.blit(self.game.assests['player'],self.pos)