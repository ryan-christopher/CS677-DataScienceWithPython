import pandas as pd
import numpy as np
import pygame
from pygame.locals import *
import pygame.mixer as mixer
from predict import generate

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


GENERATE = pygame.USEREVENT + 1

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

class PredictedNote(pygame.sprite.Sprite):
    def __init__(self, pic, x, y, id, voice):
        super().__init__()
        self.pic = pygame.image.load(pic)
        self.pic = pygame.transform.scale(self.pic, (35, 70))
        self.pic.set_alpha(128)
        self.rect = self.pic.get_rect()
        self.rect.move_ip(x, y)
        self.id = id
        self.voice = voice
        if self.voice == 'alto':
            self.noteVal = 60
        elif self.voice == 'tenor':
            self.noteVal = 48
        elif self.voice == 'bass':
            self.noteVal = 48

    def update(self, events):
        for event in events:
            if event.type == GENERATE:
                if self.voice == 'alto' and self.noteVal < note2seq[self.id]:
                    while self.noteVal < note2seq[self.id]:
                        if self.noteVal in [60, 63, 65, 67, 70, 48, 51, 53, 55, 58]:
                            self.rect.move_ip(0, 0)
                        else:
                            self.rect.move_ip(0, -10)
                        self.noteVal += 1
                if self.voice == 'alto' and self.noteVal > note2seq[self.id]:
                    while self.noteVal > note2seq[self.id]:
                        if self.noteVal in [61, 64, 66, 68, 71, 49, 52, 54, 56, 59]:
                            self.rect.move_ip(0, 0)
                        else:
                            self.rect.move_ip(0, 10)
                        self.noteVal -= 1
                if self.voice == 'tenor' and self.noteVal < note3seq[self.id]:
                    while self.noteVal < note3seq[self.id]:
                        if self.noteVal in [60, 63, 65, 67, 70, 48, 51, 53, 55, 58]:
                            self.rect.move_ip(0, 0)
                        else:
                            self.rect.move_ip(0, -10)
                        self.noteVal += 1
                if self.voice == 'tenor' and self.noteVal > note3seq[self.id]:
                    while self.noteVal > note3seq[self.id]:
                        if self.noteVal in [61, 64, 66, 68, 71, 49, 52, 54, 56, 59]:
                            self.rect.move_ip(0, 0)
                        else:
                            self.rect.move_ip(0, 10)
                        self.noteVal -= 1
                if self.voice == 'bass' and self.noteVal < note4seq[self.id]:
                    while self.noteVal < note4seq[self.id]:
                        if self.noteVal in [60, 63, 65, 67, 70, 48, 51, 53, 55, 58, 36, 39, 41, 43, 46, 24, 27, 29, 31, 34]:
                            self.rect.move_ip(0, 0)
                        else:
                            self.rect.move_ip(0, -10)
                        self.noteVal += 1
                if self.voice == 'bass' and self.noteVal > note4seq[self.id]:
                    while self.noteVal > note4seq[self.id]:
                        if self.noteVal in [61, 64, 66, 68, 71, 49, 52, 54, 56, 59, 37, 40, 42, 44, 47, 25, 28, 30, 32, 35]:
                            self.rect.move_ip(0, 0)
                        else:
                            self.rect.move_ip(0, 10)
                        self.noteVal -= 1


    def draw(self, surface):
        surface.blit(self.pic, self.rect)


class Play(pygame.sprite.Sprite):
    def __init__(self):
        self.pic = pygame.image.load("final_project/assets/play.png")
        self.pic = pygame.transform.scale(self.pic, (40, 40))
        self.rect = self.pic.get_rect()
        self.rect.move_ip(950, 100)
        self.playing = False

    def draw(self, surface):
        surface.blit(self.pic, self.rect)


class GenerateBtn(pygame.sprite.Sprite):
    def __init__(self):
        self.rect = pygame.Rect((900, 600), (100, 100))
        self.playing = False

    def draw(self, surface):
        surface.blit(font.render("Generate", True, (0, 0, 0)), (900, 600))


class Staff(pygame.sprite.Sprite):
    def __init__(self, pic, x, y, scalex, scaley):
        self.pic = pygame.image.load(pic)
        self.pic = pygame.transform.scale(self.pic, (scalex, scaley))
        self.rect = self.pic.get_rect()
        self.rect.move_ip(x, y)
    
    def draw(self, surface):
        surface.blit(self.pic, self.rect)


treble = Staff("final_project/assets/treble.png", 45, 220, 70, 110)
bass = Staff("final_project/assets/bass.png", 55, 400, 50, 65)
brace = Staff("final_project/assets/brace.png", -10, 218, 50, 270)


