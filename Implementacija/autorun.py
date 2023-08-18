import os
import argparse
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def main(style_dir, content_dir):
    style_images = [f for f in os.listdir(style_dir) if f.startswith("s") and f.endswith(".png")]
    content_images = [f for f in os.listdir(content_dir) if f.startswith("i") and f.endswith(".png")]
    i = 1
    
    # Sort the images to ensure correct order
    style_images.sort(key=natural_sort_key)
    content_images.sort(key=natural_sort_key)
    
    for style_image, content_image in zip(style_images, content_images):
        style_image_path = os.path.join(style_dir, style_image)
        content_image_path = os.path.join(content_dir, content_image)
        print(f"Running NST nr.{i} for: {style_image_path} and Content: {content_image_path}")

        # Call the nst_batch.py script for the current pair of images
        os.system(f"python implementacija/nst.py --style_image {style_image_path} --content_image {content_image_path} --i {i}")

        print(f"Finished Neural Style Transfer nr.{i}")
        i = i+1

    print(f"All Neural Style Transfers completed. Total number {i}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch Neural Style Transfer")
    parser.add_argument("--style_dir", default="Style", type=str, help="Directory containing style images")
    parser.add_argument("--content_dir", default="Input", type=str, help="Directory containing content images")
    args = parser.parse_args()

    main(args.style_dir, args.content_dir)
