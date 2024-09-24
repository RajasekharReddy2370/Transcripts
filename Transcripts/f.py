import os
from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Function to get duration of a WAV file
def get_wav_duration(file_path):
    audio = AudioSegment.from_file(file_path)
    return len(audio) / 1000  # Convert milliseconds to seconds

# Initialize a dictionary to store duration counts
duration_counts = {}

# Iterate over each WAV file in the folder
folder_path = '/home/rajashekar/Music/English_Audio_Think_and_grow_rich/silence_added_files'
for folder in os.listdir(folder_path):
    for file_name in os.listdir(os.path.join(folder_path, folder)):
        if file_name.endswith('.wav'):
            file_path = os.path.join(folder_path, folder, file_name)
            # Get the duration of the WAV file in seconds
            duration = get_wav_duration(file_path)
            # Increment the count for this duration
            duration_counts[round(duration)] = duration_counts.get(round(duration), 0) + 1

# Extract durations and counts from the dictionary
durations = sorted(duration_counts.keys())
counts = [duration_counts[duration] for duration in durations]

# Calculate total clips and average percentage
total_clips = sum(counts)  # Total number of clips

# Plot the bar graph
plt.figure(figsize=(10, 6))
bars = plt.bar(durations, counts, color='blue', alpha=0.7)
plt.xlabel('Duration (seconds)')
plt.ylabel('Count')
plt.title('Bar Graph of WAV File Durations')
plt.xticks(durations)  # Set x-axis ticks to durations

# Add count and percentage labels on top of the bars
for bar in bars:
    height = bar.get_height()
    percentage = (height / total_clips) * 100
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height} ({percentage:.2f}%)', ha='center', va='bottom')

# Annotate total clips and average percentage
plt.text(0.95, 0.95, f'Total Clips: {total_clips}', transform=plt.gca().transAxes, ha='right', fontsize=12, color='green')
plt.text(0.95, 0.90, f'Average Percentage: {(100 / 9):.2f}%', transform=plt.gca().transAxes, ha='right', fontsize=12, color='green')
plt.text(0.95, 0.85, f'Clips/Percentage: {round(total_clips / 100)}', transform=plt.gca().transAxes, ha='right', fontsize=12, color='green')

plt.tight_layout()
# plt.savefig('/home/rajashekar/Music/English_Audio_Think_and_grow_rich/graphs/bar_plot.png')
plt.show()

# Plot the bell curve (normal distribution)
plt.figure(figsize=(8, 6))
mu, std = np.mean(durations), np.std(durations)
x = np.linspace(min(durations), max(durations), 100)
plt.plot(x, norm.pdf(x, mu, std), color='red', label='Normal Distribution')
plt.title('Bell Curve Plot of WAV File Durations')
plt.xlabel('Duration (seconds)')
plt.ylabel('Density')
plt.legend()

plt.tight_layout()
plt.savefig('/home/rajashekar/Music/English_Audio_Think_and_grow_rich/graphs/bell_curve_plot.png')
plt.show()
