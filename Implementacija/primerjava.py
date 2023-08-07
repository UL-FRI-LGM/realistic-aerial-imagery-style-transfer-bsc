import skimage.metrics as metrics
from PIL import Image

def image_comparison_matrices(image1, image2):
  """
  Calculates and prints the SSIM, PSNR, LPIPS, and VMAF scores for two images.

  Args:
    image1: The first image.
    image2: The second image.

  Returns:
    A dictionary containing the SSIM, PSNR, LPIPS, and VMAF scores.
  """

  scores = {}
  scores["ssim"] = metrics.structural_similarity(image1, image2)
  scores["psnr"] = metrics.peak_signal_to_noise_ratio(image1, image2)
  scores["lpips"] = metrics.lpips(image1, image2)
  scores["vmaf"] = metrics.vmaf(image1, image2)

  return scores

if __name__ == "__main__":
  path1 = 
  path2 =
  image1 = Image.open(path1)

  image2 = Image.open(path2)

  scores = image_comparison_matrices(image1, image2)

  print("SSIM:", scores["ssim"])
  print("PSNR:", scores["psnr"])
  print("LPIPS:", scores["lpips"])
  print("VMAF:", scores["vmaf"])
