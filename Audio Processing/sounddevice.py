import sounddevice as sd
import numpy as np
import wavio

# Parameters for recording
duration = 5  # seconds
sample_rate = 44100  # Hz (samples per second)

# Record audio
print("Recording...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype=np.float32)
sd.wait()  # Wait until the recording is finished
print("Recording complete.")

# Play back the recorded audio
print("Playing back...")
sd.play(audio_data, samplerate=sample_rate)
sd.wait()  # Wait until the playback is finished
print("Playback complete.")

# Save the audio to a WAV file
output_filename = 'recorded_audio.wav'
wavio.write(output_filename, audio_data, sample_rate, sampwidth=3)
print(f"Audio saved to '{output_filename}'.")
