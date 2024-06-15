
from graphics import Canvas

# Constants
BOX_SIZE = 80
N_BOXES = 5

def main():
    # Create a canvas
    canvas = Canvas(width=BOX_SIZE * N_BOXES, height=200, title="Line of Boxes")

    # Create a line of boxes
    for i in range(N_BOXES):
        left_x = i * BOX_SIZE
        top_y = 120
        right_x = left_x + BOX_SIZE
        bottom_y = 200
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, "white", "black")

    # Display the canvas
    canvas.mainloop()

if __name__ == "__main__":
    main()
