import pygame

pygame.init()

pygame.mixer.music.load('estouaqui.mp3')
pygame.mixer.music.play()
pygame.event.wait()
