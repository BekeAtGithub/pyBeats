import csnd6

# Create an instance of the Csound object
cs = csnd6.Csound()

# Csound orchestra string defining a simple sine wave
orc = """
sr = 44100           ; Sample rate
ksmps = 32           ; Control rate
nchnls = 1           ; Number of channels (mono)
0dbfs = 1            ; Peak amplitude

instr 1
    aout oscils 0.5, 440, 0  ; Generate a sine wave with 0.5 amplitude and 440 Hz frequency
    out aout                 ; Output the audio signal
endin
"""

# Csound score defining the event to play the sine wave
sco = """
i1 0 2                  ; Play instrument 1, starting at 0 seconds, for 2 seconds
"""

# Compile the Csound orchestra and score
cs.compileOrc(orc)
cs.readScore(sco)

# Start Csound
cs.start()

# Perform Csound until the end of the score
cs.perform()

# Stop Csound
cs.stop()
cs.cleanup()

print("Sine wave generated successfully using Csound!")
