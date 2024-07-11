from PIL import Image
import os

def crop_sprites(image_path, num_rows, num_cols, output_path):
    image = Image.open(image_path)
    image_width, image_height = image.size
    
    sprite_width = image_width // num_cols
    sprite_height = image_height // num_rows

    os.makedirs(output_path, exist_ok=True)  # Create the output directory if it doesn't exist

    for row in range(num_rows):
        for col in range(num_cols):
            left = col * sprite_width
            upper = row * sprite_height
            right = (col + 1) * sprite_width
            lower = (row + 1) * sprite_height

            sprite_image = image.crop((left, upper, right, lower))
            sprite_image.save(f"{output_path}/sprite_{row}_{col}.png")

    print(f"{num_rows * num_cols} sprites have been saved to {output_path}.")

# Example usage
image_path = "image_23.png"
num_rows = 4  # Number of rows in the spritesheet
num_cols = 4  # Number of columns in the spritesheet
output_path = "output_sprites"

crop_sprites(image_path, num_rows, num_cols, output_path)
