from pythonosc import udp_client
import time

# Set up the UDP client to communicate with SuperCollider
ip = "127.0.0.1"  # Localhost
port = 57110      # Default SuperCollider server port
client = udp_client.SimpleUDPClient(ip, port)

# Trigger the simple sine wave synth
freq = 440   # Frequency in Hz
amp = 0.5    # Amplitude (0.0 to 1.0)

print(f"Playing sine wave at {freq} Hz with amplitude {amp}")
client.send_message("/s_new", ["simpleSine", -1, 1, 0, "freq", freq, "amp", amp])

# Let the sound play for 2 seconds
time.sleep(2)

# Stop the sound by freeing the synth
client.send_message("/n_free", [1])

print("Sine wave stopped.")
