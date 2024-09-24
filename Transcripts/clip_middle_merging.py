# import os
# from pydub import AudioSegment
# from pydub.silence import detect_silence
#
# # Define the folder path and the output file path
# folder_path = '/home/rajashekar/Music/English_Audio_Think_and_grow_rich/test1/3'
#
# # Initialize an empty list to store the 3-second WAV files
# three_second_files = []
#
# # Iterate over the files in the folder
# for filename in os.listdir(folder_path):
#     # Check if the file is a WAV file
#     if filename.endswith('.wav'):
#         file = filename
#         # Get the file path
#         file_path = os.path.join(folder_path, filename)
#
#         # Open the WAV file using PyDub
#         audio = AudioSegment.from_wav(file_path)
#
#         # Check if the file duration is 3 seconds
#         if len(audio) >= 3501 and len(audio) <=4500:  # 3000 milliseconds = 3 seconds
#             # Add the file to the list
#             three_second_files.append(audio)
#         else:
#             audio.export(f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/test1/4/{file}',format = 'wav')
# print(len(three_second_files))
#
# # Take only the first 250 files
# three_second_files = three_second_files[:108]
#
# # Merge files in pairs
# merged_files = []
# for i in range(0, len(three_second_files), 2):
#     file1 = three_second_files[i]
#     file2 = three_second_files[i+1]
#
#     # Remove ending silence from file1
#     silence_segments = detect_silence(file1, min_silence_len=150, silence_thresh=-60)
#     if silence_segments:
#         file1 = file1[:silence_segments[-1][0]]
#
#     # Remove starting silence from file2
#     silence_segments = detect_silence(file2.reverse(), min_silence_len=150, silence_thresh=-60)
#     if silence_segments:
#         file2 = file2[silence_segments[-1][1]:].reverse()
#
#     # Add 240ms silence between the two files
#     silence_segment = AudioSegment.silent(duration=200)
#
#     # Merge the files with adjusted silence
#     merged_file = file1 + silence_segment + file2
#     merged_files.append(merged_file)
#
# print(len(merged_files))
#
# # Export the merged files
# for i, merged_file in enumerate(merged_files):
#     merged_file.export(f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/test1/4/file_{i+1}.wav', format='wav')
# # # Export remaining files that were not merged
# remaining_files = three_second_files[108:]
# for j, audio in enumerate(remaining_files):
#     # output_path = os.path.join(output_folder, f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/test1/full_files_aftr_merging/file_{len(merged_files) + j + 1}.wav')
#     audio.export(f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/test1/4/file_{len(merged_files) + j + 1}.wav', format='wav')

# import os
# from pydub import AudioSegment
# from pydub.silence import detect_silence
#
# # Define folder paths
# folder_path = '/home/rajashekar/Music/English_Audio_Think_and_grow_rich/test1/full_files_aftr_merging'
# # output_folder = '/home/rajashekar/Music/English_Audio_Think_and_grow_rich/test1/4_sec_108_merged/'
#
# # Initialize variables
# three_second_files = []
# min_silence_len = 150  # Minimum silence length in milliseconds
# silence_thresh = -60  # Silence threshold in dB
#
# # Function to remove silence from the beginning or end of an audio segment
# def remove_silence(audio_segment, start=False):
#     if start:
#         silence_segments = detect_silence(audio_segment, min_silence_len=min_silence_len, silence_thresh=silence_thresh)
#         if silence_segments:
#             audio_segment = audio_segment[silence_segments[-1][1]:]
#     else:
#         silence_segments = detect_silence(audio_segment.reverse(), min_silence_len=min_silence_len, silence_thresh=silence_thresh)
#         if silence_segments:
#             audio_segment = audio_segment[:silence_segments[-1][0]].reverse()
#     return audio_segment
#
# # Iterate over WAV files in the folder
# for filename in os.listdir(folder_path):
#     if filename.endswith('.wav'):
#         file = filename
#         file_path = os.path.join(folder_path, filename)
#         audio = AudioSegment.from_wav(file_path)
#
#         # Check if duration is between 2.5 to 3.5 seconds (2500 to 3500 milliseconds)
#         if 3500 <= len(audio) <= 4500:
#             three_second_files.append(audio)
#         else :
#             audio.export(f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/test1/after_merging/{file}',format = 'wav')
#
# # Ensure we have at least 108 files
# three_second_files = three_second_files[:108]
#
# # Merge files in pairs
# merged_files = []
# for i in range(0, len(three_second_files), 2):
#     file1 = three_second_files[i]
#     file2 = three_second_files[i + 1] if i + 1 < len(three_second_files) else None
#
#     # Remove silence from the ends
#     file1 = remove_silence(file1, start=True)
#     if file2:
#         file2 = remove_silence(file2)
#
#     # Add 200ms of silence between files
#     silence_segment = AudioSegment.silent(duration=200)
#     merged_file = file1 + silence_segment + (file2 if file2 else AudioSegment.silent(duration=0))
#     merged_files.append(merged_file)
#
# # Export merged files
# for i, merged_file in enumerate(merged_files):
#     # output_path = os.path.join(output_folder, f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/test1/full_files_aftr_merging/file_{i+1}.wav')
#     merged_file.export(f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/test1/after_merging/file_{i+1}.wav', format='wav')
#
# # Export remaining files that were not merged
# remaining_files = three_second_files[108:]
# for j, audio in enumerate(remaining_files):
#     # output_path = os.path.join(output_folder, f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/test1/full_files_aftr_merging/file_{len(merged_files) + j + 1}.wav')
#     audio.export(f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/test1/after_merging/file_{len(merged_files) + j + 1}.wav', format='wav')


from pathlib import Path
import os
from pydub import AudioSegment

main_folder = '/home/rajashekar/Music/English_Audio_Think_and_grow_rich/silence_added_files'

all_clips = []

for num in range(1,7):
    for file in os.listdir(f'{main_folder}/part_{num}'):
        all_clips.append(f'{main_folder}/part_{num}/{file}')

sample_dict = {}
for clip in all_clips:
    dur = round(AudioSegment.from_wav(clip).duration_seconds)
    if dur in sample_dict.keys():
        sample_dict[dur].append(clip)
    else:
        sample_dict[dur] = []
        sample_dict[dur].append(clip)

for key, val in sample_dict.items():
    print(key, len(val))

def clip_merge(data: list, count: int):
    if count/2 == 0:
        pass
    else:
        count -= 1
    Path('/home/rajashekar/Music/English_Audio_Think_and_grow_rich/silence_added_files/Merged').mkdir(exist_ok=True, parents=True)
    new_data = zip(data[:count:2], data[1:count:2])
    for idx, data in enumerate(new_data):
        new_clip = AudioSegment.from_wav(data[0])[:-150] + AudioSegment.from_wav(data[1])
        new_clip.export(f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/silence_added_files/Merged/merged_{round(AudioSegment.from_wav(data[0]).duration_seconds)}_{round(AudioSegment.from_wav(data[1]).duration_seconds)}_{idx}.wav', 'wav')
        Path(data[0]).unlink()
        Path(data[1]).unlink()

clip_merge(sample_dict[3], 550)