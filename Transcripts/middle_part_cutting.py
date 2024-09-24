import datetime
from moviepy.audio.io.AudioFileClip import AudioFileClip

# Overall time of the audio file
overall_time = datetime.timedelta(hours=1, minutes=35, seconds=0)

# Start and end times of the segment you want to extract
start_time = datetime.timedelta(seconds=31)
end_time = datetime.timedelta(minutes=10, seconds=00)

# Open the audio file
audio = AudioFileClip("/home/rajashekar/Music/main/parts2/part_1_0_00_00.wav")

# Sample rate
sample_rate = 22050

# Convert start and end times to seconds
start_seconds = start_time.total_seconds()
end_seconds = end_time.total_seconds()

# Ensure end time does not exceed overall time
if end_seconds > overall_time.total_seconds():
    end_seconds = overall_time.total_seconds()

# Extract subclip and save as WAV
wav_filename = "/home/rajashekar/Music/main/parts2/ten_minutes_middle_part.wav"
subclip = audio.subclip(start_seconds, end_seconds)
subclip.write_audiofile(wav_filename, codec='pcm_s16le', fps=sample_rate)

# Print or use the start and end times of the custom segment
print("Custom Part:")
print(f"Start time: {start_time}")
print(f"End time: {end_time}")
print(f"Saved as: {wav_filename}")

# Close the audio file
audio.close()
