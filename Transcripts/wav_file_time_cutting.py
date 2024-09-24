import datetime
from moviepy.audio.io.AudioFileClip import AudioFileClip

# Overall time of the audio file
overall_time = datetime.timedelta(hours=1, minutes=35, seconds=0)

# Duration of each part
part_duration = datetime.timedelta(hours=0, minutes=2, seconds=0)

# Open the audio file
audio = AudioFileClip("/home/rajashekar/Music/main/parts2/part_1_0_00_00.wav")

# Sample rate
sample_rate = 22050

# Calculate number of parts
num_parts = int((overall_time.total_seconds() + part_duration.total_seconds() - 1) // part_duration.total_seconds())

# Initialize start time
start_time = datetime.timedelta()

# Iterate over each part
for i in range(num_parts):
    # Calculate end time for this part
    end_time = start_time + part_duration

    # Ensure end time does not exceed overall time
    if end_time > overall_time:
        end_time = overall_time

    # Convert time to seconds
    start_seconds = start_time.total_seconds()
    end_seconds = end_time.total_seconds()

    # Extract subclip and save as WAV
    start_time_str = str(start_time).replace(':', '_')  # Replace ':' with '_' for filename compatibility
    wav_filename = f"/home/rajashekar/Music/main/parts2/sample_part_{i + 1}_{start_time_str}.wav"
    subclip = audio.subclip(start_seconds, end_seconds)
    subclip.write_audiofile(wav_filename, codec='pcm_s16le', fps=sample_rate)

    # Print or use the start and end times for each part
    print(f"Part {i + 1}:")
    print(f"Start time: {start_time}")
    print(f"End time: {end_time}")
    print(f"Saved as: {wav_filename}")
    print()

    # Update start time for the next part
    start_time = end_time + datetime.timedelta(seconds=1)  # Move start time to the next second after end_time
    break
# Close the audio file
audio.close()
