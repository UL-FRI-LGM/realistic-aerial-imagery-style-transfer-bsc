import os
import matplotlib.pyplot as plt
from PIL import Image

def plot_images(image_paths, titles, save_path):
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))

    for i, ax in enumerate(axes):
        image_path = image_paths[i]
        image = Image.open(image_path)
        image = image.resize((500, 500))
        ax.imshow(image)
        ax.set_title(titles[i])
        ax.axis('off')

    plt.tight_layout()

    plt.savefig(save_path)
    plt.show()

style_folder = 'Style'
content_folder = 'Content'
wct2_folder = 'WCT2'
nst_folder = 'NST'

output_folder = 'Plots'
os.makedirs(output_folder, exist_ok=True)

for i in range(16):
    style_image = os.path.join(style_folder, f's{i + 1}.png')
    content_image = os.path.join(content_folder, f'i{i + 1}.png')
    wct2_image = os.path.join(wct2_folder, f'i{i + 1}.png')
    nst_image = os.path.join(nst_folder, f'o{i + 1}.png')

    plot_title = [f'Style {i + 1}', f'Content {i + 1}', f'WCT2 {i + 1}', f'NST {i + 1}']
    plot_save_path = os.path.join(output_folder, f'plot_{i + 1}.png')

    plot_images([style_image, content_image, wct2_image, nst_image], plot_title, plot_save_path)
