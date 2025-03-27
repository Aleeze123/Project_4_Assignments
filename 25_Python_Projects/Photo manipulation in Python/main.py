from PIL import Image, ImageEnhance, ImageFilter
import os
from termcolor import colored

def change_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def change_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def apply_blur(image, radius):
    return image.filter(ImageFilter.GaussianBlur(radius))

def open_image(file_path):
    try:
        image = Image.open(file_path)
        print(colored(f"Image loaded successfully: {file_path}", 'green'))
        return image
    except FileNotFoundError:
        print(colored(f"Error: The file at {file_path} was not found.", 'red'))
    except Exception as e:
        print(colored(f"An error occurred: {e}", 'red'))
    return None

def save_image(image, output_path):
    try:
        image.save(output_path)
        print(colored(f"Image saved successfully to {output_path}", 'green'))
    except Exception as e:
        print(colored(f"Failed to save image: {e}", 'red'))

def process_images(input_paths, output_paths):
    for i in range(len(input_paths)):
        input_path = input_paths[i]
        output_path = output_paths[i]
        
        image = open_image(input_path)
        if not image:
            continue

        contrast_factor = 1.5
        image = change_contrast(image, contrast_factor)

        brightness_factor = 1.2
        image = change_brightness(image, brightness_factor)

        blur_radius = 2
        image = apply_blur(image, blur_radius)

        save_image(image, output_path)

def main():
    input_paths = ["input_image1.jpg", "input_image2.jpg"]
    output_paths = ["output_image1.jpg", "output_image2.jpg"]
    process_images(input_paths, output_paths)

if __name__ == "__main__":
    main()
