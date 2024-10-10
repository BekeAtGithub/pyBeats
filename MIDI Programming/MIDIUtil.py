from midiutil import MIDIFile

# Create a MIDIFile object with 1 track
track = 0
time = 0    # Start at the beginning
midi_file = MIDIFile(1)  # One track
midi_file.addTempo(track, time, 120)  # Set the tempo (120 BPM)

# Add notes to the MIDI file
# Parameters are: track, channel, pitch, time, duration, volume
notes = [
    (60, 1),  # C4, 1 beat
    (62, 1),  # D4, 1 beat
    (64, 1),  # E4, 1 beat
    (65, 1),  # F4, 1 beat
    (67, 1),  # G4, 1 beat
    (69, 1),  # A4, 1 beat
    (71, 1),  # B4, 1 beat
    (72, 1),  # C5, 1 beat
]

time = 0  # Start time for the first note
volume = 100  # Volume (0-127)

for pitch, duration in notes:
    midi_file.addNote(track, 0, pitch, time, duration, volume)
    time += duration  # Move to the next time for the next note

# Write the MIDI file to disk
with open("simple_melody.mid", "wb") as output_file:
    midi_file.writeFile(output_file)

print("MIDI file 'simple_melody.mid' created successfully!")
