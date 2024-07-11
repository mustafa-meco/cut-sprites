from PIL import Image

def crop_sprites(image_path, num_moves, output_path):
    image = Image.open(image_path)
    image_width, image_height = image.size
    
    sprite_width = image_width // num_moves
    sprite_height = image_height

    for i in range(num_moves):
        left = i * sprite_width
        upper = 0
        right = (i + 1) * sprite_width
        lower = sprite_height

        if right > image_width:
            break

        sprite_image = image.crop((left, upper, right, lower))
        sprite_image.save(f"{output_path}/sprite_{i}.png")

    print(f"{num_moves} sprites have been saved to {output_path}.")

# Example usage
image_path = "download-removebg-preview.png"
num_moves = 4  # Number of moves in the spritesheet
output_path = "output_sprites"

crop_sprites(image_path, num_moves, output_path)
