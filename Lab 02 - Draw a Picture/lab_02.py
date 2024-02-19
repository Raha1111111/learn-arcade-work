# Library imports
import arcade

# Constants - variables that do not change
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Drawing With Functions Example"


def draw_background():
    
    # Draw the sky in the top two-thirds
    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      SCREEN_HEIGHT * (1 / 3),
                                      arcade.color.SKY_BLUE)

    # Draw the ground in the bottom third
    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT / 3,
                                      0,
                                      arcade.color.DARK_SPRING_GREEN)


def draw_bird(x, y):
    """
    Draw a bird using a couple arcs.
    """
    arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x + 40, y, 20, 20, arcade.color.BLACK, 90, 180)


def draw_pine_tree(x, y):
    """
    This function draws a pine tree at the specified location.
    """
    # Draw the triangle on top of the trunk
    arcade.draw_triangle_filled(x + 40, y,
                                x, y - 100,
                                x + 80, y - 100,
                                arcade.csscolor.DARK_GREEN)

    # Draw the trunk
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)


def main():
    """
    This is the main program.
    """

    # Open the window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Start the render process. This must be done before any drawing commands.
    arcade.start_render()

    # Call our drawing functions.
    draw_background()

    draw_pine_tree(350, 320)
    draw_pine_tree(450, 320)
    draw_bird(70, 500)
    draw_bird(100, 250)
    draw_bird(200, 360)

    # Draw a sun
    arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

    # Rays to the left, right, up, and down
    arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

    # Diagonal ray
    arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

    # --- Draw the tractor ---

    # Draw the engine
    arcade.draw_rectangle_filled(600, 120, 140, 70, arcade.color.GRAY)
    arcade.draw_rectangle_filled(590, 105, 90, 40, arcade.color.BLACK)

    # Draw the smoke stack
    arcade.draw_rectangle_filled(580, 175, 10, 40, arcade.color.BLACK)

    # Back wheel
    arcade.draw_circle_filled(490, 110, 50, arcade.color.BLACK)
    arcade.draw_circle_filled(490, 110, 45, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(490, 110, 35, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(490, 110, 10, arcade.color.RED)

    # Front wheel
    arcade.draw_circle_filled(650, 90, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(650, 90, 25, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(650, 90, 18, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(650, 90, 5, arcade.color.RED)
    # Tree trunk
    arcade.draw_rectangle_filled(250, 220, 20, 80, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(250, 250, 30, arcade.csscolor.DARK_GREEN)

    arcade.draw_ellipse_filled(200, 100, 200, 100, arcade.color.BLUE)

    # Draw the cloud
    arcade.draw_circle_filled(100, 600, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(140, 600, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(180, 600, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(120, 570, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(160, 570, 40, arcade.color.WHITE)

    # Finish the render.
    # Nothing will be drawn without this.
    # Must happen after all draw commands
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()


if __name__ == "__main__":
    main() 
