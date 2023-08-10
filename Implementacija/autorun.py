import os
import argparse

def main(style_dir, content_dir):
    style_images = [f for f in os.listdir(style_dir) if f.startswith("style") and f.endswith(".jpg")]
    content_images = [f for f in os.listdir(content_dir) if f.startswith("content") and f.endswith(".jpg")]

    for style_image, content_image in zip(style_images, content_images):
        style_image_path = os.path.join(style_dir, style_image)
        content_image_path = os.path.join(content_dir, content_image)

        print(f"Running Neural Style Transfer for Style: {style_image_path} and Content: {content_image_path}")

        # Call the nst_batch.py script for the current pair of images
        os.system(f"python nst_batch.py --style_image {style_image_path} --content_image {content_image_path}")

        print("Finished Neural Style Transfer")

    print("All Neural Style Transfers completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch Neural Style Transfer")
    parser.add_argument("--style_dir", type=str, help="Directory containing style images")
    parser.add_argument("--content_dir", type=str, help="Directory containing content images")
    args = parser.parse_args()

    main(args.style_dir, args.content_dir)
