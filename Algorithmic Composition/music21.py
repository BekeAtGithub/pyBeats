from music21 import stream, note, midi, key

# Step 1: Create a Stream
melody = stream.Stream()

# Step 2: Add Notes to the Melody
notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
for pitch in notes:
    melody.append(note.Note(pitch, quarterLength=1))

# Step 3: Analyze the Key
melody_key = melody.analyze('key')
print(f"The key of the melody is: {melody_key.tonic.name} {melody_key.mode}")

# Step 4: Add the Key Signature to the Melody
melody.insert(0, key.KeySignature(melody_key.sharps))

# Step 5: Show the Music Notation (Optional, opens a music score viewer)
melody.show('text')  # Text representation
# melody.show()       # Standard music notation (requires MuseScore or another music editor installed)

# Step 6: Export the Melody as a MIDI File
midi_file_path = 'simple_melody.mid'
mf = midi.translate.music21ObjectToMidiFile(melody)
mf.open(midi_file_path, 'wb')
mf.write()
mf.close()

print(f"MIDI file '{midi_file_path}' created successfully!")
