
class musicPlayer():

	def __init__(self, song):
		import pygame
		pygame.mixer.init()
		self.mysong = song

	def play(self):
		pygame.mixer.music.load(self.mysong)
	
	
	

 





