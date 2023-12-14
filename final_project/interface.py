import pandas as pd
import numpy as np
import pygame
from pygame.locals import *
import pygame.mixer as mixer
global activeID
global playingnotes
activeID = None
playingnotes = False
# bounce 16 bit
# lowest sample rate
# non normalized audio
# 1 1 1 1 to 1 3 1 1
# ===== Sounds =====
# C4 = 60
# C5 = 72
mixer.init()

class Note(pygame.sprite.Sprite):
    def __init__(self, pic, x, y, id):
        super().__init__()
        self.pic = pygame.image.load(pic)
        self.pic = pygame.transform.scale(self.pic, (35, 70))
        self.rect = self.pic.get_rect()
        self.rect.move_ip(x, y)
        self.isActive = False
        self.id = id
        self.noteVal = 60

    def toggleActive(self):
        self.isActive = not self.isActive
        if self.isActive == True:
            mixer.Sound.play(mixer.Sound("final_project/assets/" + str(self.noteVal) + ".wav"))
            global activeID
            activeID = self.id
            self.pic = pygame.image.load("final_project/assets/qn-active.png")
        else:
            self.pic = pygame.image.load("final_project/assets/qn.png")
        self.pic = pygame.transform.scale(self.pic, (35, 70))

    def update(self, events):
        for event in events:
            if self.isActive == True and event.type == pygame.KEYDOWN and playingnotes == False:
                if event.key == K_UP:
                    if self.noteVal < 72:
                        self.noteVal += 1
                        self.rect.move_ip(0, -10)
                    mixer.Sound.play(mixer.Sound("final_project/assets/" + str(self.noteVal) + ".wav"))
                elif event.key == K_DOWN:
                    if self.noteVal > 60:
                        self.noteVal -= 1
                        self.rect.move_ip(0, 10)
                    mixer.Sound.play(mixer.Sound("final_project/assets/" + str(self.noteVal) + ".wav"))
            if event.type == pygame.MOUSEBUTTONDOWN and playingnotes == False:
                global activeID
                if self.rect.collidepoint(event.pos):
                    self.toggleActive()
                    if self.isActive == False:
                        activeID = None
                else:
                    if self.isActive == True:
                        self.toggleActive()
                        activeID = None

    def draw(self, surface):
        surface.blit(self.pic, self.rect)


class Play(pygame.sprite.Sprite):
    def __init__(self):
        self.pic = pygame.image.load("final_project/assets/play.png")
        self.pic = pygame.transform.scale(self.pic, (40, 40))
        self.rect = self.pic.get_rect()
        self.rect.move_ip(950, 40)
        self.playing = False

    def draw(self, surface):
        surface.blit(self.pic, self.rect)


class GenerateBtn(pygame.sprite.Sprite):
    def __init__(self):
        self.pic = pygame.image.load("final_project/assets/play.png")
        self.pic = pygame.transform.scale(self.pic, (40, 40))
        self.rect = self.pic.get_rect()
        self.rect.move_ip(950, 600)
        self.playing = False

    def draw(self, surface):
        surface.blit(self.pic, self.rect)

# note input group
notes = pygame.sprite.Group()
notelist = []
xval, yval = 150, 103

for x in range(8):
    note = Note("final_project/assets/qn.png", xval, yval, x)
    xval += 100
    notelist.append(note)

for note in notelist:
    notes.add(note)

playbtn = Play()
generatebtn = GenerateBtn()

# set up window
pygame.init()
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Bayesian Brahmsian")
pygame.display.set_icon(pygame.image.load("final_project/assets/qn.png"))
clock = pygame.time.Clock()
running = True
w, h = pygame.display.get_surface().get_size()

timer = 0
 
while running:
    screen.fill("#dfddd1")
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and playbtn.playing == False:
            if event.key == K_LEFT:
                if activeID == None:
                    activeID = 7
                else:
                    notelist[activeID].toggleActive()
                    activeID -= 1
                    if activeID < 0:
                        activeID = 7
                notelist[activeID].toggleActive()
            elif event.key == K_RIGHT:
                if activeID == None:
                    activeID = 0
                else:
                    notelist[activeID].toggleActive()
                    activeID += 1
                    if activeID > 7:
                        activeID = 0
                notelist[activeID].toggleActive()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playbtn.rect.collidepoint(event.pos):
                if playbtn.playing == False:
                    playbtn.playing = True
                    playingnotes = True
                    if activeID != None:
                        notelist[activeID].toggleActive()
                    activeID = None
                    playtime = 20
                    playindex = 0
                    playbtn.pic = pygame.image.load("final_project/assets/pause.png")
                    playbtn.pic = pygame.transform.scale(playbtn.pic, (40, 40))
                else:
                    playbtn.playing = False
                    playingnotes = False
                    playbtn.pic = pygame.image.load("final_project/assets/play.png")
                    playbtn.pic = pygame.transform.scale(playbtn.pic, (40, 40))
            if generatebtn.rect.collidepoint(event.pos):
                inputsequence = []
                for note in notelist:
                    inputsequence.append(note.noteVal)
                print(inputsequence)
        
    if playbtn.playing == True:
        playtime += 1
        if playtime % 23 == 0 and playindex < 8:
            notelist[playindex].toggleActive()
            playindex += 1
        if playtime > 210:
            playbtn.playing = False
            playingnotes = False
            playbtn.pic = pygame.image.load("final_project/assets/play.png")
            playbtn.pic = pygame.transform.scale(playbtn.pic, (40, 40))
            for note in notelist:
                note.toggleActive()
            activeID = None



    for i in range(5):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 130+(20*i), w-100, 3))
    
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(520, 130, 3, 83))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(1020, 130, 3, 83))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(1030, 130, 4, 83))
    
    for x in range(len(notes)):
        if notelist[x].noteVal > 64:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(151+(100*x), 110, 30, 3))
            if notelist[x].noteVal > 66:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(151+(100*x), 90, 30, 3)) 

    for note in notes:
        note.update(events)
        note.draw(screen)

    playbtn.update(events)
    playbtn.draw(screen)
    generatebtn.update(events)
    generatebtn.draw(screen)
    # flip() the display to put work on screen
    pygame.display.flip()
    # limits FPS to 30
    dt = clock.tick(30) / 1000


    

pygame.quit()
