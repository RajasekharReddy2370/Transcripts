from pydub import AudioSegment
from pydub.silence import split_on_silence

# Load the audio file
audio = AudioSegment.from_file("/Users/c360/Desktop/voices/import/prabhakar voice.wav")
duration_in_seconds = audio.duration_seconds

# Define parameters for silence detection
# min_silence_len = 700  # Minimum silence length in milliseconds
min_silence_len = 200  # Minimum silence length in milliseconds
# silence_thresh = -30  # Silence threshold in dBFS
silence_thresh = -60  # Silence threshold in dBFS

# Split audio into chunks based on silence
chunks = split_on_silence(
    audio,
    min_silence_len=min_silence_len,
    silence_thresh=silence_thresh,
    keep_silence=True  # Keep silence at beginning and end of chunks
)

# Initialize a list to hold final chunks
final_chunks = []
# Iterate through each chunk
for i, chunk in enumerate(chunks):
    # Check if the chunk duration is above 10 seconds
    if len(chunk) >= 10000:  # Duration in milliseconds (10 seconds)
        # Split this chunk further based on a smaller silence length
        smaller_chunks = split_on_silence(
            chunk,
            min_silence_len=300,  # New minimum silence length
            silence_thresh=silence_thresh,
            keep_silence=True
        )
        # Extend final_chunks with the smaller chunks
        final_chunks.extend(smaller_chunks)
    else:
        # Append the chunk to final_chunks as is
        final_chunks.append(chunk)

# Export each chunk as a separate WAV file
for i, chunk in enumerate(final_chunks):
    print(i,chunk)
    chunk.export(f"/Users/c360/Desktop/voices/prabhakar_sample_clip_cuttings/chunk_{i}.wav", format="wav")

print(len(final_chunks))

#######################################################################################################################

