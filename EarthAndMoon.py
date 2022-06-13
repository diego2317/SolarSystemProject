from pickle import TRUE
import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import CelestialBody

pygame.init()

WIDTH, HEIGHT =  1600, 1600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

FONT = pygame.font.SysFont("comicsans", 16)

#Various colors for planets
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
ORANGE = (255, 128, 0)
GOLD = (255,215,0)
DARK_BLUE = (0,0,128)
LIGHT_BLUE = (173,216,230)
ORANGE = (255,69,0)

AU = 149.6e6 * 1000

slider = Slider(WIN, initial=1, min=1, max=6, step=1, x=50, y=HEIGHT-100, width=70, height=30, handleColour=(255, 255, 255))
    
def main():
    run = True
    clock = pygame.time.Clock()
    time = 0
    time_text = ""

    earth = CelestialBody.Planet("Earth", 0, 0, 4.2587504556, BLUE, 5.9742 * 10**24, WIN)
    earth.sun = TRUE
    earth.SCALE = 250000/AU

    moon = CelestialBody.Planet("Moon", 0.002569 * AU, 0, 1.16138016662, DARK_GREY, 7.34767309 * 10 ** 22, WIN)
    moon.y_vel = -1.022 * 1000
    moon.SCALE = 250000/AU
    moon.limit = 100000000



    planets = [earth, moon]

    while run:
        events = pygame.event.get()
        timestep = 60 * slider.getValue()
        clock.tick(timestep)
        WIN.fill((0,0,0))
        time += 1
        
        time_text = FONT.render(f"{round(time/365,1)} years have passed", 1, WHITE)
        time_text_rect = time_text.get_rect(center=(WIDTH/2, 30))
        
        time_scale = FONT.render(f"1 second = {round(slider.getValue()*60)} days", 1, WHITE)
        WIN.blit(time_text, time_text_rect)
        WIN.blit(time_scale, (WIDTH-140,HEIGHT-150))
        
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                quit()

        for planet in planets:
            if not planet.sun:
                planet.update_position(planets)
            planet.draw(WIN)

        pygame_widgets.update(events)
        pygame.display.update()
        
    pygame.quit()



main()