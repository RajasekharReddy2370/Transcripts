from pathlib import Path
import random
from pydub import AudioSegment, silence
from pydub.silence import detect_silence

clip_location = '/Users/c360/Desktop/voices/import/prabhakar voice.wav'

clip = AudioSegment.from_wav(clip_location)

all_clips = silence.split_on_silence(clip, min_silence_len=400, silence_thresh=-60, seek_step=1)
processed_clip = AudioSegment.empty()

for cut in all_clips:
    if cut.duration_seconds > 0.7:
        processed_clip += cut
    # if len(silence.detect_silence(cut)) != 0 and  cut.duration_seconds > 2:
    #     cuts_at_silence += cut[silence.detect_silence(cut)[0][0]:silence.detect_silence(cut)[0][1]]
    #     i += 1
    # elif cut.duration_seconds > 2:
    #     cuts_at_silence += cut

processed_clip.export('/Users/c360/Desktop/voices/prabhakar_sample_clip_cuttings/preprocessed_part_6.wav', 'wav', )