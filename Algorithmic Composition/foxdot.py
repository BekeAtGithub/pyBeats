from FoxDot import *

# Start a drum beat
d1 >> play("x-o-")

# Add a bassline
b1 >> bass([0, 2, 4, 5], dur=1/2)

# Add a melody
p1 >> pluck([0, 2, 4, 7], dur=[1/4, 1/4, 1/2, 1], amp=0.8)

# Let it play for a while, then stop all sounds after 8 measures
Clock.future(8, Clock.clear)
