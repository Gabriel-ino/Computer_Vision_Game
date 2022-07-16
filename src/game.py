import pygame
from typing import Final
from cam import Cam
import random
import math

pygame.init()
pygame.font.init()


class Game:
    def __init__(self):
        self.WIDTH: Final = 720
        self.HEIGHT: Final = 480
        self.TITLE: Final = "Viruses Destroyer"
        self.FONT: Final = pygame.font.SysFont('comicsans', 24)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.score = 0
        self.cam = Cam()
        self.clock = pygame.time.Clock()
        self.running = None
        self.virus_image = pygame.image.load('img/virus.png')
        self.virus_x_coord = None
        self.virus_y_coord = None
        self.collide = False

        pygame.display.set_caption(self.TITLE)

    def run(self):
        self.running = True
        self.choose_random_position()
        while self.run:
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
            score_text = self.FONT.render(f"Score: {self.score}", False, (255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.cam.recording()
            self.cam.convert_frame()
            self.convert_to_pygame_img()
            self.screen.blit(self.cam.frame, (0, 0))
            self.screen.blit(self.virus_image, (self.virus_x_coord, self.virus_y_coord))
            self.compare_coordinates()
            if self.collide:
                self.choose_random_position()
                self.collide = False
            self.screen.blit(score_text, (20, 20))
            print(self.virus_x_coord, self.virus_y_coord)
            print(self.cam.hand_tracker.finger_x_coordinate, self.cam.hand_tracker.finger_y_coordinate)
            pygame.display.update()

    def convert_to_pygame_img(self):
        shape = self.cam.frame.shape[1::-1]
        self.cam.frame = pygame.image.frombuffer(self.cam.frame.tobytes(), shape, 'RGB')

    def compare_coordinates(self):
        if self.virus_x_coord is not None and self.virus_y_coord is not None and self.cam.hand_tracker.finger_x_coordinate is not None and self.cam.hand_tracker.finger_y_coordinate is not None:
            if (math.isclose(self.cam.hand_tracker.finger_x_coordinate, self.virus_x_coord, abs_tol=50) and
                    math.isclose(self.cam.hand_tracker.finger_y_coordinate, self.virus_y_coord, abs_tol=50)):
                self.score = self.score + 1
                self.collide = True

    def choose_random_position(self):
        self.virus_x_coord = random.randint(50, self.WIDTH - 50)
        self.virus_y_coord = random.randint(50, self.HEIGHT - 50)



