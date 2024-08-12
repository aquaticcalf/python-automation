from PIL import Image
import os


icon_sizes = [
    (72, 72),
    (96, 96),
    (128, 128),
    (144, 144),
    (152, 152),
    (192, 192),
    (384, 384),
    (512, 512)
]


def generate_icons(input_image_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with Image.open(input_image_path) as img:
        for size in icon_sizes:
            resized_img = img.resize(size, Image.LANCZOS)
            output_path = os.path.join(output_dir, f'icon-{size[0]}x{size[1]}.png')
            resized_img.save(output_path, 'PNG')


input_image_path = input("enter the path of the image: ")
output_dir = input("enter the path of the output directory: ")
generate_icons(input_image_path, output_dir)