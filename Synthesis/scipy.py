import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# Parameters for the sine wave
sample_rate = 44100  # Sample rate in Hz
duration = 2.0       # Duration in seconds
frequency = 440.0    # Frequency of the sine wave (A4 note)

# Generate the time axis for the signal
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate the sine wave signal
amplitude = 0.5  # Amplitude of the sine wave
sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)

# Plot the sine wave
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], sine_wave[:1000])  # Plot only the first 1000 samples for clarity
plt.title(f'Sine Wave: {frequency} Hz')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Save the sine wave as a WAV file
output_filename = 'sine_wave_440Hz.wav'
write(output_filename, sample_rate, (sine_wave * 32767).astype(np.int16))
print(f"Audio file '{output_filename}' created successfully!")
