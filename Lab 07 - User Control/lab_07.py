import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 5
ACCELERATION = 1.05

class Rocket:
    def __init__(self, position_x, position_y, change_x, change_y):
        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        """ Draw the rocket with the instance variables we have. """
        # Body of the rocket
        arcade.draw_rectangle_filled(self.position_x, self.position_y, 20, 60, arcade.color.RED)
        # Top cone of the rocket
        arcade.draw_triangle_filled(self.position_x - 10, self.position_y + 30,
                                    self.position_x + 10, self.position_y + 30,
                                    self.position_x, self.position_y + 45, arcade.color.RED)
        # Fins of the rocket
        arcade.draw_triangle_filled(self.position_x - 10, self.position_y - 30,
                                    self.position_x - 25, self.position_y - 45,
                                    self.position_x - 10, self.position_y - 45, arcade.color.DARK_SPRING_GREEN)
        arcade.draw_triangle_filled(self.position_x + 10, self.position_y - 30,
                                    self.position_x + 25, self.position_y - 45,
                                    self.position_x + 10, self.position_y - 45, arcade.color.DARK_SPRING_GREEN)
        # Window of the rocket
        arcade.draw_circle_filled(self.position_x, self.position_y + 10, 5, arcade.color.SKY_BLUE)

    def update(self):
        # Move the rocket
        self.position_y += self.change_y
        self.position_x += self.change_x

        # Accelerate the rocket
        self.change_x *= ACCELERATION
        self.change_y *= ACCELERATION

        # See if the rocket hit the edge of the screen. If so, stop acceleration and reverse direction
        if self.position_x < 20 or self.position_x > SCREEN_WIDTH - 20:
            self.change_x = 0

        if self.position_y < 40 or self.position_y > SCREEN_HEIGHT - 40:
            self.change_y = 0

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.rocket = Rocket(50, 50, 0, 0)

    def on_draw(self):
        arcade.start_render()
        self.rocket.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.rocket.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.rocket.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.rocket.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.rocket.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.rocket.change_y = 0
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.rocket.change_x = 0

    def update(self, delta_time):
        self.rocket.update()

def main():
    window = MyGame(640, 480, "Rocket Movement Example")
    arcade.run()

main()

