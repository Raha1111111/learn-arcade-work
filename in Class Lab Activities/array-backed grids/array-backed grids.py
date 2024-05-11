

import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Constants for grid setup
        self.WIDTH = 20
        self.HEIGHT = 20
        self.MARGIN = 5
        self.ROW_COUNT = 10
        self.COLUMN_COUNT = 10

        # Calculate total screen size
        self.SCREEN_WIDTH = (self.WIDTH + self.MARGIN) * self.COLUMN_COUNT + self.MARGIN
        self.SCREEN_HEIGHT = (self.HEIGHT + self.MARGIN) * self.ROW_COUNT + self.MARGIN

        # Initialize grid with all white squares
        self.grid = [[0 for _ in range(self.COLUMN_COUNT)] for _ in range(self.ROW_COUNT)]

        # Set background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        # Draw grid squares
        for row in range(self.ROW_COUNT):
            for column in range(self.COLUMN_COUNT):
                x = (self.MARGIN + self.WIDTH) * column + self.MARGIN + self.WIDTH / 2
                y = (self.MARGIN + self.HEIGHT) * row + self.MARGIN + self.HEIGHT / 2
                color = arcade.color.WHITE if self.grid[row][column] == 0 else arcade.color.GREEN
                arcade.draw_rectangle_filled(x, y, self.WIDTH, self.HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        # Convert screen coordinates to grid coordinates
        column = x // (self.WIDTH + self.MARGIN)
        row = y // (self.HEIGHT + self.MARGIN)

        # Toggle the color of the clicked square
        if 0 <= row < self.ROW_COUNT and 0 <= column < self.COLUMN_COUNT:
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

def main():
    game = MyGame(255, 255, "Grid Game")
    arcade.run()


if __name__ == "__main__":
    main()