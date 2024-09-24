
import random
from pydub import AudioSegment, silence
from pydub.silence import detect_silence
from pydub.playback import play
from random import randint

clip_loc = '/home/rajashekar/Music/main/English_preprocessed_files/preprocessed_part_6.wav'
clip = AudioSegment.from_wav(clip_loc)

clips = silence.split_on_silence(clip, min_silence_len=165, silence_thresh=-60, seek_step=1)
print(len(clips))
for index, c in enumerate(clips):
    if int(c.duration_seconds) >= 2:
        if int(c.duration_seconds) > 9:
            # Break the clip into smaller clips based on silence
            sub_clips = silence.split_on_silence(c, min_silence_len=170, silence_thresh=-60, seek_step=1)
            for sub_index, sub_c in enumerate(sub_clips):
                sub_c.export(f'/home/rajashekar/Music/main/English_wav_files_above_10_sec/part_6/{index}_{sub_index}.wav', 'wav')
        else:
            c.export(f'/home/rajashekar/Music/main/English_wav_files_between_2_10_sec/part_6/{index}.wav', 'wav')
    else:
        print(int(c.duration_seconds))


