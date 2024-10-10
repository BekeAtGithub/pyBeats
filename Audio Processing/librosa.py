import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the audio file
file_path = 'input_audio.wav'
audio_data, sample_rate = librosa.load(file_path, sr=None)

# Display the waveform
plt.figure(figsize=(12, 4))
librosa.display.waveshow(audio_data, sr=sample_rate)
plt.title('Waveform of the Audio')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()

# Compute the Mel-frequency cepstral coefficients (MFCCs)
mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)

# Display the MFCCs
plt.figure(figsize=(12, 4))
librosa.display.specshow(mfccs, sr=sample_rate, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.xlabel('Time (s)')
plt.ylabel('MFCC Coefficients')
plt.show()

# Speed up the audio by 1.5x
audio_fast = librosa.effects.time_stretch(audio_data, rate=1.5)

# Save the modified audio to a new file
librosa.output.write_wav('output_audio_fast.wav', audio_fast, sample_rate)

print("Modified audio file 'output_audio_fast.wav' created successfully!")
