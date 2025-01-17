s = Server.local;
s.boot;
// Define a simple sine wave synth 
SynthDef(\simpleSine, {
    |freq = 440, amp = 0.5|
    var sig;
    sig = SinOsc.ar(freq) * amp;
    Out.ar(0, sig ! 2);  // Output the signal to both left and right channels
}).add;
