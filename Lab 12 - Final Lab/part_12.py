import arcade
import math  # Import math module for distance calculation
import random  # Import random module for generating random coin positions

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Forest Runner"
GRAVITY = 1
PLAYER_JUMP_SPEED = 10
PLAYER_MOVE_SPEED = 5
NEW_LEVEL_SCORE = 200  # Score needed to reach new level

class Player():
    """
    Player class to represent the playable character as a man driving a car.
    """
    def __init__(self, position_x, position_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.width = 60  # Width of the car
        self.height = 40  # Height of the car including the man
        self.change_x = 0
        self.change_y = 0

    def draw(self):
        """ Draw the player as a car with a man. """
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height - 10, self.color)
        arcade.draw_rectangle_filled(self.position_x, self.position_y + 10, self.width * 0.5, self.height * 0.4, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x - 20, self.position_y - 20, 10, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x + 20, self.position_y - 20, 10, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x, self.position_y + 20, 10, arcade.color.PEACH)

    def update(self):
        """ Apply gravity and manage screen boundaries for the player. """
        self.change_y -= GRAVITY
        self.position_x += self.change_x
        self.position_y += self.change_y

        # Prevent the player from moving out of the screen bounds
        if self.position_x < self.width / 2:
            self.position_x = self.width / 2
        elif self.position_x > SCREEN_WIDTH - self.width / 2:
            self.position_x = SCREEN_WIDTH - self.width / 2
        if self.position_y < 0:
            self.position_y = 0

class MyGame(arcade.Window):
    """
    Main application class for the game window, inheriting from arcade.Window.
    """
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.FOREST_GREEN)
        self.player = None
        self.platforms = []
        self.coins = []
        self.score = 0
        self.display_level_message = False

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.player = Player(100, 112, arcade.color.BLUE)
        # Create platforms
        for x in range(0, 1250, 64):
            self.platforms.append((x, 50, 60, 20, arcade.color.DARK_GREEN))

        # Create coins with varied placement
        for x in range(50, 1250, 50):  # More frequent placement
            for y in range(100, 400, 50):  # Create multiple layers of coins at different heights
                if random.choice([True, True, False]):  # Increase the probability of coin placement
                    self.coins.append((x, y, 10, arcade.color.GOLD))

    def draw_background(self):
        """ Draw mountains and clouds in the background """
        arcade.draw_triangle_filled(0, 100, 200, 400, 400, 100, arcade.color.DARK_GRAY)
        arcade.draw_triangle_filled(300, 100, 500, 400, 700, 100, arcade.color.GRAY)
        arcade.draw_circle_filled(200, 500, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(240, 520, 50, arcade.color.WHITE)
        arcade.draw_circle_filled(280, 500, 40, arcade.color.WHITE)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.draw_background()
        for platform in self.platforms:
            arcade.draw_rectangle_filled(platform[0], platform[1], platform[2], platform[3], platform[4])
        self.player.draw()
        for coin in self.coins:
            arcade.draw_circle_filled(coin[0], coin[1], coin[2], coin[3])
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)
        if self.display_level_message:
            arcade.draw_text("You are at a new level!", SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2, arcade.color.YELLOW, 20, align="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_MOVE_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_MOVE_SPEED

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.change_x = 0

    def update(self, delta_time):
        self.player.update()
        for coin in self.coins[:]:
            distance = math.sqrt((self.player.position_x - coin[0]) ** 2 + (self.player.position_y - coin[1]) ** 2)
            if distance < max(self.player.width, self.player.height) / 2 + coin[2]:
                self.coins.remove(coin)
                self.score += 10
                if self.score == NEW_LEVEL_SCORE:
                    self.display_level_message = True

def main():
    game = MyGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()





