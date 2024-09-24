from pydub import AudioSegment
import os

folder_path = '/home/rajashekar/Music/English_Audio_Think_and_grow_rich/English_wav_files_between_2_10_sec/part_6'

for filename in os.listdir(folder_path):
    if filename.endswith('.wav'):
        file_path = os.path.join(folder_path, filename)
        audio = AudioSegment.from_wav(file_path)
        silence = AudioSegment.silent(duration=150)
        silence = silence.apply_gain(-60)
        audio_with_silence = silence + audio + silence
        audio_with_silence.export(f'/home/rajashekar/Music/English_Audio_Think_and_grow_rich/SAF/part_6/{filename}', format='wav')