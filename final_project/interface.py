import pandas as pd
import numpy as np
import pygame
from pygame.locals import *
import pygame.mixer as mixer

activeID = None
playingnotes = False
inputsequence = []
mixer.init()

valtoNotes = {
    24 : "C",  25 : "C#", 26 : "D",  27 : "Eb", 28 : "E",  29 : "F", 
    30 : "F#", 31 : "G",  32 : "G#", 33 : "A",  34 : "Bb", 35 : "B",
    36 : "C",  37 : "C#", 38 : "D",  39 : "Eb", 40 : "E",  41 : "F",
    42 : "F#", 43 : "G",  44 : "G#", 45 : "A",  46 : "Bb", 47 : "B",
    48 : "C",  49 : "C#", 50 : "D",  51 : "Eb", 52 : "E",  53 : "F", 
    54 : "F#", 55 : "G",  56 : "G#", 57 : "A",  58 : "Bb", 59 : "B",
    60 : "C",  61 : "C#", 62 : "D",  63 : "Eb", 64 : "E",  65 : "F", 
    66 : "F#", 67 : "G",  68 : "G#", 69 : "A",  70 : "Bb", 71 : "B", 
    72 : "C"
}

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
            global playingnotes
            if playingnotes == False:
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
                        if self.noteVal in [60, 63, 65, 67, 70]:
                            self.rect.move_ip(0, 0)
                        else:
                            self.rect.move_ip(0, -10)
                        self.noteVal += 1
                    mixer.Sound.play(mixer.Sound("final_project/assets/" + str(self.noteVal) + ".wav")) 
                elif event.key == K_DOWN:
                    if self.noteVal > 60:
                        if self.noteVal in [61, 64, 66, 68, 71]:
                            self.rect.move_ip(0, 0)
                        else:
                            self.rect.move_ip(0, 10)
                        self.noteVal -= 1
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

font = pygame.font.Font(pygame.font.get_default_font(), 22)
 
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
                    inputsequence = []
                    for note in notelist:
                        inputsequence.append(note.noteVal)
                    note2seq = [57, 57, 57, 56, 57, 57, 57, 50]
                    note3seq = [43, 42, 43, 41, 43, 42, 43, 41]
                    note4seq = [27, 26, 24, 24, 27, 27, 26, 24]
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
            note1 = mixer.Sound("final_project/assets/" + str(notelist[playindex].noteVal) + ".wav")
            note2 = mixer.Sound("final_project/assets/" + str(note2seq[playindex]) + ".wav")
            note3 = mixer.Sound("final_project/assets/" + str(note3seq[playindex]) + ".wav")
            note4 = mixer.Sound("final_project/assets/" + str(note4seq[playindex]) + ".wav")
            mixer.find_channel(True).play(note1)
            mixer.find_channel(True).play(note2)
            mixer.find_channel(True).play(note3)
            mixer.find_channel(True).play(note4)
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
        if notelist[x].noteVal > 68:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(151+(100*x), 110, 30, 3))
            if notelist[x].noteVal > 71:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(151+(100*x), 90, 30, 3)) 
        if notelist[x].noteVal in [61, 66, 68]:
            screen.blit(font.render("#", True, (0, 0, 0)), (notelist[x].rect[0]-10, notelist[x].rect[1]+47))
        elif notelist[x].noteVal in [63, 70]:
            screen.blit(font.render("b", True, (0, 0, 0)), (notelist[x].rect[0]-10, notelist[x].rect[1]+47))

    for note in notes:
        note.update(events)
        note.draw(screen)

    playbtn.update(events)
    playbtn.draw(screen)
    generatebtn.update(events)
    generatebtn.draw(screen)

    for i in range(8):
        screen.blit(font.render(str(notelist[i].noteVal) + " - " + str(valtoNotes[notelist[i].noteVal]), True, (0, 0, 0)), (160+(100*i), 30))

    # flip() the display to put work on screen
    pygame.display.flip()
    # limits FPS to 30
    dt = clock.tick(30) / 1000

pygame.quit()