---
title: LFOmlog
date: 2019-05-08
tags:
  - LFO
  - Synthesizer
---


# LFOmlog


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/gBD8-8tB_Uo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** LFO, Synthesizer

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/03/LFOmlog.zip)**

Four independent LFOs control Cutoff Freq, Resonance, Attack, and Decay parameters of this two oscillator synth. Store up to 14 sequences. Features sequence overdub capabilities!

## Details

A cousin to Analog Style and Randomlog, LFOmlog is an independently tunable two oscillator synth featuring independent LFO control of Cutoff Freq, Resonance, Attack, and Decay parameters.

Set the range and center of each LFO-controlled parameter and then set the LFO rate.

Aux Button controls a new ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. With Aux pressed:

- The Top Row of Organelle keys selects the Menu command. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command (if applicable).
- The Bottom Row of keys selects one of 14 Sequence ‘slots’ to record to. Changing sequence slot will change the number that precedes the command in the left column.

Aux Menu Commands:

1. Seq Play/Stop – Plays/Stop selected Sequence.
2. Seq Record  
   a. When selected, Sequence is first Record Enabled. LED will be Pink. Sequencer is waiting for key press or incoming MIDI note.  
   b. When key pressed or MIDI Note received, Recording starts.  
   c. To end recording, press Aux (new seq begins looping immediately)
3. Seq Dub – Overdub on top of existing sequence. Counts in 3 Sec before starting recording.
4. Undo – Reverts Sequence to previous state.
5. Latch – Toggles Latch On or Off.
6. Sync: On/Off. When ‘On’: New note retriggers LFO back to 0 (zero) so that all notes are in same phase.

Footswitch: Toggles Latch On/Off

If sending MIDI clock or part of a Link session:

- Sequence length will be quantized to nearest quarter note.
- Sequence playback speed will sync to tempo

Note: For those users who become comfortable with the Aux menu: If you press both Aux and Menu command/Sequence Slot key before the menu is displayed, your choice/command will be accepted.
