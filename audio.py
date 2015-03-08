import pygame
import time

class musicPlayer(object):
    def __init__(self,song):
        pygame.mixer.init()
        pygame.mixer.music.load(song)

    def play(self):
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

if __name__ == '__main__':
    songpath = '/home/pi/audiocheck.net_BrownNoise_15min.mp3'

    mp = musicPlayer(songpath)
    mp.play()
    time.sleep(1)
    print pygame.mixer.music.get_busy()
    mp.stop()

