import os
import wave
import pandas as pd

folder_path = "/home/rajashekar/Music/wav_folder"

#C:\Users\SriramineniSindu\Documents\bp\PratapReddy_Clips_3000
wav_files = [file for file in os.listdir(folder_path) if file.endswith('.wav')]

data = []

for wav_file_name in wav_files:
    file_path = os.path.join(folder_path, wav_file_name)
    
    with wave.open(file_path, 'rb') as wav_file:
        params = wav_file.getparams()
        sample_rate = params.framerate
        pcm_format = params.sampwidth * 8 
        duration = params.nframes / float(sample_rate) 
        num_channels = params.nchannels
        channel_info = 'Mono' if num_channels == 1 else 'Stereo'

    audio_clip_name = os.path.splitext(wav_file_name)[0]
    
    data.append({'File Name': audio_clip_name, 'Sample Rate (Hz)': sample_rate, 'PCM Format (bits)': pcm_format, 'Duration (s)': duration, 'Channels': channel_info})
        
    
    #data.append({'File Name': wav_file, 'Sample Rate (Hz)': sample_rate, 'PCM Format (bits)': pcm_format, 'Duration (s)': duration, 'Channels': channel_info})

df = pd.DataFrame(data)


excel_file_path = 'output.xlsx'


df.to_excel(excel_file_path, index=False)

print(f'Data has been written to {excel_file_path}')

