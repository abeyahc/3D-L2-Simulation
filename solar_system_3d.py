
import math
import matplotlib.pyplot as plt

from vectors import Vector


class SolarSystem:
    def __init__(self, size):
        self.size = size
        # contain all bodies within the solar system
        self.bodies = []

        self.fig, self.ax = plt.subplots(
            # first two arguments 1, 1, create a single set of axes
            1,
            1,
            # sets projection to 3D || Axes created are an Axes3D object
            subplot_kw={"projection": "3d"},
            # sets overall size of the figure containing Axes3D
            figsize=(self.size / 50, self.size / 50),
        )
        self.fig.tight_layout()

    # used to add orbiting bodies to the solar system
    def add_body(self, body):
        self.bodies.append(body)

    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()

    # sets limits for the three axes using the solar system's size and updates the plot through the pause()
    def draw_all(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))
        plt.pause(0.001)
        self.ax.clear()


class SolarSystemBody:
    min_display_size = 10
    display_log_base = 1.3

    def __init__(
        self,
        solar_system,
        mass,
        position=(0, 0, 0),
        velocity=(0, 0, 0),
    ):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
        self.colour = "black"

        self.solar_system.add_body(self)

    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.position[1],
            self.position[2] + self.position[2],
        )

    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker="o",
            markersize=self.display_size,
            color=self.colour
        )
