import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_DIAMOND = 0.3
SPRITE_SCALING_ROCK = 0.3
DIAMOND_COUNT = 40
ROCK_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Lab 8"


class Diamond(arcade.Sprite):

    # This class represents the diamonds on our screen.
    def reset_pos(self):
        # Reset the diamond to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the diamond
        self.center_y -= 1
        # See if the diamond has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class Rock(arcade.Sprite):

    # This class represents the rocks on our screen.

    def reset_pos(self):
        # Reset the rock to a random spot below the screen
        self.center_y = random.randrange(SCREEN_HEIGHT - 820, SCREEN_HEIGHT - 720)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the rock
        self.center_y += 1
        # See if the rock has gone off the top of the screen.
        # If so, reset it.
        if self.bottom > SCREEN_HEIGHT:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_sprite_list = None
        self.diamond_sprite_list = None
        self.rock_sprite_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        self.diamond_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.rock_sound = arcade.load_sound(":resources:sounds/error5.wav")

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.YANKEES_BLUE)

        # Flag to track game over
        self.game_over = False

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.diamond_sprite_list = arcade.SpriteList()
        self.rock_sprite_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_walk2.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)

        # Create the diamonds
        for i in range(DIAMOND_COUNT):
            diamond = Diamond(":resources:images/items/gemBlue.png", SPRITE_SCALING_DIAMOND)
            diamond.center_x = random.randrange(SCREEN_WIDTH)
            diamond.center_y = random.randrange(SCREEN_HEIGHT)
            self.diamond_sprite_list.append(diamond)

        # Create the rocks
        for i in range(ROCK_COUNT):
            rock = Rock(":resources:images/tiles/rock.png", SPRITE_SCALING_ROCK)
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)
            self.rock_sprite_list.append(rock)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.diamond_sprite_list.draw()
        self.rock_sprite_list.draw()
        self.player_sprite_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if self.game_over:
            arcade.draw_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.RED, font_size=40, anchor_x="center")

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """
        if not self.game_over:
            self.diamond_sprite_list.update()
            self.rock_sprite_list.update()

            diamond_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.diamond_sprite_list)

            # Loop through each colliding diamond, remove it, and add to the score.
            for diamond in diamond_hit_list:
                diamond.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.diamond_sound)

            rock_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.rock_sprite_list)

            for rock in rock_hit_list:
                rock.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(self.rock_sound)

            # Check if all diamonds are collected
            if len(self.diamond_sprite_list) == 0:
                self.game_over = True


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
