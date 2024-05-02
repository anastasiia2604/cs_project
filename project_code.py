import sys
from sys import exit
import pygame
from pygame.locals import *
#import matplotlib.pyplot as plt

pygame.init()

screen_width = 1360
screen_height = 690
clock = pygame.time.Clock()

pygame.mouse.set_visible(2)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simulation of A-level Chemisrty CPAC practicals 3 and 7')
surface = pygame.Surface((screen_width,screen_height), pygame.SRCALPHA).convert_alpha() 
surface.fill((91, 151, 207))

objects = []

class Button():
    def __init__(self, x, y, width, height, button_image1, button_image2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pressed = False

        self.button_image1 = pygame.image.load(button_image1)
        self.button_image2 = pygame.image.load(button_image2)

        self.button_surface = pygame.Surface((self.width, self.height))
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        
        objects.append(self)

    def process(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            self.button_size = pygame.transform.scale(self.button_image2, (self.width, self.height))
            self.button_placing = surface.blit(self.button_image2, (self.x, self.y))
        else:
            self.button_size = pygame.transform.scale(self.button_image1, (self.width, self.height))
            self.button_placing = surface.blit(self.button_image1, (self.x, self.y))

    def check_for_input(self, position):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            return True
        return False

class Solution:
    def __init__(self):
        self.solution_height = 150
        self.height = self.solution_height + 200

        self.red = 0
        self.green = 0
        self.blue = 255

        self.surface = pygame.surface.Surface((280, self.solution_height))
        self.surface.fill((self.red, self.green, self.blue))
        self.surf = self.surface.convert_alpha()
        self.surf.set_alpha(15)

        self.rect = self.surf.get_rect(
            topleft = (540, self.height)
        )
        
    
    def draw_beaker():
        pygame.draw.line(surface, (0,0,0), [540, 500], [540, 200])
        pygame.draw.line(surface, (0,0,0), [820, 500], [820, 200])
        pygame.draw.line(surface, (0,0,0), [540, 500], [820, 500])

    def draw_solution_border(self):
        pygame.draw.line(surface, 'white', (540, self.height+1), (820, self.height+1))

    def colour_change():
        for i in range(256):
            self.red += i
            self.green += i
            self.surface.fill((self.red, self.green, self.blue))





def main_menu():
    objects.clear()
    surface.fill((91, 151, 207))

    #button for practical 3:
    practical3_button = Button(391, 285, 579, 77, 'main_code/rp3b1.png', 'main_code/rp3b2.png')
    
    #button for practical 7:
    practical7_button = Button(391, 397, 579, 77, 'main_code/rp7b1.png', 'main_code/rp7b2.png')
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if practical3_button.check_for_input(mouse):
                    practical3()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if practical7_button.check_for_input(mouse):
                    practical7()

        screen.blit(surface,(0,0))
        menu = pygame.image.load('main_code/menu.png')
        screen.blit(menu, (34, 36))

        for object in objects:
            object.process()
        pygame.display.update()
        clock.tick(60)

def practical3():
    objects.clear()
    surface.fill((91, 151, 207))

    pygame.draw.line(surface, (0,0,0), [640, 450], [720, 370])
    pygame.draw.line(surface, (0,0,0), [640, 370], [720, 450])

    back_button = Button(1183, 36, 122, 37, 'main_code/back_button1.png', 'main_code/back_button2.png')

    start_button = Button(493, 597, 202, 37, 'main_code/start_button1.png', 'main_code/start_button2.png')

    while True:
        solution = Solution()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_for_input(mouse):
                    main_menu()
                if start_button.check_for_input(mouse):
                    solution.colour_change

        screen.blit(surface,(0,0))

        practical3_image = pygame.image.load('main_code/practical3.png')
        screen.blit(practical3_image, (15, 22))

        practical3_conditions = pygame.image.load('main_code/practical3_conditions.png')
        screen.blit(practical3_conditions, (40, 251))

        practical3_notes = pygame.image.load('main_code/practical3_notes.png')
        screen.blit(practical3_notes, (935, 118))

        screen.blit(solution.surf, solution.rect)

        Solution().draw_solution_border()
        Solution.draw_beaker()

        for object in objects:
            object.process()
        pygame.display.update()
        clock.tick(60)

def practical7():
    objects.clear()
    surface.fill((91, 151, 207))

    back_button = Button(1183, 36, 122, 37, 'main_code/back_button1.png', 'main_code/back_button2.png')

    start_button = Button(493, 597, 202, 37, 'main_code/start_button1.png', 'main_code/start_button2.png')

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_for_input(mouse):
                    main_menu()

        solution = Solution()

        screen.blit(surface,(0,0))
        practical7_image = pygame.image.load('main_code/practical7.png')
        screen.blit(practical7_image, (15, 22))

        practical7_conditions = pygame.image.load('main_code/practical7_conditions.png')
        screen.blit(practical7_conditions, (29, 246))

        practical7_equations = pygame.image.load('main_code/practical7_equations.png')
        screen.blit(practical7_equations, (894, 76))

        practical7_notes = pygame.image.load('main_code/practical7_notes.png')
        screen.blit(practical7_notes, (916, 207))

        screen.blit(solution.surf, solution.rect)

        Solution().draw_solution_border()
        Solution.draw_beaker()

        for object in objects:
            object.process()
        pygame.display.update()
        clock.tick(60)

#def simulation3():


main_menu()








