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
    Path('/home/rajashekar/Music/English_Audio_Think_and_grow_rich/MERGED/Merged').mkdir(exist_ok=True, parents=True)
    new_data = zip(data[:count:2], data[1:count:2])
    for idx, data in enumerate(new_data):
        new_clip = AudioSegment.from_wav(data[0])[:-150] + AudioSegment.from_wav(data[1])
        new_clip.export(f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/MERGED/Merged/merged_{round(AudioSegment.from_wav(data[0]).duration_seconds)}_{round(AudioSegment.from_wav(data[1]).duration_seconds)}_{idx}.wav', 'wav')
        Path(data[0]).unlink()
        Path(data[1]).unlink()

clip_merge(sample_dict[4], 100)