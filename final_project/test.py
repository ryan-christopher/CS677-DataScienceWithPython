import pandas as pd
import numpy as np
import pygame
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("#3a3a3a")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

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