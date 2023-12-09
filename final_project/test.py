import pandas as pd
import numpy as np
import pygame
from pygame.locals import *

class Note(pygame.sprite.Sprite):
    def __init__(self, pic, x, y):
        super().__init__()
        self.pic = pygame.image.load(pic)
        self.pic = pygame.transform.scale(self.pic, (25, 75))
        self.rect = self.pic.get_rect()
        self.rect.move_ip(x, y)
        self.isActive = True

    def update(self, events):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        if self.isActive == True:
            if pressed_keys[pygame.K_w]:
                self.rect.move_ip(0, -5)
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                    if self.rect.collidepoint(event.pos):
                        self.isActive = not self.isActive
                        print(self.isActive)

    def draw(self, surface):
        surface.blit(self.pic, self.rect)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
running = True
dt = 0


note1 = Note("final_project/assets/quarternote.png", 400, 400)
note2 = Note("final_project/assets/quarternote.png", 450, 400)
note3 = Note("final_project/assets/quarternote.png", 500, 400)


while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    screen.fill("#dfddd1")
    note1.update(events)
    note1.draw(screen)
    note2.update(events)
    note2.draw(screen)
    note3.update(events)
    note3.draw(screen)

    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    # flip() the display to put work on screen
    pygame.display.flip()
    # limits FPS to 30
    dt = clock.tick(30) / 1000

pygame.quit()


# data = pd.read_json(path_or_buf='final_project/data-test-1.jsonl', lines=True)
# data = data.drop(['backend','composition_time', 'country', 'loops_listened', 'request_id', 'session_id'], axis = 1)
# print("Full entry")
# print(data)
# print("input sequence")
# noteinput = data['input_sequence']
# for note in noteinput[0][0]['notes']:
#     print(note)
# print("output sequence")
# for note in data['output_sequence'][0][0]['notes']:
#     print(note)