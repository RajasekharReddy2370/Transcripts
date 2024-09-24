import os
from pydub import AudioSegment

# Set the folder path
folder_path = '/home/rajashekar/Music/English_Audio_Think_and_grow_rich/English_wav_files_above_10_sec/part_6'

# Set the starting number
start_number = 1721976600

# Loop through all WAV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.wav'):
        # Load the audio file
        audio = AudioSegment.from_wav(os.path.join(folder_path, filename))

        # Export the audio file with the new filename
        audio.export(
            f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/above_10sec_epoc_no/part_6/{start_number}_{filename}',
            format='wav')

        # Increment the start number
        # start_number += 1

print('Files renamed successfully!')