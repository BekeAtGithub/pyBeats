from abletonremotepy import AbletonRemote
import time

# Set up the Ableton Remote connection
ableton = AbletonRemote('127.0.0.1', 9000)  # Default IP and port for LiveOSC

# Function to start playback
def start_playback():
    print("Starting playback...")
    ableton.start()
    time.sleep(1)

# Function to stop playback
def stop_playback():
    print("Stopping playback...")
    ableton.stop()
    time.sleep(1)

# Function to set the volume of track 0 (first track)
def set_volume(track_index, volume_level):
    print(f"Setting volume for track {track_index} to {volume_level}")
    ableton.set_track_volume(track_index, volume_level)

# Main script execution
if __name__ == "__main__":
    # Start playback
    start_playback()

    # Set volume of the first track to 0.5 (50%)
    set_volume(0, 0.5)

    # Let it play for 5 seconds
    time.sleep(5)

    # Stop playback
    stop_playback()

    print("Script execution completed.")
