from pydub import AudioSegment

# Load an audio file (supports various formats: mp3, wav, aiff, etc.)
audio = AudioSegment.from_file("input_audio.mp3", format="mp3")

# Apply some basic audio manipulations
# 1. Increase the volume by 6 dB
louder_audio = audio + 6

# 2. Apply a fade in over the first 2 seconds
faded_audio = louder_audio.fade_in(2000)

# 3. Split the audio in half and reverse the second half
halfway_point = len(faded_audio) // 2
first_half = faded_audio[:halfway_point]
second_half = faded_audio[halfway_point:].reverse()

# 4. Concatenate the original first half with the reversed second half
manipulated_audio = first_half + second_half

# Export the modified audio to a new file
manipulated_audio.export("output_audio.mp3", format="mp3")

print("Modified audio file 'output_audio.mp3' created successfully!")
