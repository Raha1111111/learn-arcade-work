import random
import arcade
from pyglet.math import Vec2

# adding a comment

SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_DIAMOND = 0.5

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

NUMBER_OF_DIAMONDS = 50

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7

SCORE_FONT_SIZE = 16
SCORE_COLOR = arcade.color.ORANGE


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.diamond_list = None

        # Set up the player
        self.player_sprite = None
        self.score = 0

        self.diamond_sound = arcade.load_sound(":resources:sounds/coin5.wav")

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.game_over = False

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.diamond_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png",
                                           scale=0.55)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)

        # Place boxes inside a loop
        for x in range(280, 730, 64):
            wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)
        for x in range(280, 730, 64):
                wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", SPRITE_SCALING_BOX)
                wall.center_x = x
                wall.center_y = 300
                self.wall_list.append(wall)
        for x in range(210, 550, 64):
                wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", SPRITE_SCALING_BOX)
                wall.center_x = x
                wall.center_y = 850
                self.wall_list.append(wall)
        for x in range(150, 400, 64):
                    wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", SPRITE_SCALING_BOX)
                    wall.center_x = x
                    wall.center_y = 550
                    self.wall_list.append(wall)
        for x in range(400, 700, 64):
                        wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", SPRITE_SCALING_BOX)
                        wall.center_x = x
                        wall.center_y = 180
                        self.wall_list.append(wall)
        for x in range(0, 195, 64):
                            wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", SPRITE_SCALING_BOX)
                            wall.center_x = x
                            wall.center_y = 150
                            self.wall_list.append(wall)
        for y in range(400, 700, 64):
                                wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", SPRITE_SCALING_BOX)
                                wall.center_x = 700
                                wall.center_y = y
                                self.wall_list.append(wall)
        for y in range(400, 900, 64):
            wall = arcade.Sprite(":resources:images/tiles/dirtCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 500
            wall.center_y = y
            self.wall_list.append(wall)
        # -- Randomly place diamonds where there are no walls
        # Create the diamonds
        max_x = 1000
        max_y = 1000

        for i in range(NUMBER_OF_DIAMONDS):

            # Create the diamond instance
            # Diamond image from kenney.nl
            diamond = arcade.Sprite(":resources:images/items/gemRed.png", SPRITE_SCALING_DIAMOND)

            # --- IMPORTANT PART ---

            # Boolean variable if we successfully placed the diamond
            diamond_placed_successfully = False

            # Keep trying until success
            while not diamond_placed_successfully:
                # Position the diamond
                diamond.center_x = random.randrange(max_x)
                diamond.center_y = random.randrange(max_y)

                # See if the diamond is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(diamond, self.wall_list)

                # See if the diamond is hitting another diamond
                diamond_hit_list = arcade.check_for_collision_with_list(diamond, self.diamond_list)

                if len(wall_hit_list) == 0 and len(diamond_hit_list) == 0:
                    # It is!
                    diamond_placed_successfully = True

            # Add the diamond to the lists
            self.diamond_list.append(diamond)

            # --- END OF IMPORTANT PART ---

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.WHITE_SMOKE)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.diamond_list.draw()
        self.player_list.draw()

        # Convert screen coordinates to world coordinates
        screen_center_world = Vec2(
            self.camera_sprites.position[0] + self.width/2,
            self.camera_sprites.position[1] + self.height/2
        )

        score_offset = Vec2(-400, -290)

        score_position_world = screen_center_world + score_offset

        # Draw the score in the bottom left corner
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, score_position_world.x, score_position_world.y, SCORE_COLOR, SCORE_FONT_SIZE)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Apply boundary checks to prevent character from going off screen
        self.apply_boundary_checks()

        # Scroll the screen to the player
        self.scroll_to_player()

        if not self.game_over:
            self.diamond_list.update()

            diamond_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.diamond_list)

            # Loop through each colliding diamond, remove it, and add to the score.
            for diamond in diamond_hit_list:
                diamond.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.diamond_sound)

            if len(self.diamond_list) == 0:
                print("Game Over! Score:", self.score)
                self.game_over = True

    def apply_boundary_checks(self):
        """ Check boundaries and prevent character from going off screen """
        if self.player_sprite.left < 0:
            self.player_sprite.left = 0
        elif self.player_sprite.right > 1000:
            self.player_sprite.right = 1000

        if self.player_sprite.bottom < 0:
            self.player_sprite.bottom = 0
        elif self.player_sprite.top > 1000:
            self.player_sprite.top = 1000

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        # Calculate the desired position for the camera
        desired_x = self.player_sprite.center_x - self.width / 2
        desired_y = self.player_sprite.center_y - self.height / 2

        # Limit scrolling at the edges of the game world
        left_boundary = 0
        right_boundary = 1000  # Adjust this based on your game world width
        top_boundary = 1000  # Adjust this based on your game world height
        bottom_boundary = 0

        # Calculate the maximum allowed camera position
        max_x = right_boundary - self.width
        max_y = top_boundary - self.height

        # Clamp desired position to the boundaries
        desired_x = max(left_boundary, min(desired_x, max_x))
        desired_y = max(bottom_boundary, min(desired_y, max_y))

        # Move the camera to the clamped desired position
        position = Vec2(desired_x, desired_y)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
