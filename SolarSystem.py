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
MAROON = (128,0,0)

AU = 149.6e6 * 1000

slider = Slider(WIN, initial=1, min=1, max=6, step=1, x=50, y=HEIGHT-50, width=70, height=30, handleColour=(255, 255, 255))
    
def main():
    run = True
    clock = pygame.time.Clock()
    time = 0
    time_text = ""

    sun = CelestialBody.Planet("Sun",0,0, 30, YELLOW, 1.98892 * 10**30, WIN)
    sun.sun = True

    mercury = CelestialBody.Planet("Mercury", 0.387 * AU, 0, 10, DARK_GREY, 3.30 * 10**23, WIN)
    mercury.y_vel = -47.4 * 1000
    mercury.SCALE = 140/AU

    venus = CelestialBody.Planet("Venus", 0.723 * AU, 0, 14, ORANGE, 4.8685 * 10**24, WIN)
    venus.y_vel = -35.02 * 1000
    venus.SCALE = 140/AU
    
    earth = CelestialBody.Planet("Earth", -1 * AU, 0, 16, BLUE, 5.9742 * 10**24, WIN)
    earth.y_vel = 29.783 * 1000
    earth.SCALE = 140/AU

    mars = CelestialBody.Planet("Mars", -1.524 * AU, 0, 12, RED, 6.39 * 10**23, WIN)
    mars.y_vel = 24.077 * 1000
    mars.SCALE = 140/AU

    jupiter = CelestialBody.Planet("Jupiter", 5.2* AU, 0, 30, MAROON, 1898 * 10 ** 24, WIN)
    jupiter.y_vel = -13.1 * 1000
    jupiter.SCALE = 140/AU

    planets = [sun, earth, mars, mercury, venus, jupiter]

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
        WIN.blit(time_scale, (WIDTH-140,HEIGHT-100))
        
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                quit()

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame_widgets.update(events)
        pygame.display.update()
        
    pygame.quit()



main()