# note input group
notes = pygame.sprite.Group()
altonotes = pygame.sprite.Group()
tenornotes = pygame.sprite.Group()
bassnotes = pygame.sprite.Group()
notelist, altonotelist, tenornotelist, bassnotelist = [], [], [], []
xval, yval, altox, altoy = 150, 203, 145, 249
tenorx, tenory, bassx, bassy = 150, 317, 145, 435

for x in range(8):
    note = Note("final_project/assets/qn.png", xval, yval, x)
    xval += 100
    notelist.append(note)

for note in notelist:
    notes.add(note)

for n in range(8):
    altonote = PredictedNote("final_project/assets/qn-down.png", altox, altoy, n, voice = "alto")
    altox += 100
    altonotelist.append(altonote)
    tenornote = PredictedNote("final_project/assets/qn.png", tenorx, tenory, n, voice = "tenor")
    tenorx += 100
    tenornotelist.append(tenornote)
    bassnote = PredictedNote("final_project/assets/qn-down.png", bassx, bassy, n, voice = "bass")
    bassx += 100
    bassnotelist.append(bassnote)

for altonote in altonotelist:
    altonotes.add(altonote)
for tenornote in tenornotelist:
    tenornotes.add(tenornote)
for bassnote in bassnotelist:
    bassnotes.add(bassnote)

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

note2seq, note3seq, note4seq = [], [], []
 
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
                note2seq, note3seq, note4seq = generate(inputsequence)
                for x in range(len(note4seq)):
                    if note4seq[x] < 40:
                        note4seq[x] += 12
                pygame.event.post(pygame.event.Event(GENERATE))
        
    if playbtn.playing == True:
        playtime += 1
        if playtime % 23 == 0 and playindex < 8:
            notelist[playindex].toggleActive()
            note1 = mixer.Sound("final_project/assets/" + str(notelist[playindex].noteVal) + ".wav")
            if len(note2seq) > 0:
                note2 = mixer.Sound("final_project/assets/" + str(note2seq[playindex]) + ".wav")
                note3 = mixer.Sound("final_project/assets/" + str(note3seq[playindex]) + ".wav")
                note4 = mixer.Sound("final_project/assets/" + str(note4seq[playindex]) + ".wav")
            mixer.find_channel(True).play(note1)
            if len(note2seq) > 0:
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
        pygame.draw.rect(screen, (0, 0, 0), 
                         pygame.Rect(50, 230+(20*i), w-100, 3))
        pygame.draw.rect(screen, (0, 0, 0), 
                         pygame.Rect(50, 395+(20*i), w-100, 3))
     
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 230, 3, 248))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(520, 230, 3, 248))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(1020, 230, 3, 248))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(1030, 230, 4, 248))

    
    for x in range(len(notes)):
        if notelist[x].noteVal > 68:
            pygame.draw.rect(screen, (0, 0, 0), 
                             pygame.Rect(151+(100*x), 210, 30, 3))
            if notelist[x].noteVal > 71:
                pygame.draw.rect(screen, (0, 0, 0), 
                                 pygame.Rect(151+(100*x), 190, 30, 3)) 
        if tenornotelist[x].noteVal > 46:
            pygame.draw.rect(screen, (0, 0, 0), 
                             pygame.Rect(151+(100*x), 375, 30, 3))
        if bassnotelist[x].noteVal < 41:
            pygame.draw.rect(screen, (0, 0, 0), 
                             pygame.Rect(151+(100*x), 497, 30, 3))
        if notelist[x].noteVal in [61, 66, 68]:
            screen.blit(font.render("#", True, (0, 0, 0)), 
                        (notelist[x].rect[0]-10, notelist[x].rect[1]+47))
        elif notelist[x].noteVal in [63, 70]:
            screen.blit(font.render("b", True, (0, 0, 0)), 
                        (notelist[x].rect[0]-10, notelist[x].rect[1]+47))
    
    for altonote in altonotes:
        altonote.update(events)
        altonote.draw(screen)
    for tenornote in tenornotes:
        tenornote.update(events)
        tenornote.draw(screen)
    for bassnote in bassnotes:
        bassnote.update(events)
        bassnote.draw(screen)

    for note in notes:
        note.update(events)
        note.draw(screen)
        
    playbtn.update(events)
    playbtn.draw(screen)
    generatebtn.update(events)
    generatebtn.draw(screen)
    treble.draw(screen)
    bass.draw(screen)
    brace.draw(screen)

    for i in range(8):
        screen.blit(font.render(str(notelist[i].noteVal) + " - " + str(valtoNotes[notelist[i].noteVal]),
                                True, (0, 0, 0)), (145+(100*i), 130))

    pygame.display.flip()
    # limits FPS to 30
    dt = clock.tick(30) / 1000

pygame.quit()