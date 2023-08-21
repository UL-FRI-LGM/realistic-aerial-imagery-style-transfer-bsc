import os
import skimage.metrics as metrics
import numpy as np
from PIL import Image
import lpips

def image_comparison_matrices(image1, image2):
    """
    Calculates and returns the SSIM, PSNR, LPIPS, and VMAF scores for two images.

    Args:
      image1: The first image.
      image2: The second image.

    Returns:
      A dictionary containing the SSIM, PSNR, LPIPS, and VMAF scores.
    """
    image1_resized = image1.resize((500, 500))
    image2_resized = image2.resize((500, 500))
    
    image1_array = np.array(image1_resized)
    image2_array = np.array(image2_resized)

    # Ensure both images have the same number of channels (convert to RGB)
    if image1_array.shape[2] == 4 and image2_array.shape[2] == 3:
        image1_array = image1_array[:, :, :3]

    if image1_array.shape[2] == 3 and image2_array.shape[2] == 4:
        image2_array = image2_array[:, :, :3]

    scores = {}
    scores["ssim"] = metrics.structural_similarity(image1_array, image2_array, win_size=3)
    scores["psnr"] = metrics.peak_signal_noise_ratio(image1_array, image2_array)
    
    # Using LPIPS directly from the lpips package
    lpips_calculator = lpips.LPIPS(net='alex', verbose=True)
    image1_tensor = lpips.im2tensor(image1_array)
    image2_tensor = lpips.im2tensor(image2_array)
    scores["lpips"] = lpips_calculator(image1_tensor, image2_tensor).item()
    
    #scores["vmaf"] = ffmpeg_quality_metrics.(image1_array, image2_array, "vmaf")
    return scores

def compute_and_print_scores(image_folder1, image_folder2, output_folder, folder):
    for i in range(9, 16):  # Images 10 to 16
        image_path1 = os.path.join(image_folder1, f's{i + 1}.png')
        image_path2 = os.path.join(image_folder2, f'o{i + 1}.png')

        image1 = Image.open(image_path1)
        image2 = Image.open(image_path2)

        scores = image_comparison_matrices(image1, image2)

        print(f'Image Pair {i + 1}:')
        print("SSIM:", scores["ssim"])
        print("PSNR:", scores["psnr"])
        print("LPIPS:", scores["lpips"])
        #print("VMAF:", scores["vmaf"])
        print("-" * 30)

        # Save scores to a text file
        if folder == "WCT2":
            score_output_path = os.path.join(output_folder, f'WCT2scores_{i + 1}.txt')
        if folder == "NST":
            score_output_path = os.path.join(output_folder, f'NSTscores_{i + 1}.txt')
        if folder == "SD":
            score_output_path = os.path.join(output_folder, f'SDscores_{i + 1}.txt')       
        with open(score_output_path, 'w') as f:
            for metric, value in scores.items():
                f.write(f'{metric}: {value}\n')

style_folder = 'Style'
wct2_folder = 'WCT2'
nst_folder = 'NST'
stable_diffusion_folder = 'Stable Diffusion'
output_folder = 'Scores'

os.makedirs(output_folder, exist_ok=True)

compute_and_print_scores(style_folder, wct2_folder, output_folder, "WCT2")
compute_and_print_scores(style_folder, nst_folder, output_folder, "NST")
compute_and_print_scores(style_folder, stable_diffusion_folder, output_folder, "SD")
