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

        # Set background color to a soothing blue shade
        arcade.set_background_color(arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()
        # Draw grid squares with borders for clarity
        for row in range(self.ROW_COUNT):
            for column in range(self.COLUMN_COUNT):
                x = (self.MARGIN + self.WIDTH) * column + self.MARGIN + self.WIDTH / 2
                y = (self.MARGIN + self.HEIGHT) * row + self.MARGIN + self.HEIGHT / 2
                if self.grid[row][column] == 0:
                    color = arcade.color.ASH_GREY
                else:
                    color = arcade.color.APPLE_GREEN
                arcade.draw_rectangle_filled(x, y, self.WIDTH, self.HEIGHT, color)
                # Draw a border around each cell
                arcade.draw_rectangle_outline(x, y, self.WIDTH, self.HEIGHT, arcade.color.BLACK)

    def on_mouse_press(self, x, y, button, modifiers):
        column = int(x // (self.WIDTH + self.MARGIN))
        row = int(y // (self.HEIGHT + self.MARGIN))

        # Toggle the color of the clicked square and adjacent squares
        self.toggle_square(row, column)
        self.toggle_square(row-1, column)  # Above
        self.toggle_square(row+1, column)  # Below
        self.toggle_square(row, column-1)  # Left
        self.toggle_square(row, column+1)  # Right

        # Logging selection details
        self.log_selection_details()

    def toggle_square(self, row, column):
        # Safely toggle square state if within bounds
        if 0 <= row < self.ROW_COUNT and 0 <= column < self.COLUMN_COUNT:
            self.grid[row][column] = 1 - self.grid[row][column]

    def log_selection_details(self):
        total_selected = sum(sum(row) for row in self.grid)
        print(f"Total of {total_selected} cells are selected.")
        for r, row in enumerate(self.grid):
            row_selected = sum(row)
            print(f"Row {r} has {row_selected} cells selected.")

def main():
    game = MyGame(255, 255, "Customized Grid Game")
    arcade.run()

if __name__ == "__main__":
    main()
