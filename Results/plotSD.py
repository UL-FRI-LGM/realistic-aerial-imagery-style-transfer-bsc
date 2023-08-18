import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def plot_images(image_paths, titles, save_path):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    for i, ax in enumerate(axes):
        image_path = image_paths[i]
        image = Image.open(image_path)
        image = image.resize((500, 500))
        image_array = np.array(image)
        ax.imshow(image_array)
        ax.set_title(titles[i])
        ax.axis('off')

    plt.tight_layout()

    plt.savefig(save_path)
    plt.close()  # Close the display window after saving

content_folder = 'Content'
stable_diffusion_folder = 'Stable diffusion'

output_folder = 'PlotsSD'
os.makedirs(output_folder, exist_ok=True)

for i in range(16):
    content_image = os.path.join(content_folder, f'i{i + 1}.png')
    stable_diffusion_image = os.path.join(stable_diffusion_folder, f'{i + 1}.png')

    plot_title = [f'Content {i + 1}', f'StableDiffusion {i + 1}']
    plot_save_path = os.path.join(output_folder, f'plot_{i + 1}.png')

    plot_images([content_image, stable_diffusion_image], plot_title, plot_save_path)
