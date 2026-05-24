---
title: CCquencer2
date: 2021-04-08
tags:
  - Automation
  - Utility
  - Sequencer
---


# CCquencer2


<div class="video-embed"><iframe width="560" height="315" src="https://www.youtube.com/embed/dMELEyLhjqI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Tags:** Automation, Utility, Sequencer

**[Download Patch](https://patchstorage.com/wp-content/uploads/2021/04/CCquencer2.zip)**

Automates EYESY controls via MIDI CC. Also synthesizes audio at frequencies ‘tuned’ for EYESY visuals.

## Details

WHAT IS THIS PATCH?  
CCquencer2 for Organelle automates EYESY video synth mode control via MIDI. Organelle Knobs 1-4 and the Vol knob are mapped to the five knobs of the EYESY as MIDI CCs. Organelle knob adjustments, key presses, and EYESY ‘Persist’ setting, can be recorded, looped, overdubbed, and sent to EYESY where the current EYESY mode will respond accordingly. Requires that the Organelle and EYESY are connected via MIDI either via EYESY’s USB-MIDI or TRS-MIDI input.

The keys are set to synthesize audio at frequencies that look ‘good’ when displayed in a EYESY oscilloscope (‘Scope’) mode. A given key’s frequency will be close to ‘frozen’ or alternate in an interesting way when displayed. This requires that the Organelle’s audio output to be connected to EYESY audio input. Change the waveform for visual variety.

HOW DO I USE THIS PATCH?  
A typical use case would be:   
1. Connect Organelle’s MIDI output and/or Audio Output to the EYESY's corresponding ports.  
2. Record a sequence of knob adjustments and/or a sequence of key presses.  
3. Overdub it, etc.  
4. Revisit the above steps in any order as needed.

To do steps 2 & 3 above you will need to use the ‘Aux Menu’. The Aux Button controls the ‘Aux Menu’. When you press Aux for 0.2 seconds, a new menu is displayed on OLED Screen for as long as you hold Aux. To select an Aux Menu command/Page, use the Top Row of Organelle keys. There are 10 possible commands selected by the 10 keys. The low C# key selects Top Left command. The High A# key selects the Bottom Right command. The Command Grid is to be read from top left to bottom, then top right to bottom.

The following commands are available on the Aux Menu's Right Column:  
Wave - Cycles through four waveforms for synthesizer.

VolDwn - Selecting this command will lower synth volume by 25% until it reaches 0%.

VolUp - Selecting this command will raise synth volume by 25% until it reaches 100%.

The following commands are available on the Aux Menu's Left Column:  
Seq:Play/Stop - Plays or Stops selected sequence

Rec:Off/Armd - Controls Keyboard Sequence Recording. When selected, Sequence is first Record Armed (Enabled). LED will be Pink. Sequencer is waiting for knob adjustment, key press or incoming MIDI note. When knob adjusted, key pressed or MIDI Note received, Recording starts. LED is Red. To end recording, press Aux (new seq begins looping immediately). LED will be Green and flash White on quarter note. Sequence length will be quantized to nearest quarter note.

Dub:Off/On – Overdub on top of existing sequence. Counts in 3 Sec before starting recording. To end recording, press Aux and sequence begins looping immediately.

Undo – Reverts Sequence to previous state. If this command says 'Undid' you cannot 'undo' further.

Latch: Off/On - Turn on to keep notes playing after release.

The Bottom Row of keys selects one of 14 Sequence ‘slots’ to record sequences to. Changing sequence slot will change the number that precedes the command in the left column.

When recording a sequence, you can record adjustments to the knobs!

TECH SPECS:  
Keys are / synth is monophonic.

To toggle EYESY 'Persist' command press the Organelle's highest key. (There is no audio synthesis on this key.)

Link enabled for syncing with other devices on a shared wireless network.

MIDI Start and Stop commands will start sequencer.

Foot Switch: Toggles EYESY 'Persist' setting.

If you view EYESY's OSD (on screen display), the knob graphs will appear red.
