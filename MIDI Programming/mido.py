import mido
from mido import MidiFile, MidiTrack, Message

# Create a new MIDI file and add a track
midi_file = MidiFile()
track = MidiTrack()
midi_file.tracks.append(track)

# Set the tempo (120 BPM)
tempo = mido.bpm2tempo(120)
track.append(mido.MetaMessage('set_tempo', tempo=tempo))

# Define a simple melody (MIDI note numbers for C4, D4, E4, etc.)
notes = [60, 62, 64, 65, 67, 69, 71, 72]  # C4 to C5
duration = 480  # Duration of each note in ticks

# Add the notes to the track
for note in notes:
    track.append(Message('note_on', note=note, velocity=64, time=0))  # Note on
    track.append(Message('note_off', note=note, velocity=64, time=duration))  # Note off

# Save the MIDI file
midi_file.save('simple_melody_mido.mid')

print("MIDI file 'simple_melody_mido.mid' created successfully!")
