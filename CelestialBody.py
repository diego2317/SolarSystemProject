import pygame
import math

pygame.init()

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

FONT = pygame.font.SysFont("comicsans", 16)


class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    TIMESTEP = 3600*24 # 1 day
    SCALE = 250/AU #1 AU = 100 pixels

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

    def __init__(self, name, x, y, radius, color, mass, win):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun=0

        self.x_vel=0
        self.y_vel=0
        self.moons = []

        self.WIDTH = win.get_width()
        self.HEIGHT = win.get_height()
        self.limit = 1000
        

    def draw(self, win):
        x = self.x * self.SCALE + self.WIDTH/2
        y = self.y * self.SCALE + self.HEIGHT/2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit[-self.limit:]:
                x, y = point
                x = x * self.SCALE + self.WIDTH / 2
                y = y * self.SCALE + self.HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 1)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

        distance_text = FONT.render(self.name, 1, (255-self.color[0], 255-self.color[1], 255-self.color[2]))
        win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))
		

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        #calculates force of gravity between two objects
        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x) #finds theta
        force_x = math.cos(theta) * force
        force_y = math.sin(theta)*force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
            
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))