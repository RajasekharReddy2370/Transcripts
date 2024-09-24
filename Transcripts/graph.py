import os
from pydub import AudioSegment
import matplotlib.pyplot as plt

# Function to get duration of a WAV file
def get_wav_duration(file_path):
    audio = AudioSegment.from_file(file_path)
    return len(audio) / 1000  # Convert milliseconds to seconds

# Initialize a dictionary to store duration counts
duration_counts = {}

# Iterate over each WAV file in the folder
folder_path = '/home/rajashekar/Music/English_Audio_Think_and_grow_rich/FINAL_FILES'
for folder in os.listdir(folder_path):
    for file_name in os.listdir(folder_path+'/'+folder):

        if file_name.endswith('.wav'):
            file_path = os.path.join(folder_path, folder,file_name)
            # Get the duration of the WAV file in seconds
            duration = get_wav_duration(file_path)
            # Increment the count for this duration
            duration_counts[round(duration)] = duration_counts.get(round(duration), 0) + 1

# Extract durations and counts from the dictionary
durations = sorted(duration_counts.keys())
counts = [duration_counts[duration] for duration in durations]

# Plot the bar graph
plt.figure(figsize=(10, 6))
bars = plt.bar(durations, counts, color='blue', alpha=0.7)
plt.xlabel('Duration (seconds)')
plt.ylabel('Count')
plt.title('FINAL GRAPH')
plt.xticks(durations)  # Set x-axis ticks to durations

# Add count and percentage labels on top of the ba
total_clips = sum(counts)  # Total number of clips
for bar in bars:
    height = bar.get_height()
    percentage = (height / total_clips) * 100
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height} ({percentage:.2f}%)', ha='center', va='bottom')

# Annotate total clips and average percentage
plt.text(0.95, 0.95, f'Total Clips: {total_clips}', transform=plt.gca().transAxes, ha='right', fontsize=12,color = 'green')
plt.text(0.95, 0.90, f'Average Percentage: {(100 / 9):.2f}%', transform=plt.gca().transAxes, ha='right', fontsize=12,color = 'green')
plt.text(0.95, 0.85, f'Clips/Percentage: {round(total_clips / 100)}', transform=plt.gca().transAxes, ha='right', fontsize=12, color='green')
plt.tight_layout()
plt.savefig('/home/rajashekar/Music/English_Audio_Think_and_grow_rich/graphs/bar_plot7.png')
plt.show()
