import os
import numpy as np
import matplotlib.pyplot as plt

# Function to read scores from a text file
def read_scores(file_path):
    scores = {}
    with open(file_path, 'r') as f:
        for line in f:
            metric, value = line.strip().split(': ')
            scores[metric] = float(value)
    return scores

# Initialize lists to store scores for different algorithms and metrics
metrics = ['ssim', 'psnr', 'lpips']  # Add more metrics if needed

algorithm_scores = {
    'wct2': {metric: [] for metric in metrics},
    'nst': {metric: [] for metric in metrics},
    'sd': {metric: [] for metric in metrics},
}

output_folder = 'Scores'

for i in range(9, 16):  # Images 10 to 16
    for algorithm in algorithm_scores.keys():
        score_path = os.path.join(output_folder, f'{algorithm.capitalize()}scores_{i + 1}.txt')
        scores = read_scores(score_path)
        
        for metric in metrics:
            algorithm_scores[algorithm][metric].append(scores[metric])

# Create plots for each metric
for metric in metrics:
    plt.figure(figsize=(10, 6))
    for algorithm, scores in algorithm_scores.items():
        plt.plot(range(10, 17), scores[metric], marker='o', label=algorithm.capitalize())
    
    plt.xlabel('Image Pair')
    plt.ylabel(f'{metric.upper()} Score')
    if metric == "ssim" or metric == "psnr":
        plt.title(f'{metric.upper()} Scores Comparison (Higher is better)')
    if metric == "lpips":
        plt.title(f'{metric.upper()} Scores Comparison (Lower is better)') 
    plt.legend()
    plt.grid(True)
    
    # Calculate and display average values
    for algorithm, scores in algorithm_scores.items():
        avg_value = np.mean(scores[metric])
        if avg_value >= np.mean(scores[metric]):
            va = 'bottom'  # Place the annotation below the line if the average is above the line
            offset = 0.05
        else:
            va = 'top'  # Place the annotation above the line if the average is below the line
            offset = -0.05
        plt.text(10, avg_value + offset, f'Avg {algorithm.capitalize()}: {avg_value:.2f}', va=va)
    
    plt.show()
