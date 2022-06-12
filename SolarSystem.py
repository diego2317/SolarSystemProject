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
SUN_COLOR = (255, 255, 0)
EARTH_COLOR = (100, 149, 237)
MARS_COLOR = (188, 39, 50)
MERCURY_COLOR = (80, 78, 81)
VENUS_COLOR = (255, 128, 0)
JUPITER_COLOR = (148, 107, 69)

AU = 149.6e6 * 1000

slider = Slider(WIN, initial=1, min=1, max=6, step=1, x=50, y=HEIGHT-50, width=70, height=30, handleColour=(255, 255, 255))
    
def main():
    run = True
    clock = pygame.time.Clock()
    time = 0
    time_text = ""

    sun = CelestialBody.Planet("Sun",0,0, 30, SUN_COLOR, 1.98892 * 10**30, WIN)
    sun.sun = True

    mercury = CelestialBody.Planet("Mercury", 0.387 * AU, 0, 10, MERCURY_COLOR, 3.30 * 10**23, WIN)
    mercury.y_vel = -47.4 * 1000
    mercury.SCALE = 140/AU

    venus = CelestialBody.Planet("Venus", 0.723 * AU, 0, 14, VENUS_COLOR, 4.8685 * 10**24, WIN)
    venus.y_vel = -35.02 * 1000
    venus.SCALE = 140/AU
    
    earth = CelestialBody.Planet("Earth", -1 * AU, 0, 16, EARTH_COLOR, 5.9742 * 10**24, WIN)
    earth.y_vel = 29.783 * 1000
    earth.SCALE = 140/AU

    mars = CelestialBody.Planet("Mars", -1.524 * AU, 0, 12, MARS_COLOR, 6.39 * 10**23, WIN)
    mars.y_vel = 24.077 * 1000
    mars.SCALE = 140/AU

    jupiter = CelestialBody.Planet("Jupiter", 5.2* AU, 0, 30, JUPITER_COLOR, 1898 * 10 ** 24, WIN)
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
        
        mercury_dist = FONT.render("Mercury is: " + f"{round(mercury.distance_to_sun/AU, 2)} AU away from the sun", 1, WHITE)
        mercury_text = "Mercury is: " + f"{round(mercury.distance_to_sun/AU, 2)} AU away from the sun"
        WIN.blit(mercury_dist, (WIDTH/2- FONT.size(mercury_text)[0]/2, HEIGHT-550))
        
        venus_dist = FONT.render("Venus is: " + f"{round(venus.distance_to_sun/AU, 2)} AU away from the sun", 1, WHITE)
        venus_text = "Venus is: " + f"{round(venus.distance_to_sun/AU, 2)} AU away from the sun"
        WIN.blit(venus_dist, (WIDTH/2 - FONT.size(venus_text)[0]/2, HEIGHT-500))
        
        earth_dist = FONT.render("Earth is: " + f"{round(earth.distance_to_sun/AU, 2)} AU away from the sun", 1, WHITE)
        earth_text = "Earth is: " + f"{round(earth.distance_to_sun/AU, 2)} AU away from the sun"
        WIN.blit(earth_dist, (WIDTH/2 - FONT.size(earth_text)[0]/2, HEIGHT-450))
        
        mars_dist = FONT.render("Mars is: " + f"{round(mars.distance_to_sun/AU, 2)} AU away from the sun", 1, WHITE)
        mars_text = "Mars is: " + f"{round(mars.distance_to_sun/AU, 2)} AU away from the sun"
        WIN.blit(mars_dist, (WIDTH/2 - FONT.size(mars_text)[0]/2, HEIGHT-400))
        
        jupiter_dist = FONT.render("Jupiter is: " + f"{round(jupiter.distance_to_sun/AU, 2)} AU away from the sun", 1, WHITE)
        jupiter_text = "Jupiter is: " + f"{round(jupiter.distance_to_sun/AU, 2)} AU away from the sun"
        WIN.blit(jupiter_dist, (WIDTH/2 - FONT.size(jupiter_text)[0]/2, HEIGHT-350))
        
        
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
